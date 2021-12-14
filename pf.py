import streamlit as st 
from streamlit_player import st_player 
from PIL import Image 

st.title("Game Academic Projects") 

st.header("VR Healthcare System for Patients with Trypanophobia") 
st.caption("Final Year Project (Jul 2020 ~ Mar 2021)") 
st.write("Virtual reality game which combats needle fear among pediatric patients.") 
st.video("https://nd67kg.dm.files.1drv.com/y4mNYdxjro5bFm0IuSoOFcIyGea9299G2qvlDBWZ-J4VxYxkGbpGqoSTn36Fn8HiwckxEWLukDZhsxMJ0y-cR6C83X6P0RKqrThnCeI9yZsueUS_tvmOK_L6xjs4j_zvWaWiLiyG6YjvB7nyYFI4jptKM0cb47abzxpIz5Kz5NZkE0pZaK_JvkzIPZTLY98n_OWBcq0ylS4LtPw4Bb5D65QKQ") 
col1, col2 = st.columns(2) 
with col1: 
	st.caption("Language: C#") 
with col2: 
	st.caption("Framework: Google VR SDK, Unity, Visual Studio") 

st.header("Lost Robot") 
st.caption("Game Physics (Nov 2020 ~ Mar 2021)") 
st.write("2D sci-fi game built to simulate physics algorithm in games.") 
st.image("demos/LostRobotDemo.gif") 
col1, col2 = st.columns(2) 
with col1: 
	st.caption("Language: C++") 
with col2: 
	st.caption("Framework: Box2D, SFML, OpenGL") 

st.header("Upgrade") 
st.caption("3D Game Programming (Nov 2020 ~ Mar 2021)") 
st.write("3D action platformer game developed to explore the utilities of the Unity Engine.") 
st.video("https://nd7gkg.dm.files.1drv.com/y4m3Xxb2GcNMOVZdCvbvGtg0e5NIMAvcvhQuDdxcW9tZ1FN8AZcOMfplpnZUvYr-xEtcmHPhXFMuP4Uu49OiM_mCf1WpQmlx7z7ekEnwPfSjhhFiV9anQ-4oklvkTYX57lRPiph3d5RFHsVb8nf0RGETzI-sAlatz58l3Q_caUFRkOj7PfVm_h9IpZgfCerIVm6Pj-eDtZwCuM748FJHhvt4A") 
col1, col2 = st.columns(2) 
with col1: 
	st.caption("Language: C#") 
with col2: 
	st.caption("Framework: Unity, Visual Studio") 

st.header("MagnifiCast") 
st.caption("Game Production (Nov 2020 ~ Mar 2021)") 
st.write("Tower defense mobile game developed from competitive analysis of mechanically similar games on the market.") 
st_player("https://nd68kg.dm.files.1drv.com/y4m5yAghoSk16j_D0kAr-Rys-ODulmrCM9do9gtYJ_picdCwS1dBAv_fo00AU_wmNotsVEsV6WhTqrb2KCPOWRDsoqJBYi4NZkSZY2oU4K5adDFKI3Qa9YogLh7YlkyNoXGtgOe_rAzKAA4il6B1_AZm3Yihv_3Cc207PNxlWWeyCKX3FSn2XVTDHlD9KxbwGaFoj3WzvaeG7W2tBPR3bwBpg") 
col1, col2 = st.columns(2) 
with col1: 
	st.caption("Language: C#") 
with col2: 
	st.caption("Framework: Android, Unity, Visual Studio") 

st.header("Todd") 
st.caption("Game Design Fundamentals (Nov 2019 ~ Mar 2020)") 
st.write("2D platformer web game built with emphasis on level design and 2D sprite managements.") 
st_player("https://nd7fkg.dm.files.1drv.com/y4mMK8ihDVuBSXJjUJi2B9285juzxc9WK_NVOWE5SUsx5RSED3t9dhdfwMzCKcgGNfhH51mm0Z-r4YQFcm2iBaxuMDVLhw5-3DB_iDkSq2lebXdL-vw_wlKgECrkcZkQBf1WedL3vdPt4tirolQiRiPZaNKkGibpQW2d6i65Mpbjsz2I7Q46znhjBHtPfVQSg2EGtXviaFRxxIpdhKV2xvPqA") 
col1, col2 = st.columns(2) 
with col1: 
	st.caption("Language: JavaScript") 
with col2: 
	st.caption("Framework: Phaser2, Visual Studio") 

st.header("Violet World") 
st.caption("Computer Graphic Fundamentals (Nov 2019 ~ Mar 2020)") 
st.write("Imaginative 3D world of outer space fully built with program codes.") 
st.image("demos/VioletWorldDemo.gif") 
col1, col2 = st.columns(2) 
with col1: 
	st.caption("Language: C++") 
with col2: 
	st.caption("Framework: Code::Blocks, OpenGL") 
