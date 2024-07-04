# ds_algo_cp_page.py

import streamlit as st

def show_setup_page():
    st.set_page_config(
        page_title="Installations and Setup",
        page_icon="🔨"
    )

    st.write("# Installations and Setup! 🔨")

    st.sidebar.header("Installations and Setup")

    st.markdown(
        """

    ## Download Links:

    1. [Git](https://git-scm.com/downloads)
    2. [VScode](https://code.visualstudio.com/download)
    3. [NodeJS](https://nodejs.org/en/download)
    4. [Python](https://www.python.org/downloads/)

    ## Git/Github Setup

    - Git is a version control system that lets you manage and keep track of your source code history.
    - GitHub is a cloud-based hosting service that lets you manage Git repositories.

    - Create a GitHub account : [GitHub](https://github.com/)
    - Install Git : [Git](https://git-scm.com/downloads)

    ```sh
    git --version
    git config --global user.name "Your Name"
    git config --global user.email "Your Email"
    ```

    - Create a new repository on GitHub and clone it to your local machine.

    ```sh
    git clone <repository-name>
    cd <repository-name>
    ```

    - Make changes to the code 

    ```sh
    git status
    git add .
    git commit -m "Your Message"
    git push origin main
    ```

    ## Setup First Time

    ```sh
    git init
    git config --list
    git config --global user.name "Your Name"
    git config --global user.email "Your Email"
    git remote add origin https://<PAT>@github.com/<username>/<repo>
    """
    )

if __name__ == "__main__":
    show_setup_page()
