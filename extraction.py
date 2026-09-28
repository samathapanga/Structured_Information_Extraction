import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0,
    google_api_key=gemini_api_key
)


def extract_information(text):

    prompt = f"""
You are an information extraction system.

Extract the following information from the given text:

- name
- loan_type
- loan_amount
- monthly_income
- employment_type

Rules:
1. Return ONLY valid JSON.
2. Do not use Markdown.
3. Do not use ```json or ``` code fences.
4. loan_amount must be a number without currency symbols or commas.
5. monthly_income must be a number without currency symbols or commas.
6. If information is not available, use null.

Expected format:

{{
    "name": "John Smith",
    "loan_type": "Personal Loan",
    "loan_amount": 500000,
    "monthly_income": 75000,
    "employment_type": "Salaried"
}}

Text:
{text}
"""

    response = llm.invoke(prompt)

    response_text = response.content

    # Handle Gemini responses that may contain multiple content blocks
    if isinstance(response_text, list):
        response_text = "".join(
            item.get("text", "")
            for item in response_text
            if isinstance(item, dict)
        )

    # Remove Markdown code fences if Gemini adds them
    response_text = response_text.replace("```json", "").replace("```", "").strip()

    # Convert the response into actual Python JSON data
    try:
        extracted_data = json.loads(response_text)
        return extracted_data

    except json.JSONDecodeError:
        return {
            "error": "Could not convert Gemini response into valid JSON.",
            "raw_response": response_text
        }