# from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import datetime
# from typing import Text, List, Dict, Any

# class GenerateGPT2Response(Action):
#     def name(self) -> Text:
#         return "action_generate_gpt2_response"
    
#     def __init__(self):
#         super().__init__()
#         # Initializing GPT-2 tokenizer and model
#         self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
#         self.model = TFGPT2LMHeadModel.from_pretrained("gpt2")
        
#         # Open log file in append mode
#         self.log_file = open("conversation_logs.txt", "a")

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Get user input
#         user_input = tracker.latest_message.get("text")

#         # Generate response using GPT-2
#         response = self.generate_response(user_input)
        
#         # Log conversation
#         self.log_conversation(user_input, response)

#         # Send response back to user
#         dispatcher.utter_message(text=response)

#         return []

#     def generate_response(self, user_input: str) -> str:
#         # Tokenize user input
#         inputs = self.tokenizer.encode(user_input, return_tensors="pt")

#         # Generate response using GPT-2
#         outputs = self.model.generate(inputs, max_length=100, num_return_sequences=1)
#         response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

#         return response
    
#     def log_conversation(self, user_input: str, response: str) -> None:
#         # Get current date and time
#         current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
#         # Write user input and response to log file
#         self.log_file.write(f"{current_time} - User: {user_input}\n")
#         self.log_file.write(f"{current_time} - GPT-2: {response}\n")
#         self.log_file.write("\n")
