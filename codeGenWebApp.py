import streamlit as st
from oalib.solutions import generate_code

# Define a dictionary of code templates for each language
code_templates = {
    "Python": "print('{}')",
    "JavaScript": "console.log('{}');",
    "Java": "System.out.println('{}');",
    "C++": 'cout << "{}" << endl;',
}

# Define the Streamlit app
def app():
    # Set the app title
    st.title("Code Generator")

    # Define the input and language selection widgets
    input_text = st.text_input("Enter input:")
    language = st.selectbox("Select language:", list(code_templates.keys()))

    # Generate the code based on the user input and selected language
    if input_text:
        code = generate_code(input_text, language)
        st.code(code, language=language.lower())

# Run the app
if __name__ == "__main__":
    app()
