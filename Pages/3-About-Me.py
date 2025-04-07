import streamlit as st
import base64
import os



# Set page config (must be at the top)
st.set_page_config(page_title="About Me", layout="wide", page_icon="🙋‍♂️")

# Top navigation bar
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("main.py", label="Home", icon="🏠")

with col2:
    st.page_link("Pages/2-chat.py", label="ChatBot", icon="🤖")

with col3:
    st.page_link("Pages/3-About-Me.py", label="About Me", icon="🙋‍♂️")

# Page title
st.markdown('<h1 style="text-align: center; color: #00BFA6; font-weight: bold; margin-bottom: 10px;">Built with Passion by Faisal Almufarrih</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align: center; color: #666; margin-bottom: 30px;">Created and developed by a passionate learner</h3>', unsafe_allow_html=True)

# Custom CSS styling
# 💅 Custom CSS with teal + gradient + smooth style
st.markdown("""
    <style>
        /* Gradient header text */
        h1, h3 {
            font-family: 'Segoe UI', sans-serif;
        }

        .profile-card {
            background: linear-gradient(145deg, #f8f9fa, #ffffff);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            max-width: 400px;
            margin: 40px auto;
        }

        .profile-image {
            width: 160px;
            height: 160px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid #00BFA6;
            margin-bottom: 20px;
        }

        .member-name {
            color: #222;
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .member-role {
            color: #00BFA6;
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 20px;
        }

        .button-container a {
            background-color: #00BFA6;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            margin: 5px;
            display: inline-block;
            transition: background-color 0.3s ease;
        }

        .button-container a:hover {
            background-color: #009e88;
        }
    </style>
""", unsafe_allow_html=True)


# 🔁 Convert local image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ✅ Update this to your correct image path
image_path = r"C:\Users\AHC\Desktop\Tuwaiq-Projects\ChatBot(Eliza)\StudyBuddy\linkedin Image.jpg"

if os.path.exists(image_path):
    image_base64 = get_base64_image(image_path)

    # Profile card
    st.markdown(f"""
        <div class="profile-card">
            <img src="data:image/jpeg;base64,{image_base64}" class="profile-image">
            <div class="member-name">Faisal Almufarrih</div>
            <div class="member-role">Artificial Intelligence Engineer</div>
            <div class="button-container">
                <a href="https://www.linkedin.com/in/faisal-almufarrih-b8090628b" target="_blank">LinkedIn</a>
                <a href="https://github.com/faisaluty25" target="_blank">GitHub</a>
            </div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.error("❌ Profile image not found. Please check the file path.")
