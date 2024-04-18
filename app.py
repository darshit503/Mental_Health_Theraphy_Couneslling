import streamlit as st
import requests
import json

st.set_page_config(page_title="Generate Therapy Answers🤖",
            page_icon='🤖',
            layout='centered',
            initial_sidebar_state='collapsed')


url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

def generate_response(prompt):
    data = {
        "model": "openorca_FT_medical",
        "stream": False,
        "prompt": prompt,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None


def generate_text():
    # prompt = f"Please generate a draft for a legal notice in detail. The notice is to be sent on behalf of {client_name}, located at {client_address}, to {recipient_name} regarding {reason_for_notice}. The notice should include a clear statement of the issue, a request for resolution or action, a deadline for response or action, and any legal consequences of non-compliance. Please use formal language and ensure the notice is legally sound.\n\nCrime Type: include any IPC that applies to this perticular case"
    prompt = f"PRovide Response on the below text \n\n{input_text}"


    data = {
        "model": "openorca_FT_medical",
        "stream": False,
        "prompt": prompt,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        return actual_response
    else:
        st.error(f"Error: {response.status_code}, {response.text}")


st.header("Mental Health Counselling 🤖")
input_text=st.text_area("Enter your Problem/Emotions")

if st.button("Generate Response"):
    generated_notice = generate_text()
    st.text_area("Generated Legal Notice", generated_notice)

