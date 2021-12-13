import streamlit as st 
from PIL import Image 

st.title("Game Academic Projects") 

st.header("VR Healthcare System for Patients with Trypanophobia") 
st.caption("Final Year Project (Jul 2020 ~ Mar 2021)") 
st.write("Virtual reality game which combats needle fear among pediatric patients.") 
vid1 = open("demos/FYPDemo.mov", "rb") 
st.video(vid1, format = "video/quicktime") 
st.caption("Language: C#") 
st.caption("Framework: Google VR SDK, Unity, Visual Studio") 

st.header("Lost Robot") 
st.caption("Game Physics (Nov 2020 ~ Mar 2021)") 
st.write("2D sci-fi game built to simulate physics algorithm in games.") 
#st.video("") 
st.caption("Language: C++") 
st.caption("Framework: OpenGL") 

st.header("Upgrade") 
st.caption("3D Game Programming (Nov 2020 ~ Mar 2021)") 
st.write("3D Action platformer game developed to explore the utilities of the Unity Engine.") 
#st.video("") 
st.caption("Language: C#") 
st.caption("Framework: Unity, Visual Studio") 

st.header("MagnifiCast") 
st.caption("Game Production (Nov 2020 ~ Mar 2021)") 
st.write("Tower defense mobile game developed from competitive analysis of mechanically similar games on the market.") 
#st.video("") 
st.caption("Language: C#") 
st.caption("Framework: Android, Unity, Visual Studio") 

st.header("Todd") 
st.caption("Game Design Fundamentals (Nov 2019 ~ Mar 2020)") 
st.write("2D platformer PC game built with emphasis on level design and 2D sprite managements.") 
st.markdown("![Alt Text](https://raw.githubusercontent.com/Heeuul/temportfolio/main/demos/ToddDemo.gif)") 
st.caption("Language: JavaScript") 
st.caption("Framework: Phaser2, Visual Studio") 

st.header("Violet World") 
st.caption("Computer Graphic Fundamentals (Nov 2019 ~ Mar 2020)") 
st.write("Imaginative 3D world of outer space fully built with program codes.") 
#st.image("") 
st.caption("Language: C++") 
st.caption("Framework: Code::Blocks, OpenGL") 
