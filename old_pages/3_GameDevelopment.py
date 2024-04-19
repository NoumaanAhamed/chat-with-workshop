# game_development_page.py

import streamlit as st

def show_game_development_page():
    st.set_page_config(
        page_title="Game Development",
        page_icon="🎮"
    )

    st.write("# Game Development! 🎮")

    st.sidebar.header("Game Development")

    st.markdown(
        """
### Resources

- [Complete Roadmap](https://roadmap.sh/game-developer)
- [Unity Tutorials](https://learn.unity.com/)
- [Pygame Tutorials](https://www.youtube.com/@ClearCode)
- [Blender Tutorials](https://www.youtube.com/@blenderguru)

### Recommended Tech Stack:

- **Game Engines**: Unity / Unreal Engine / Godot
- **Libraries**: Pygame (Python) / SDL / OpenGL
- **Art**: Blender/Photoshop
- **Projects**: Start with either programming or art.

### Tips for Game Development:

- **Game Engines**: Choose one engine to start with.
- Start with either Programming or Art.
- **Programming**: Learn C# for Unity, C++ for Unreal Engine.
- **Art**: Learn Blender for 3D modeling, Photoshop for 2D art.
- **Projects**: Start with simple games and gradually move to complex ones.

    """
    )

if __name__ == "__main__":
    show_game_development_page()
