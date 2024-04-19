# generative_ai_page.py

import streamlit as st

def show_generative_ai_page():
    st.set_page_config(
        page_title="Generative AI",
        page_icon="🧠"
    )

    st.write("# Generative AI! 🧠")

    st.sidebar.header("Generative AI")

    st.markdown(
        """
### Resources:

- [Learn Python](https://www.learnpython.org/)
- [Prompt Engineering](https://roadmap.sh/prompt-engineering)
- [GenAI Projects](https://www.youtube.com/@krishnaik06)

### Technologies:

- **Python**: Core language
- **Tools**: Hugging Face, Langchain, Prompt Engineering
- **Projects**: Explore generative AI concepts.

### Tips for GenAI:

- Start with Python basics.
- Learn about LLMs and Prompt Engineering.
- Learn about Langchain
- Streamlit for Frontend
- FastAPI for Backend
- Vector Databases and Embeddings (RAG)
- AI Agents
    """
    )

if __name__ == "__main__":
    show_generative_ai_page()
