from django.shortcuts import render
from django.http import HttpResponse
from pandasai import SmartDataframe
from pandasai.llm.google_palm import GooglePalm

# Initialize GooglePalm
llm = GooglePalm(api_key="AIzaSyCw3CjCkF4nySicqwkuxob31V65nNlzBwI")

# Load SmartDataframe with the initialized llm
df2 = SmartDataframe(r'C:\Users\kj\Desktop\GTM\qa_project\qa_app\webpage_data.xlsx', config={"llm": llm})

# Set a default question
default_question = "What is the capital of India"

# Get the initial answer for the default question
default_answer = df2.chat(default_question)

def index(request):
    context = {
        'question': default_question,
        'answer': default_answer,
    }
    return render(request, 'index.html', context)

def ask_question(request):
    if request.method == 'POST':
        user_question = request.POST.get('question')
        user_answer = df2.chat(user_question)
        context = {
            'question': user_question,
            'answer': user_answer,
        }
    return render(request, 'index.html', context)
    # return HttpResponse("Invalid Request")
