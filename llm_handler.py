import llama_cpp
from config import MODEL_PATH


llm = llama_cpp.Llama(model_path=MODEL_PATH)

def chatbot_response(prompt, history):
    """
    Generates AI response using an open-source LLM with context.
    """
    
    full_prompt = "\n".join(history) + f"\nUser: {prompt}\nAI:"

    response = llm(
        prompt=full_prompt,
        max_tokens=200,
        stop=["\n", "User:", "AI:"]
    )

    return response["choices"][0]["text"].strip()
