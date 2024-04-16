import streamlit as st


st.set_page_config(
    page_title="Vscode, Git & GitHub",
    page_icon="🗒️",
)

st.write("# Vscode, Git & GitHub")

st.sidebar.success("Vscode, Git & GitHub")

st.markdown(
    """
    ## VSCode, Git, and Github

This guide provides a basic overview of using Visual Studio Code (VSCode), Git version control, and GitHub for collaborative coding.

### VSCode

VSCode is a popular, free, and open-source code editor with built-in Git integration. It offers features like syntax highlighting, code completion, debugging, and a built-in terminal.

* **Installation:** Download and install VSCode from the official website: https://code.visualstudio.com/download

### Git

Git is a version control system (VCS) that allows you to track changes in your code over time. It helps you:

* Maintain a history of your code
* Revert to previous versions if needed
* Collaborate with other developers

### GitHub

GitHub is a web-based platform for version control using Git. It provides additional features like:

* Code hosting
* Issue tracking
* Project management
* Collaboration tools

Here's a basic workflow for using these tools together:

1. **Create a project directory:** Create a directory for your project on your local machine.
2. **Initialize a Git repository:** Open a terminal in your project directory and run `git init`. This creates a hidden `.git` folder to store Git data.
3. **Open the project in VSCode:** Open your project folder in VSCode. The Git integration features will be available.
4. **Create and edit files:** Create and edit your code files in VSCode.
5. **Stage changes:** Use the Git features in VSCode to stage (add) the changes you want to track in the next commit.
6. **Commit changes:** Create a snapshot of your staged changes with a descriptive commit message.
7. **Push to GitHub:** Create a remote repository on GitHub and push your local commits to it. This makes your code accessible online and allows collaboration.

**Benefits of using VSCode, Git, and Github:**

* **Version control:** Track changes and revert to previous versions if needed.
* **Collaboration:** Work with other developers on the same project.
* **Code sharing:** Share your code publicly or privately on GitHub.
* **Open source contribution:** Contribute to open-source projects hosted on GitHub.

**Further Resources:**

* VSCode documentation: https://code.visualstudio.com/docs
* Git documentation: https://git-scm.com/
* GitHub guides: https://docs.github.com/

This is a basic introduction. There's a lot more to explore with these powerful tools!

"""
)

if __name__ == "__main__":
    vscode_git_github_page()
