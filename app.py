import streamlit as st
import qrcode
from io import BytesIO

st.title("🔳 QR Maker")

text = st.text_input("Enter URL or text")

if st.button("Generate"):
    if not text:
        st.warning("Input tidak boleh kosong")
    else:
        qr = qrcode.make(text)
        buf = BytesIO()
        qr.save(buf, format="PNG")
        buf.seek(0)

        st.image(buf)
        st.download_button(
            "Download QR",
            buf,
            file_name="qrcode.png",
            mime="image/png"
        )
