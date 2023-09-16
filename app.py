import streamlit as st
from detoxify import Detoxify

# Set Streamlit app title
st.title("Clean Chat Control")

# Create a text input box for user input
input_text = st.text_area('Enter a sentence')

# Check if there is input text
if input_text:
    # Add a button to trigger moderation
    if st.button("Moderate"):
        # Perform toxicity prediction
        with st.spinner("Analyzing..."):
            results = Detoxify('original').predict(input_text)

        # Display the results in columns
        st.header("Moderation Results:")
        st.write("Toxicity: {:.2f}".format(results['toxicity']))
        st.write("Severe Toxicity: {:.2f}".format(results['severe_toxicity']))
        st.write("Obscene: {:.2f}".format(results['obscene']))
        st.write("Threat: {:.2f}".format(results['threat']))
        st.write("Insult: {:.2f}".format(results['insult']))
        st.write("Identity Attack: {:.2f}".format(results['identity_attack']))

# Add a brief description of the app
st.markdown("""
This simple app helps you analyze the content of a sentence for toxicity, threats, and insults. 
Enter a sentence in the text box above and click the "Moderate" button to see the results.
""")

st.markdown("""
---
Created with ❤️ by Joas
""")
