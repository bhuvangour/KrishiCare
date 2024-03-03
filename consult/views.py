# views.py
from django.shortcuts import render
from .models import Message

def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        response, _ = predict(user_message)
        message = Message(user_message=user_message, bot_message=response)
        message.save()

    messages = Message.objects.all().order_by('created_at')
    context = {'messages': messages}
    return render(request, 'chatbot.html', context)

# utils.py
import pickle
import joblib
import numpy as np

# Replace 'model_path.sav' with the actual path to your saved ML model
# model = joblib.load('model_path.sav')

# def predict(text):
#    input_text = np.array([text])
#    prediction = model.predict(input_text)
#    return prediction[0], None