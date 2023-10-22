import streamlit as st
from oalib.solutions import unit_tests_from_function

def app():
    # Set the app title
    st.title("Python Unit Test Generator")

    # Introduction and guidance
    st.write("Welcome to the Python Unit Test Generator!")
    st.write("Input a Python function below, and this tool will generate unit tests for you.")

    # Text area for users to input a Python function
    function_input = st.text_area("Paste your Python function here:")

    # Button to trigger the generation of the unit test
    if st.button("Generate Unit Test"):
        if function_input:
            try:
                # Use the 'unit_tests_from_function' function to generate the unit test
                unit_test = unit_tests_from_function(function_input)
                st.code(unit_test, language='python')
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please input a Python function to generate its unit test.")

# Run the app
if __name__ == "__main__":
    app()
