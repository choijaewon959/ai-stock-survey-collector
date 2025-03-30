from openai import OpenAI

class OpenAIAdvisor:
    def __init__(self, api_key):
        """
        Initialize the OpenAIAdvisor with the OpenAI API key.
        """
        self.client = OpenAI(api_key=api_key)
        self.model = 'gpt-4o-search-preview-2025-03-11'

    def send_message(self, conversation_history, max_token=150, temperature=1):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=conversation_history,
                max_tokens=max_token,
            )
            return {
                'role': 'assistant',
                'content': response.choices[0].message.content
            }
        except Exception as e:
            return f"An error occurred: {e}"

    def get_advice(self):
        """
        Get advice from OpenAI based on the user's input prompt.
        """
        q1 = "Should I buy Apple stock now?"
        q2 = "Considering current market situation, you would rather either strongly buy/buy/hold/sell/storngly sell Apple stock? Give me short answer, current market price, and target price."
        
        conversation_history = []
        for q in [q1, q2]:
            conversation_history.append({
                'role': 'user', 'content': q
            })
            res = self.send_message(conversation_history)
            conversation_history.append(res)

        return conversation_history

if __name__ == "__main__":
    api_key = input("Enter your OpenAI API key: ")
    advisor = OpenAIAdvisor(api_key)

    while True:
        user_input = input("Ask the AI Advisor (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        advice = advisor.get_advice(user_input)
        print(f"AI Advisor: {advice}")