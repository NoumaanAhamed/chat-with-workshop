# ds_algo_cp_page.py

import streamlit as st

def show_project_page():
    st.set_page_config(
        page_title="Projects and Other Domains",
        page_icon="📽️"
    )

    st.write("# Projects and Other Domains! 📽️")

    st.sidebar.header("Projects and Other Domains")

    st.markdown(
        """
## Other Domains?

- **UI/UX Design**: Learn Figma, Adobe XD, Sketch, Zeplin
- **Product Management**: Learn about Agile, Scrum, Kanban, Jira, Trello
- **Technical Writing**: Learn about Documentation, Blogging, Content Writing
- **Open Source**: Contribute to projects on GitHub
- **Low Code/No Code**: Learn about Bubble, Webflow, Adalo, Glide
- **Hardware/IoT**: Learn about Arduino, Raspberry Pi, Sensors, Robotics
- **Low Level Programming**: Learn about C, Assembly, Operating Systems, Compilers
- **AR/VR**: Learn about Unity, Unreal Engine, ARCore, ARKit, Oculus, HTC Vive

## Projects

- [Intermediate to Advanced WebDev + Web3](https://www.youtube.com/@harkirat1)
- [GenAI Projects](https://www.youtube.com/@alejandro_ao)
- [Good Web Development Projects](https://www.youtube.com/@javascriptmastery)
- [Advanced Web Development Projects](https://www.youtube.com/@codewithantonio)
- [Software Engineering Projects](https://github.com/codecrafters-io/build-your-own-x)
    """
    )

if __name__ == "__main__":
    show_project_page()
