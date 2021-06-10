import streamlit as st
from transformers import pipeline, Conversation

conversational_pipeline = pipeline('conversational')

conv = Conversation()
st.title("Huggingface Q&A pipeline")
def get_text():
    input_text = st.text_input('type here')
    return input_text

def ask(user_input):
    conv.add_user_input(user_input)
    conversational_pipeline([conv])
    # if conv.generated_responses != []:
    #     output = conv.generated_responses[-1]
    # else:
    #     output = ""
    output = conv.generated_responses[-1]
    return output
conv.add_user_input("Let's start the conversation")
conversational_pipeline([conv])
ans = conv.generated_responses[-1]
st.write(ans)

user_input = get_text()

answer = ask(user_input)
st.write(answer)

