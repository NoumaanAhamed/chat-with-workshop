import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders.web_base import WebBaseLoader
from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders.markdown import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter,MarkdownTextSplitter
# from langchain_community.vectorstores.faiss import FAISS
from langchain_pinecone import PineconeVectorStore
from langchain_cohere import ChatCohere,CohereEmbeddings
from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


load_dotenv()

def get_vectorstore():
    # get the text in document form
    # loader = WebBaseLoader(url)
    loader = TextLoader('./index.md')
    document = loader.load()
    # split the document into chunks
    # text_splitter = RecursiveCharacterTextSplitter()
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)
    index_name="mega-workshop"
    # create a vectorstore from the chunks
    vector_store = PineconeVectorStore.from_documents(document_chunks, CohereEmbeddings(model='embed-english-light-v3.0'),index_name=index_name)
    # vector_store = FAISS.from_documents(document_chunks, OpenAIEmbeddings())

    return vector_store

def get_context_retriever_chain(vector_store):
    # llm = ChatCohere()
    # llm = ChatOpenAI()
    llm = ChatGroq(model="llama3-8b-8192")

    retriever = vector_store.as_retriever()
    
    # prompt = ChatPromptTemplate.from_messages([
    #   MessagesPlaceholder(variable_name="chat_history"),
    #   ("user", "{input}"),
    #   ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
    # ])

    prompt = ChatPromptTemplate.from_messages([
      MessagesPlaceholder(variable_name="chat_history"),
      ("user", "{input}"),
      ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the current question. " +
          "Don't leave out any relevant keywords. Only return the query and no other text.",)
    ])

    
    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
    
    return retriever_chain
    
def get_conversational_rag_chain(retriever_chain): 
    
    # llm = ChatCohere()
    # llm = ChatOpenAI()
    llm = ChatGroq(model="llama3-8b-8192")

    
    # prompt = ChatPromptTemplate.from_messages([
    #   ("system", "Answer the user's questions strictly based on the below context in Markdown. Do not exceed 100 words.:\n\n{context}"),
    #   MessagesPlaceholder(variable_name="chat_history"),
    #   ("user", "{input}"),
    # ])

    prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a personal tutor for students attending a workshop. You impersonate the workshop instructor. " +
          "Answer the user's questions based on the below context. " +
          "Whenever it makes sense, provide links to pages that contain more information about the topic from the given context. " +
          "Format your messages in markdown format.\n\n" +
          "Context:\n{context}"),
      MessagesPlaceholder(variable_name="chat_history"),
      ("user", "{input}"),
    ])

    
    stuff_documents_chain = create_stuff_documents_chain(llm,prompt)
    
    return create_retrieval_chain(retriever_chain, stuff_documents_chain)

def get_response(user_input):
    retriever_chain = get_context_retriever_chain(st.session_state.vector_store)
    conversation_rag_chain = get_conversational_rag_chain(retriever_chain)
    
    # response = conversation_rag_chain.invoke({
    #     "chat_history": st.session_state.chat_history,
    #     "input": user_input
    # })
    
    # return response['answer']
    response_stream = conversation_rag_chain.stream({
        "chat_history": st.session_state.chat_history,
        "input": user_input
    })

    for chunk in response_stream:
        content = chunk.get("answer", "")
        yield content

# app config
st.set_page_config(page_title="Chat with Workshop", page_icon="📕")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title("Chat with Workshop")
st.markdown(
    """
    Let us know what we can improve about the chatbot here: 
    [Feedback Form](https://forms.gle/tKQ4QMYBfe4jEgGq7)
"""
)
st.sidebar.header("Chat with Workshop")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello, I am your AI workshop Instructor. Ask me any doubts related to the workshop."),
    ]
if "vector_store" not in st.session_state:
    st.session_state.vector_store = get_vectorstore()    

# conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# user input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    # response = get_response(user_query)
    # st.session_state.chat_history.append(HumanMessage(content=user_query))
    # st.session_state.chat_history.append(AIMessage(content=response))
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    with st.chat_message("Human"):
        st.markdown(user_query)
    
    with st.chat_message("AI"):
        response = st.write_stream(get_response(user_query))
    st.session_state.chat_history.append(AIMessage(content=response))

# # conversation
# for message in st.session_state.chat_history:
#     if isinstance(message, AIMessage):
#         with st.chat_message("AI"):
#             st.write(message.content)
#     elif isinstance(message, HumanMessage):
#         with st.chat_message("Human"):
#             st.write(message.content)
