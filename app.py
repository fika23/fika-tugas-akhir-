import streamlit as st

st.set_page_config(page_title="Aplikasi Web Sederhana", layout="centered")

st.title("🌐 Aplikasi Web Berbasis Streamlit")
st.write("Ini adalah contoh aplikasi web sederhana menggunakan **Streamlit**.")

menu = st.sidebar.radio("Menu", ["Home", "Tentang", "Kontak"])

if menu == "Home":
    st.subheader("Halaman Home")
    st.write("Selamat datang di aplikasi web sederhana ini!")
elif menu == "Tentang":
    st.subheader("Tentang Aplikasi")
    st.info("Aplikasi ini dibuat dengan Python dan Streamlit.")
elif menu == "Kontak":
    st.subheader("Kontak")
    st.write("Email: contoh@email.com")
    st.write("Instagram: @contoh")
