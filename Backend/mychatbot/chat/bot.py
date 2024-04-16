import nltk
nltk.download('punkt')
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello", ["Hello!", "Hi there!"]],
    [r"how are you?", ["I'm good, how are you?"]],
    [r"quit", ["Bye, have a good day!"]],
    [r"are you give hosting|are you give deploy", ["Yes"]],
    [r"kreatech|what is kreatech|know kreatech\?*|kreatech\?", ["I know about Kreatech. It is a leading software company"]],
    [r"কে আপনি ? | আপনি কে ? ", ["আমি মানুষ "]]
]

chatbot = Chat(pairs, reflections)

def chat(user_input):
    return chatbot.respond(user_input)
