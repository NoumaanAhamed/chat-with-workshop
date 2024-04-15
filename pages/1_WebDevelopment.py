# web_development_page.py

import streamlit as st

def show_web_development_page():
    st.set_page_config(
        page_title="Web Development",
        page_icon="🌐"
    )

    st.write("# Web Development! 🌐")

    st.sidebar.header("Web Development")

    st.markdown(
        """
### Resources

- [Complete Roadmap](https://roadmap.sh/full-stack)
- [Basics to Full stack](https://www.theodinproject.com/)
- [Learn UI/UX](https://learnuiux.in/) (optional)

### Recommended Tech Stack:

- **Frontend**: HTML/CSS, JavaScript, React/Next.js
- **Backend**: SpringBoot/Express/Django
- **Databases**: SQL/NoSQL (MongoDB/Postgres)
- **Projects**: Build multiple projects to solidify skills.

### Tips for Web Development:

- **Focus**: Choose either Frontend or Backend to start with.
- **Projects**: After learning one stack, start building projects.

    """
    )

if __name__ == "__main__":
    show_web_development_page()
