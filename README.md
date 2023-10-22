# streamlit-codegen
A unit-test code generator web app using Streamlit

# Unit test writing using a multi-step prompt

Complex tasks, such as writing unit tests, can benefit from multi-step prompts. In contrast to a single prompt, a multi-step prompt generates text from GPT and then feeds that output text back into subsequent prompts. This can help in cases where you want GPT to reason things out before answering, or brainstorm a plan before executing it.

In this repo, we use a 3-step prompt to write unit tests in Python using the following steps:

1. **Explain**: Given a Python function, we ask GPT to explain what the function is doing and why.
2. **Plan**: We ask GPT to plan a set of unit tests for the function.
    - If the plan is too short, we ask GPT to elaborate with more ideas for unit tests.
3. **Execute**: Finally, we instruct GPT to write unit tests that cover the planned cases.

The code example illustrates a few embellishments on the chained, multi-step prompt:
    - Conditional branching (e.g., asking for elaboration only if the first plan is too short)
    - The choice of different models for different steps
    - A check that re-runs the function if the output is unsatisfactory (e.g., if the output code cannot be parsed by Python's `ast` module)
    - Streaming output so that you can start reading the output before it's fully generated (handy for long, multi-step outputs)
