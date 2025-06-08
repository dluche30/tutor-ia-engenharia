
import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    st.warning("⚠️ A chave da OpenAI não foi carregada. Verifique os 'Secrets' no Streamlit Cloud.")

st.title("Tutor IA para Engenharia")

prompt = st.text_area("Digite sua dúvida:", "")

if st.button("Enviar") and prompt.strip() != "":
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "Você é um tutor de engenharia útil e claro."},
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post("https://api.openai.com/v1/chat/completions",
                                 headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        st.success(reply)
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
