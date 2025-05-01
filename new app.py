import streamlit as st

# Phrase data
phrases = {
    "Thank You": [
        "Thank you for your help!",
        "Thanks a lot for your support.",
        "Thank you so much!",
        "Thanks for being there for me.",
        "I truly appreciate your assistance.",
        "Thank you for your kindness.",
        "Many thanks for your time.",
        "Thanks a ton!",
        "Thanks for everything you’ve done.",
        "I’m grateful for your help."
    ],
    "Sorry": [
        "Sorry I'm late.",
        "I'm really sorry for the confusion.",
        "Sorry, I didn’t mean to interrupt.",
        "I apologize for the inconvenience.",
        "My apologies for the mistake.",
        "I’m sorry if I upset you.",
        "Please forgive me.",
        "Sorry, that was my fault.",
        "I regret what happened.",
        "Apologies for the delay."
    ],
    "Please": [
        "Please pass the salt.",
        "Please help me carry this.",
        "Please close the window.",
        "Could you please explain that again?",
        "Please make yourself comfortable.",
        "Please wait a moment.",
        "Please be honest with me.",
        "Please don’t forget to call me.",
        "Please let me know your thoughts.",
        "Please turn off the lights."
    ],
    "Welcome": [
        "Welcome to the team!",
        "You're always welcome here.",
        "Welcome to our event!",
        "A warm welcome to all our guests.",
        "Welcome aboard the project!",
        "Welcome back!",
        "Welcome, it's great to see you!",
        "Feel welcome to ask anything.",
        "Welcome to our home.",
        "Welcome! We hope you enjoy your time."
    ],
    "Congratulations": [
        "Congratulations on your promotion!",
        "Congratulations, you did it!",
        "Congratulations on your big day!",
        "Well done, congratulations!",
        "Heartfelt congratulations on your achievement!",
        "Congrats on your success!",
        "Many congratulations on the new job!",
        "Kudos to you!",
        "You deserve all the congratulations!",
        "Big congratulations on the milestone!"
    ],
    "Excuse Me": [
        "Excuse me, can I ask you something?",
        "Excuse me, do you have a moment?",
        "Excuse me for interrupting.",
        "Excuse me, I didn’t mean to bump into you.",
        "Excuse me, where is the restroom?",
        "Excuse me, may I come in?",
        "Excuse me, I need some help here.",
        "Excuse me, could you please repeat that?",
        "Excuse me for a moment.",
        "Excuse me, I have a question."
    ]
}

# Streamlit UI
st.title("Golden Words Phrase Viewer")

selected = st.selectbox("Choose a Golden Word:", list(phrases.keys()))

if selected:
    st.subheader(f"{selected} Phrases:")
    for i, line in enumerate(phrases[selected], 1):
        st.write(f"{i}. {line}")
