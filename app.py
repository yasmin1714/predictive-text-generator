import streamlit as st
from model import (
    train_from_csv,
    predict_next_word,
    add_user_sentence,
    add_frequent_word
)

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Predictive Text Generator",
    page_icon="⌨️",
    layout="centered"
)

# ---------- HEADER ----------
st.markdown(
    """
    <h1 style='text-align: center;'>⌨️ Predictive Text Generator</h1>
    <p style='text-align: center; color: gray;'>
    Autocomplete-style word prediction using NLP & Markov Chain
    </p>
    """,
    unsafe_allow_html=True
)

# ---------- TRAIN MODEL ----------
@st.cache_data
def load_model():
    from model import train_default_data
    train_default_data()
    return True

load_model()

# ---------- MAIN TABS ----------
tab1, tab2 = st.tabs(["🔮 Predict Word", "➕ Custom Dictionary"])

# ---------- TAB 1: PREDICTION ----------
with tab1:
    st.subheader("🔮 Word Prediction")

    user_input = st.text_input(
        "Type a sentence",
        placeholder="e.g. i love machine"
    )

    if st.button("Predict Next Word"):
        if user_input.strip():
            prediction = predict_next_word(user_input)
            st.success(f"💡 Suggested word: **{prediction}**")
        else:
            st.warning("Please enter some text")

# ---------- TAB 2: CUSTOM DICTIONARY ----------
with tab2:
    st.subheader("➕ Add Custom Data")

    st.markdown("#### Add a Sentence")
    sentence = st.text_input(
        "Sentence",
        placeholder="e.g. i love natural language processing"
    )

    if st.button("Add Sentence"):
        if sentence.strip():
            add_user_sentence(sentence)
            st.success("✅ Sentence added successfully")
        else:
            st.warning("Please enter a sentence")

    st.markdown("---")

    st.markdown("#### ⭐ Add Frequently Used Word")

    col1, col2 = st.columns(2)
    with col1:
        prev_word = st.text_input("Previous Word", placeholder="e.g. i")
    with col2:
        freq_word = st.text_input("Frequently Used Word", placeholder="e.g. am")

    if st.button("Add Frequent Word"):
        if prev_word and freq_word:
            add_frequent_word(prev_word, freq_word)
            st.success("⭐ Frequent word added successfully")
        else:
            st.warning("Fill both fields")

# ---------- FOOTER ----------
st.markdown("---")
st.info(
    """
    **Key Features Implemented**
    • Word Prediction  
    • Context Awareness  
    • Customizable Dictionary  
    • Frequently Used Words  
    • Markov Chain (n-gram) Model  
    """
)
