from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "pfp.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jacob Moore"
PAGE_ICON = "random"
NAME = "Jacob Moore"
DESCRIPTION = "Recent Waikato Management School BMS(hons) graduate, double majoring in Economics and Strategic Management."
EMAIL = "jacob.moore0081@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jacob-moore-6083191a8/",
    "GitHub": "https://github.com/Sandhawk81",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)






# --- LOAD CSS, PDF & PFP ---
with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📝 Download CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="appliction/octet-stream",
    )
    st.write("✉️", EMAIL)


# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✅ Recently completed Bachelor of Managment Studies (hons) from Waikato University
- ✅ Basic understanding of Mandarin (currently learning)
- ✅ Basic understanding and proficiency in Python (I coded this in Python myself)
- ✅ Proficiency in MS Excel and Power BI
"""
)

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - 🗝️ Highly reliable and responsible
    - 🕑 Ability to excel under pressure
    - 👍 Good sense of initative
    - 💻 Technical ability
    - 🏛️ Organisational knowledge
    - 📣 Clear commuication
    - 🥇 Ability to work in a team or individually
    - 🤝 Good interpersonal skills
"""
)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("📈", "**Sales Consultant | Noel Leeming**")
st.write("Feb 2022 - Present")
st.write("Te Rapa")
st.write("As a part of the sales team, my responsibilities include:")
st.write(
    """
    - ➤ Ensuring customer satisfaction before, during, and continuing after the purchase is made
    - ➤ Completing sales goals and achieving KPIs
    - ➤ Maintaining a high level of professionalism
    - ➤ Sharing knowledge and advice with customers and co-workers about various products we sell
    - ➤ Studying and developing expertise in new products and models when they release
"""
)

# --- JOB 2
st.write("#")
st.write("💼", "**Intern | AFFCO New Zealand**")
st.write("July 2022 - November 2022")
st.write("Horotiu")
st.write("As an intern for the Hakarimata project team at AFFCO, my responsibilities included:")
st.write(
    """
    - ➤ Assisting in system migration
    - ➤ Data preparation and analysis
    - ➤ Developing training management tools
    - ➤ Streamlining logistics and distribution systems
"""
)
