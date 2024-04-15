# cybersecurity_page.py

import streamlit as st

def show_cybersecurity_page():
    st.set_page_config(
        page_title="Cybersecurity",
        page_icon="🔒"
    )

    st.write("# Cybersecurity! 🔒")

    st.sidebar.header("Cybersecurity")

    st.markdown(
        """
### Resources:

- [Complete Roadmap](https://roadmap.sh/cyber-security)
- [Youtube Tutorials](https://www.youtube.com/@NahamSec)
- [Networking and Linux](https://www.youtube.com/@NetworkChuck)

### Key Areas:

- **Skills**: Networking, Linux, Programming (Python, C, C++), Web Development
- **Specialization**: Choose a field (Web Security, Network Security, etc.)
- **Certifications**: CEH, OSCP, CISSP

### Tips for Cybersecurity:

- Learn Networking and Linux basics.
- Master programming languages like Python,bash, C, C++.
- Learn about Cryptography, Ethical Hacking, Forensics.
- Choose a specialization and get certified.
- Practice on platforms like Hack The Box, TryHackMe.
- Keep on learning and stay updated with the latest trends.
"""
    )

if __name__ == "__main__":
    show_cybersecurity_page()
