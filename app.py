import streamlit as st

# Phrase data
phrases = {
    "Thank You": [
        "Thank you for your help!",
        "Thanks a lot for your support.",
        "Thank you so much!"
    ],
    "Sorry": [
        "Sorry I'm late.",
        "I'm really sorry for the confusion.",
        "Sorry, I didn’t mean to interrupt."
    ],
    "Please": [
        "Please pass the salt.",
        "Please help me carry this.",
        "Please close the window."
    ],
    "Welcome": [
        "Welcome to the team!",
        "You're always welcome here.",
        "Welcome to our event!"
    ],
    "Congratulations": [
        "Congratulations on your promotion!",
        "Congratulations, you did it!",
        "Congratulations on your big day!"
    ]
}

# Streamlit UI
st.title("Golden Words Phrase Viewer")

selected = st.selectbox("Choose a Golden Word:", list(phrases.keys()))

if selected:
    st.subheader(f"{selected} Phrases:")
    for i, line in enumerate(phrases[selected], 1):
        st.write(f"{i}. {line}")
