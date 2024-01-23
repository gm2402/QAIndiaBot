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

# Add some styling using HTML and CSS
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding: 50px;
        }

        .container {
            max-width: 600px;
            margin: auto;
            background-color: #fff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: #333;
            margin-bottom: 20px;
        }

        input[type="text"] {
            width: 80%;
            padding: 10px;
            margin: 10px 0;
            box-sizing: border-box;
        }

        button {
            background-color: #4caf50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }

        .answer-container {
            margin-top: 30px;
            text-align: left;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display default question and answer
st.write("<div class='container'>", unsafe_allow_html=True)
st.write("<h1>Ask Me Anything!</h1>", unsafe_allow_html=True)

# Allow users to input a question
user_question = st.text_input("Your Question:")

# Respond to user's question
if st.button("Get Answer"):
    user_answer = df2.chat(user_question)
    st.write("<div class='answer-container'>", unsafe_allow_html=True)
    st.write(f"<p><strong>Your Question:</strong> {user_question}</p>", unsafe_allow_html=True)
    st.write(f"<p><strong>Answer:</strong> {user_answer}</p>", unsafe_allow_html=True)
    st.write("</div>", unsafe_allow_html=True)

st.write("</div>", unsafe_allow_html=True)