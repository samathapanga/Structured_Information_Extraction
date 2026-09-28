import streamlit as st
import json

from extraction import extract_information


st.set_page_config(
    page_title="Structured Information Extraction",
    page_icon="📋",
    layout="centered"
)


# -----------------------------
# Header
# -----------------------------

st.title("📋 Structured Information Extraction System")

st.write(
    "Convert unstructured text into structured JSON using "
    "Gemini 3.6 Flash."
)


# -----------------------------
# Example Inputs
# -----------------------------

st.subheader("🧪 Try an Example")

example_loan = (
    "John Smith applied for a personal loan of ₹5,00,000. "
    "His monthly income is ₹75,000 and his employment type is salaried."
)

example_home = (
    "Rahul Sharma applied for a home loan of ₹30,00,000. "
    "He works as a software engineer."
)


col1, col2 = st.columns(2)

with col1:
    if st.button("🏦 Personal Loan", use_container_width=True):
        st.session_state.example_text = example_loan

with col2:
    if st.button("🏠 Home Loan", use_container_width=True):
        st.session_state.example_text = example_home


# -----------------------------
# Text Input
# -----------------------------

default_text = st.session_state.get("example_text", "")

text = st.text_area(
    "📝 Enter unstructured text",
    value=default_text,
    height=180,
    placeholder=(
        "Example:\n"
        "John Smith applied for a personal loan of ₹5,00,000. "
        "His monthly income is ₹75,000 and his employment type is salaried."
    )
)


# -----------------------------
# Extract Button
# -----------------------------

if st.button(
    "🔍 Extract Information",
    use_container_width=True,
    type="primary"
):

    if not text.strip():

        st.warning("⚠️ Please enter some text first.")

    else:

        with st.spinner("🤖 Extracting information using Gemini..."):

            result = extract_information(text)

        st.subheader("📄 Extracted Information")

        if "error" in result:

            st.error(result["error"])

            st.write(result["raw_response"])

        else:

            # Display JSON
            st.json(result)

            # Download JSON
            json_data = json.dumps(
                result,
                indent=4,
                ensure_ascii=False
            )

            st.download_button(
                label="⬇️ Download JSON",
                data=json_data,
                file_name="extracted_information.json",
                mime="application/json",
                use_container_width=True
            )


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.header("🛠️ Technologies")

    st.write("• Python")
    st.write("• LangChain")
    st.write("• Gemini 3.6 Flash")
    st.write("• Streamlit")
    st.write("• JSON")

    st.divider()

    st.header("📌 Extracted Fields")

    st.write("• Name")
    st.write("• Loan Type")
    st.write("• Loan Amount")
    st.write("• Monthly Income")
    st.write("• Employment Type")

    st.divider()

    st.info(
        "This application converts unstructured text "
        "into structured information using an LLM."
    )