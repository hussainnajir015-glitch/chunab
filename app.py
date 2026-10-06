import streamlit as st
import base64

# Page configuration
st.set_page_config(
    page_title="संकल्प सबल संगठन",
    page_icon="🇳🇵",
    layout="centered"
)

# ---- Function to encode image to base64 ----
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load images
bg_image = get_base64_image("background.jpg")
front_image = get_base64_image("front_image.png")

# ---- Custom CSS ----
st.markdown(f"""
    <style>
        /* Background image */
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Dark overlay so white text stays readable everywhere */
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-color: rgba(0, 0, 0, 0.65);
            z-index: -1;
        }}

        /* ---- UNIVERSAL FONT STYLING ---- */
        /* Works on any background: text has a soft shadow for readability */
        html, body, [class*="css"], .stMarkdown, .stText,
        p, h1, h2, h3, h4, h5, h6, span, div, label {{
            color: #FFFFFF !important;
            font-family: 'Noto Sans Devanagari', 'Mukta', 'Poppins', 
                         'Segoe UI', Arial, sans-serif !important;
            text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.85),
                         0 0 12px rgba(0, 0, 0, 0.6) !important;
            line-height: 1.7 !important;
        }}

        h1 {{
            text-align: center;
            font-size: 2.4rem !important;
            font-weight: 800 !important;
            letter-spacing: 0.5px;
        }}

        h3 {{
            text-align: center;
            font-size: 1.7rem !important;
            font-weight: 700 !important;
            margin-top: 2rem;
        }}

        .main .block-container {{
            padding-top: 3rem;
            padding-bottom: 3rem;
            max-width: 800px;
        }}

        /* ---- Highlighted card for the message (improves readability) ---- */
        .message-card {{
            background-color: rgba(0, 0, 0, 0.55);
            border: 2px solid rgba(255, 255, 255, 0.35);
            border-radius: 16px;
            padding: 28px 26px;
            margin: 20px auto;
            max-width: 720px;
            backdrop-filter: blur(6px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
        }}

        .message-card p {{
            font-size: 17px;
            margin-bottom: 14px;
        }}

        .signature {{
            text-align: right;
            font-weight: 700;
            font-size: 18px !important;
            margin-top: 18px;
            color: #FFD700 !important;
        }}

        /* Gmail button */
        .gmail-btn {{
            display: inline-block;
            background-color: #FFFFFF;
            color: #000000 !important;
            padding: 12px 28px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            font-size: 16px;
            transition: 0.3s;
            border: 2px solid #FFFFFF;
            text-shadow: none !important;
        }}
        .gmail-btn:hover {{
            background-color: #000000;
            color: #FFFFFF !important;
            border: 2px solid #FFFFFF;
        }}

        .footer {{
            text-align: center;
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 1px solid #555555;
        }}

        #MainMenu, footer, header {{ visibility: hidden; }}
    </style>
""", unsafe_allow_html=True)

# ---- Front image ----
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(
        f'<div style="text-align:center;">'
        f'<img src="data:image/png;base64,{front_image}" '
        f'style="width:180px; height:auto; border-radius:12px;" />'
        f'</div>',
        unsafe_allow_html=True
    )

# ---- Page Content ----
st.markdown("<h1>संकल्प सबल संगठन</h1>", unsafe_allow_html=True)

st.markdown("<h3>About</h3>", unsafe_allow_html=True)

# ---- Nepali Message Card ----
st.markdown("""
    <div class="message-card">
        <p>✊🇳🇵 <b>संकल्प सबल संगठनको, अपिल यहाँहरूको अमूल्य मतको!</b></p>
        <p>पार्टी सुदृढीकरण र भावी योजनाका विषयमा केन्द्रित संवादको अर्को अंश।</p>
        <p>१५औँ महाधिवेशनमा मुस्लिम कोटाबाट केन्द्रीय सदस्य पदका लागि देशभरिका 
           आदरणीय महाधिवेशन प्रतिनिधि साथीहरूको विश्वास र अमूल्य मतको अपेक्षा गर्दछु।</p>
        <p class="signature">— महमद जवार दिन मिया<br>
           <span style="font-size:14px; color:#FFFFFF !important;">
           (Mahamad Jabar Din Miya)</span></p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---- Footer ----
st.markdown("""
    <div class="footer">
        <p style='font-size:16px;'>Contact us:</p>
        <a href="mailto:yourname@gmail.com" class="gmail-btn" target="_blank">
            ✉️ Send Gmail
        </a>
        <p style='font-size:14px; margin-top:20px;'>© 2024 संकल्प सबल संगठन</p>
    </div>
""", unsafe_allow_html=True)