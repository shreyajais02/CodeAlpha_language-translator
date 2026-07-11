import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#22010b,#3b0715,#4d0b1f);
color:white;
}

h1{
text-align:center;
font-size:50px;
color:#ffd3a5;
}

p{
text-align:center;
color:#f5dcdc;
font-size:18px;
}

textarea{
background:#350714 !important;
color:white !important;
border:2px solid #ff4d79 !important;
border-radius:15px !important;
}

.stSelectbox div[data-baseweb="select"]{
background:#350714;
color:white;
border-radius:12px;
}

div.stButton > button{
width:100%;
height:55px;
background:linear-gradient(90deg,#d4145a,#fbb03b);
color:white;
font-size:20px;
font-weight:bold;
border:none;
border-radius:15px;
cursor:pointer;
box-shadow:0 0 15px #ff4d79;
transition:all .3s ease-in-out;
}

div.stButton > button:hover{
transform:scale(1.05);
box-shadow:
0 0 20px #ff4d79,
0 0 40px #ff4d79,
0 0 60px #ff4d79;
}

.result{
background:#300612;
border:2px solid #ff4d79;
border-radius:18px;
padding:20px;
font-size:28px;
font-weight:bold;
color:white;
margin-top:20px;
box-shadow:0 0 20px rgba(255,70,120,.5);
}

</style>
""", unsafe_allow_html=True)

text = st.text_area("Enter text")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

source = st.selectbox("Source Language", languages.keys())
target = st.selectbox("Target Language", languages.keys())

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translated Text:")
        st.write(translated)
    else:
        st.warning("Please enter some text.")

     