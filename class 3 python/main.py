import streamlit as st
from zxcvbn import zxcvbn

def password_strength_meter(password):
    """Returns the strength of a password and a score to indicate its strength."""
    result = zxcvbn(password)
    score = result['score']  # Score between 0 and 4
    feedback = result['feedback']['suggestions']
    
    return score, feedback

def strength_label(score):
    """Returns a label based on the password score."""
    if score == 0:
        return "Very Weak", "red"
    elif score == 1:
        return "Weak", "orange"
    elif score == 2:
        return "Fair", "yellow"
    elif score == 3:
        return "Strong", "lightgreen"
    else:
        return "Very Strong", "green"

# Streamlit user interface
st.title("Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = password_strength_meter(password)
    strength, color = strength_label(score)
    
    st.markdown(f"**Password Strength: {strength}**", unsafe_allow_html=True)
    st.markdown(f"<span style='color: {color};'>{'⬤' * (score + 1)}</span>", unsafe_allow_html=True)  # Visualization

    # If available, show suggestions to improve password
    if feedback:
        st.markdown("### Suggestions to Improve:")
        for suggestion in feedback:
            st.markdown(f"- {suggestion}")
else:
    st.markdown("Please enter a password to evaluate its strength.")

st.sidebar.header("Password Guidelines")
st.sidebar.markdown("""
- **Length:** At least 12 characters
- **Complexity:** Include numbers, uppercase letters, lowercase letters, and symbols
- **Avoid:** Common words and phrases
""")
