# app_development_page.py

import streamlit as st

def show_app_development_page():
    st.set_page_config(
        page_title="App Development",
        page_icon="📱"
    )

    st.write("# App Development! 📱")

    st.sidebar.header("App Development")

    st.markdown(
        """
### Resources

- [Flutter + Jetpack Compose](https://salt-manchego-99d.notion.site/Flutter-Jetpack-Compose-An-App-Development-Course-98dfc4caa0814175bb82da273a39b171)
- [Other roadmaps](https://roadmap.sh/)

### Recommended Tech Stack:

- **Android**: Java/Kotlin/Jetpack Compose
- **iOS**: Swift
- **Cross Platform**: React Native/Flutter
- **Backend**: Firebase/Node.js
- **Projects**: Focus on practical app development.

### Tips for App Development:

- **Choose Platform**: Decide between Native or Cross Platform.
- **Languages**: Stick to one language for each platform.
- **Projects**: Build multiple apps to gain experience.

    """
    )

if __name__ == "__main__":
    show_app_development_page()
