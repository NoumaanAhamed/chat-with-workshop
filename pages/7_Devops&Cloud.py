# devops_cloud_page.py

import streamlit as st

def show_devops_cloud_page():
    st.set_page_config(
        page_title="DevOps and Cloud",
        page_icon="☁️"
    )

    st.write("# DevOps and Cloud! ☁️")

    st.sidebar.header("DevOps and Cloud")

    st.markdown(
        """
### Resources:

- [Devops Roadmap](https://roadmap.sh/devops)
- [Cloud Roadmap](https://roadmap.sh/aws)
- [Youtube Tutorials](https://www.youtube.com/@AbhishekVeeramalla)

### Focus Areas:

- **Cloud Provider**: AWS, Azure, GCP
- **Tools**: Docker, Kubernetes, Jenkins, Ansible, Terraform
- **Certifications**: AWS, Azure, GCP, Docker, Kubernetes

### Tips for DevOps and Cloud:

- Choose a Cloud Provider to start with,AWS is recommended.
- Learn about Virtualization, Containers, CI/CD, Monitoring, Logging.
- Master tools like Docker, Kubernetes, Jenkins, Ansible, Terraform.
- Get certified in AWS, Azure, GCP, Docker, Kubernetes.
- Practice on platforms like AWS, Azure, GCP.

        """
    )

if __name__ == "__main__":
    show_devops_cloud_page()
