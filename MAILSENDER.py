from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import os

# Load .env for keys
load_dotenv()
sendgrid_api_key = os.getenv("SENDGRID_API_KEY")
sender_email = os.getenv("SENDER_EMAIL")

# Set up LLM
model = OllamaLLM(model="llama3")

# Define prompt
prompt_template = ChatPromptTemplate.from_template("""
You are an AI that writes birthday wishes.

Write a {tone} birthday message for a friend named {name}.
Keep it friendly and creative.
""")

# Combine prompt with model
chain = prompt_template | model

# Collect input
receiver_email = input("Enter recipient email: ")
name = input("Enter recipient's name: ")
tone = input("What kind of tone? (funny, sweet, formal, etc): ")

# Generate message using LangChain pipeline
while True:
    message_content = chain.invoke({"name": name, "tone": tone})
    print("Content:", message_content)
    confirm = input("Is this message okay? (yes/no): ").strip().lower()
    if confirm == "yes" or confirm == "y":
        break
button = input("Do you want to send this message? (yes/no): ").strip().lower()
if button == "yes" or button == "y":
# Prepare and send email
    sg = SendGridAPIClient(api_key=sendgrid_api_key)
    email = Mail(
        from_email=sender_email,
        to_emails=receiver_email,
        subject=f"Happy Birthday, {name}!",
        plain_text_content=message_content
    )
    response = sg.send(email)

print("✅ Email sent! Status:", response.status_code)
