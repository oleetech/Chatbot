import nltk
nltk.download('punkt')
from nltk.chat.util import Chat, reflections
from .models import QA_Pair  

def load_pairs():
    db_pairs = [
        [fr"{pair.question}", [pair.answer]]
        for pair in QA_Pair.objects.all()
    ]
    static_pairs = [
        [r"hi|hello", ["Hello!", "Hi there!"]],
        [r"who made you ?| your creator ? |who make you", ["I am developed by Olee Ahmmed (Backend Developer)"]],
        [r"how are you?", ["I'm good, how are you?"]],
        [r"quit", ["Bye, have a good day!"]],
        [r"are you give hosting|are you give deploy", ["Yes"]],
        [r"kreatech|what is kreatech|know kreatech\?*|kreatech\?", ["I know about Kreatech. It is a leading software company"]],
        [r"কে আপনি ? | আপনি কে ?", ["আমি মানুষ "]]
    ]
    return static_pairs + db_pairs

pairs = load_pairs()
chatbot = Chat(pairs, reflections)

def chat(user_input):
    return chatbot.respond(user_input)
