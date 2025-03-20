import streamlit as st
import requests

# App ka title
st.title("Islamic Q&A - Quran & Hadith Answers")

# User se input lena
question = st.text_input("Apna sawal likhein:")

if st.button("Jawab Dekhein"):
    if question:
        # Quran API se data lena
        quran_response = requests.get("https://api.alquran.cloud/v1/quran/en.asad").json()
        hadees_response = requests.get("https://hadithapi.com/api/hadiths").json()

        # Quran ka jawab dikhana
        st.write("🔹 **Quran ka jawab:**")
        st.write(quran_response["data"]["surahs"][0]["ayahs"][0]["text"])

        # Hadees ka jawab dikhana
        st.write("🔹 **Hadees ka jawab:**")
        st.write(hadees_response.get("data", "Koi relevant hadees nahi mili."))
    else:
        st.warning("Sawal likhna zaroori hai!")
