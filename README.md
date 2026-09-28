# 📋 Structured Information Extraction System

An AI-powered information extraction application that converts unstructured text into structured JSON using **Gemini 3.6 Flash**, **LangChain**, and **Streamlit**.

## 🚀 Project Overview

Real-world information is often available as unstructured text.

For example:

> John Smith applied for a personal loan of ₹5,00,000. His monthly income is ₹75,000 and his employment type is salaried.

This application uses a Large Language Model to identify important information and convert it into structured JSON.

### Example Output

```json
{
    "name": "John Smith",
    "loan_type": "Personal Loan",
    "loan_amount": 500000,
    "monthly_income": 75000,
    "employment_type": "Salaried"
}