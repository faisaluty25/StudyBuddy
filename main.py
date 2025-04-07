import streamlit as st

# Set page configuration
st.set_page_config(page_title="Welcome to StudyBuddy", page_icon="🎓", layout="wide")

# --------
# Navigation links
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.page_link(r"main.py", label="Home", icon="🏠")

# with col2:
#     st.page_link(r"Pages\2-chat.py", label="ChatBot", icon="🤖")

# with col3:
#     st.page_link(r"Pages\3-About-Me.py", label="About Me", icon="🙋‍♂️")
# ---------

# Title and intro
st.title("👋 Welcome to StudyBuddy!")
st.markdown("---")

# Overview of the chatbot
st.subheader("📘 About the Chatbot")
st.markdown("""
**StudyBuddy** is your friendly study assistant chatbot designed to help you stay motivated, focused, and organized while studying.

It can help with:
- 📅 **Time management tips**
- ✍️ **Note-taking techniques**
- 🧠 **Memory and concentration tips**
- 📚 **Exam preparation advice**
- 💬 Friendly support to keep you going!

Whether you're tired, unmotivated, or just looking for the best way to prepare for an exam — **StudyBuddy is here for you**!
""")

# How it works
st.subheader("🤖 How it Works")
st.markdown("""
- Go to the **Chat** page from the sidebar.
- Type your question or message into the chat box at the bottom.
- Click the **Send** button to get a response.
- Chat as much as you'd like — your messages will appear in a friendly conversation format.

The chatbot uses regular expressions and a set of helpful responses to understand your input and reply with study tips tailored to your needs.
""")

# Example questions
st.subheader("💡 Example Questions You Can Ask")
st.markdown("""
- "How can I stay focused while studying?"
- "What's the best way to prepare for an exam?"
- "I'm feeling unmotivated, help!"
- "Any tips to manage my time better?"
""")

st.subheader("💬 Example Problems You Can Ask About")
st.markdown("""
- "I'm having trouble studying or understanding the topic."
- "I can't focus. I get easily distracted!"
- "I forget what I study and have a hard time memorizing things."
""")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Python and Streamlit by Faisal Almufarrih 👨🏻‍💻")

