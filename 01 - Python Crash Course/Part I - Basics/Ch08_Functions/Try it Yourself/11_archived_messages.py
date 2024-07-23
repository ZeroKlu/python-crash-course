# Assignment 8.11
# Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of
#                    the list of messages. After calling the function, print both of your lists to show that the
#                    original list has retained its messages.

print("Try-it-Yourself:")
print("Assignment 8.11")

def send_messages(messages, sent_messages):
    """Move messages to sent_messages list"""
    while messages:
        message = messages.pop(0)
        print(f"Sending message: {message}")
        sent_messages.append(message)

messages = ["Hi there!", "Having fun at code camp!", "Python is great!"]
sent_messages = []
send_messages(messages[:], sent_messages)
print("Messages:\n", messages)
print("Sent Messages:\n", sent_messages)
