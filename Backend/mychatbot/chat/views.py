from rest_framework.views import APIView
from rest_framework.response import Response
from .bot import chat
from .models import Message

class ChatView(APIView):
    def post(self, request):
        user_input = request.data.get('message')
        if not user_input:
            return Response({"message": "No input provided"}, status=400)

        # Process the input to generate a response
        bot_response = chat(user_input)
        
        # Check if the response exists
        if bot_response is None or bot_response == "I'm not sure how to answer that. Can you ask something else?":
            # Save the question to the database only if there is no valid answer
            Message.objects.create(text=user_input)
            bot_response = bot_response if bot_response else "I'm not sure how to answer that. Can you ask something else?"

        return Response({"message": bot_response})
