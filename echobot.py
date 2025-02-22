import sys
import json
from commands import execute_command
from llm_handler import chatbot_response
from config import MAX_HISTORY

# Chat history to maintain context
chat_history = []

def main():
    print("🔹 TermiBot: AI-Powered Terminal Assistant 🔹")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("💻 You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        
        command_result = execute_command(user_input)
        if command_result:
            print("🛠️ Terminal Output:\n" + command_result)
            continue
        
        
        chat_history.append(f"User: {user_input}")
        if len(chat_history) > MAX_HISTORY:
            chat_history.pop(0)  
       
        ai_response = chatbot_response(user_input, chat_history)
        print("🤖 TermiBot:", ai_response)
        
        
        chat_history.append(f"AI: {ai_response}")

if __name__ == "__main__":
    main()
