# Short Chatbot with Exception Handling

qa_bot = {
    "hi": "Hello!",
    "what is your name?": "I am a Python chatbot.",
    "how are you?": "I'm doing great!",
    "what is python?": "A programming language.",
    "who made you?": "A programmer.",
    "what can you do?": "Answer basic questions.",
}


def run_chatbot():
  print("Chatbot: Hi! Type 'exit' to quit.")
  while True:
    try:
      user = input("\nYou: ").lower().strip()
      if user == "exit":
        print("Chatbot: Bye!")
        break
      if not user:
        raise ValueError("Input cannot be empty!")

      # Respond using dictionary or default message
      response = qa_bot.get(user, "I don't understand that.")
      print(f"Chatbot: {response}")

    except ValueError as e:
      print(f"Error: {e}")
    except Exception:
      print("An unexpected error occurred.")


run_chatbot()