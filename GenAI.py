import streamlit as st
import openai

# Initialize OpenAI API client
openai.api_key = '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'

# Streamlit UI
def main():
    st.title('GenAI App - AI Code Reviewer')
    st.write('Submit your Python code for review')

    code_input = st.text_area('Enter your Python code here:', height=300)

    if st.button('Submit'):
        if code_input.strip() == '':
            st.error('Please enter some Python code.')
        else:
            # Call function to analyze code
            analyze_code(code_input)

# Function to analyze code using OpenAI API
def analyze_code(code):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=code,
            max_tokens=100,
            n=1,
            stop=['\n']
        )

        # Extract feedback and fixed code from API response
        feedback = response['choices'][0]['text']
        fixed_code = extract_fixed_code(feedback)

        # Display results
        st.subheader('Feedback:')
        st.write(feedback)
        st.subheader('Fixed Code:')
        st.code(fixed_code, language='python')

    except Exception as e:
        st.error(f'An error occurred: {str(e)}')

# Function to extract fixed code from feedback
def extract_fixed_code(feedback):
    # Implement logic to extract fixed code from feedback
    # You may need to customize this based on the structure of feedback provided by OpenAI
    fixed_code = feedback  # Placeholder logic
    return fixed_code

if __name__ == "__main__":
    main()
