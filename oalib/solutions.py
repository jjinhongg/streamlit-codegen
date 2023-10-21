"""Library with OpenAI API solutions as functions

References:

For building code:  https://beta.openai.com/docs/guides/code/introduction

"""

import openai
import os

# OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]
import openai
from oalib import solutions
import os

# OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

def generate_code(prompt):

    """
    Generates code using OpenAI's GPT-3 engine.

    Args:
        prompt (str): The prompt to generate code for.

    Returns:
        str: The generated code.
    """
    
    # Set up the OpenAI GPT-3 engine
    model_engine = "text-davinci-002"
    prompt = f"Generate code to {prompt}"
    max_tokens = 1024
    temperature = 0.5

    # Generate code using OpenAI's GPT-3
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
    )

    # Return the generated code
    return response.choices[0].text
