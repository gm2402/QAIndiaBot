from flask import Flask, render_template, request
from pandasai import SmartDataframe
from pandasai.llm.google_palm import GooglePalm

app = Flask(__name__)

# Initialize GooglePalm
llm = GooglePalm(api_key="AIzaSyCw3CjCkF4nySicqwkuxob31V65nNlzBwI")

# Load SmartDataframe with the initialized llm
df2 = SmartDataframe('webpage_data.xlsx', config={"llm": llm})

# Set a default question
default_question = "What is the capital of India"

# Get the initial answer for the default question
default_answer = df2.chat(default_question)

@app.route('/')
def index():
    return render_template('index.html', question=default_question, answer=default_answer)

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.form['question']
    user_answer = df2.chat(user_question)
    return render_template('index.html', question=user_question, answer=user_answer)

if __name__ == '__main__':
    app.run(debug=True)
