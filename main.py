import streamlit as st
import re 

st.set_page_config(page_title="SecurePass Analyzer", page_icon="🔐")

st.title("SecurePass Analyzer🔑")

st.markdown("""
## Welcome To SecurePass Analyzer!  
Ensure Your Password Is Strong And Secure With This Handy Tool.  
Get Instant Feedback And Tips To Enhance Your Password’s Security 🔒.
""")

password = st.text_input("Enter Your Password", type="password") 

feedback = []
score = 0

if password: 
    if len(password) >= 8:
        score += 1 
    else:
        feedback.append("❌ Your password must be at least 8 characters long.")
        
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
        
    if re.search(r'\d', password):
        score += 1
    else: 
        feedback.append("❌ Add at least one number for better security.")
        
    if re.search(r'[!@#$%&]', password):
        score += 1
    else: 
        feedback.append("❌ Use at least one special character (!@#$%&) to strengthen your password.")

    if score == 4:
        feedback.append("✅ Your password is strong! 👍") 
    elif score == 3:
        feedback.append("⚠️ Your password is moderately strong! 👎") 
    else:
        feedback.append("❌ Your password is weak! ⛔")
        
    if feedback:
        st.markdown("## Suggestions for a Stronger Password")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Enter a password to check its strength.")
