# machine_learning_page.py

import streamlit as st

def show_machine_learning_page():
    st.set_page_config(
        page_title="Machine Learning and Data Science",
        page_icon="🤖"
    )

    st.write("# Machine Learning and Data Science! 🤖")

    st.sidebar.header("Machine Learning and Data Science")

    st.markdown(
        """
### Resources:

- [Complete Roadmap](https://roadmap.sh/ai-data-scientist)
- [Data Science Roadmap](https://roadmap.sh/data-analyst)
- [Python and AI](https://www.youtube.com/@TechWithTim)
- [Math for ML](https://www.youtube.com/@3Blue1Brown)
- [Andrew NG Courses](https://www.deeplearning.ai/courses/)

### Recommended Tech Stack:

- **Language**: Python/ R/ Julia
- **Libraries**: numpy, pandas, matplotlib, scikit-learn, TensorFlow, PyTorch
- **Focus Area**: Computer Vision, NLP, Reinforcement Learning
- **Projects**: Work on real datasets and problems.

### Tips for ML and Data Science:

- **Math**: Learn Linear Algebra, Calculus, Probability, Statistics.
- **Programming**: Master Python and libraries like numpy, pandas.
- **Data Science**: Learn about EDA, Data Cleaning, Feature Engineering.
- **Machine Learning**: Learn about ML algorithms, Deep Learning, Reinforcement Learning.
- **Projects**: Work on real datasets and problems
- Get datasets from Kaggle, UCI ML Repository, etc.

    """
    )

if __name__ == "__main__":
    show_machine_learning_page()
