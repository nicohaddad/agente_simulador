import openai

class Agent:
    def __init__(self, name: str, system_prompt: str, model: str = "gpt-4", temperature: float = 0.7):
        self.name = name
        self.model = model
        self.temperature = temperature
        self.messages = [{"role": "system", "content": system_prompt}]

    def add_user_message(self, message: str):
        self.messages.append({"role": "user", "content": message})

    def add_assistant_message(self, message: str):
        self.messages.append({"role": "assistant", "content": message})

    def chat(self) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            temperature=self.temperature,
            messages=self.messages,
        )
        content = response.choices[0].message.content
        # Keep conversation short by trimming history
        if len(self.messages) > 20:
            self.messages = self.messages[-10:]
        self.add_assistant_message(content)
        return content