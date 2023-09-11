import random
Here is the optimized version of the Python script:

```python


class SalesAssistant:
    def __init__(self):
        self.customer_profile = {}
        self.sales_funnel = {}
        self.possible_responses = [
            "I understand. Let me check our inventory for you.",
            "That's a great choice! Let me provide more details.",
            "I recommend checking out our special offers section.",
            "Would you like me to add this item to your cart?"
        ]

    def run(self):
        print("Welcome to the AI-Driven Sales Assistant!")
        while True:
            user_input = input("How can I assist you today? ")
            if user_input.lower() in ['bye', 'goodbye']:
                print("Thank you for using the AI-Driven Sales Assistant. Goodbye!")
                break
            else:
                print(self.generate_response(user_input))

    def generate_response(self, user_input):
        return random.choice(self.possible_responses)

    def update_customer_profile(self, customer_id, customer_data):
        self.customer_profile[customer_id] = customer_data

    def update_sales_funnel(self, customer_id, sales_data):
        self.sales_funnel[customer_id] = sales_data


if __name__ == '__main__':
    assistant = SalesAssistant()
    assistant.run()
```
You can copy and paste this optimized version of the script into your codebase.
