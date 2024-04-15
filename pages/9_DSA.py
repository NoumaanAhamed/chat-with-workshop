# ds_algo_cp_page.py

import streamlit as st

def show_ds_algo_cp_page():
    st.set_page_config(
        page_title="Data Structures and Algorithms/Competitive Programming",
        page_icon="🧮"
    )

    st.write("# Data Structures and Algorithms/Competitive Programming! 🧮")

    st.sidebar.header("Data Structures and Algorithms/Competitive Programming")

    st.markdown(
        """

    ## Resources:

    1. [Interview prep](https://www.techinterviewhandbook.org/)
    2. [CP resources](https://drive.google.com/drive/u/2/folders/1YK2ropL10F-FU4ICItzy1qvT9EFMH5hU)
    3. [150 DSA problems](https://neetcode.io/)

    ## Websites to practice:

    - [LeetCode](https://leetcode.com/)
    - [Codeforces](https://codeforces.com/)
    - [HackerRank](https://www.hackerrank.com/)
    - [CodeChef](https://www.codechef.com/)
    - [AtCoder](https://atcoder.jp/)

    ## Tips:

    - Try to solve problems daily
    - Learn about Time Complexity, Space Complexity
    - Learn basic Data Structures - Arrays, Linked Lists, Stacks, Queues, etc
    - Study Sorting, Searching, Graphs, Trees, Dynamic Programming, etc
    - Explore Bit Manipulation, Recursion, Backtracking, Greedy algorithms, etc
    """
    )

if __name__ == "__main__":
    show_ds_algo_cp_page()
