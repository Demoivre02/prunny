from typing import List, Dict

class SimpleOpenAI:
    def __init__(self):
        pass
    
    def generate(self, prompt: str) -> str:
        return f"This is a simulated response to: {prompt}"

class LangChain:
    def __init__(self, llm):
        self.llm = llm
    
    def run(self, user_input: str) -> str:
        
        prompt = f"User question: {user_input}\nPlease provide a helpful response:"
        return self.llm.generate(prompt)


llm = SimpleOpenAI()
chain = LangChain(llm)


user_question = "What is the capital of France?"
response = chain.run(user_question)
print(f"User: {user_question}")
print(f"AI: {response}")