import streamlit as st
from pandasai import SmartDataframe
from pandasai.llm.google_palm import GooglePalm

# Initialize GooglePalm
llm = GooglePalm(api_key="AIzaSyCw3CjCkF4nySicqwkuxob31V65nNlzBwI")

# Load SmartDataframe with the initialized llm
df2 = SmartDataframe('webpage_data.xlsx', config={"llm": llm})

# Set a default question
default_question = "What is the capital of India"

# Get the initial answer for the default question
default_answer = df2.chat(default_question)

# Streamlit app
st.title("Q&A Application of India")

# Display default question and answer
# st.write(f"Default Question: {default_question}")
# st.write(f"Default Answer: {default_answer}")

# Allow users to input a question
user_question = st.text_input("Ask a question:")

# Respond to user's question
if st.button("Get Answer"):
    user_answer = df2.chat(user_question)
    st.write(f"User's Question: {user_question}")
    st.write(f"Answer: {user_answer}")
