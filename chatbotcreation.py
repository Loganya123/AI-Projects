import streamlit as st
from datetime import datetime
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Assistant
# 2. User
# 3. Chat History

# Add-on Features
# 1. Sidebar
# 2. Clear Chat
# 3. Timestamps
# 4. Selection of Models
# 5. Temperature
# 6. Chat Statistics


st.set_page_config(
    page_title = "Chatbot",
    page_icon = ""
)
    

st.title("Chatbot with AI")
st.caption("Powered with Streamlit")

#-----------------Side Bar---------------------------
with st.sidebar:
    st.header("Settings")

    #SelectBox to Select the LLM's
    model = st.selectbox("Choose Model",
                         [
                             "Echo Bot", "Cohere", "Nvidia", "Poolside"
                         ]
                         )

    # Model Temperature
    temperature = st.slider(
        "Temperature", min_value = 0.0, max_value = 1.0, value = 0.7
        )

    st.divider()

    # Clearing Chat History
    if st.button("Clear Chat"):
        st.session_state.messages = [
            {
                "role" : "assistant",
                "content" : "Hey, How can I help you?",
                "time" : datetime.now().strftime("%I: %M %p")
            }
        ]

        st.rerun()
    st.divider()

#------------------Chat Statistics--------------------------
if "messages" in st.session_state:
    user_count = sum(
        1 for msg in st.session_state.messages
        if msg["role"] == "user"
    )

    assistant_count = sum(
        1 for msg in st.session_state.messages
        if msg["role"] == "assistant"
    )

    st.metric("User Messages", user_count)
    st.metric("Assistant Messages", assistant_count)
    st.metric("Total Messages", len(st.session_state.messages))

    # Current Time
    st.info(f"{datetime.now().strftime('%I : %M %p')}")

    #Download Chat
    chat_history = ""

    for msg in st.session_state.messages:
        chat_history += (
            f"{msg["role"].title()}"
            f"({msg["time"]}) \n"
            f"{msg["content"]}\n\n"
        )

    st.download_button(
        "Download Chat",
        chat_history,
        file_name = "chat_history.txt"
    )

#---------------Chat History------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role" : "assistant",
            "content" : "Hey, How can I help you?",
            "time" : datetime.now().strftime("%I: %M %p") #%I - 12 hour format, %M - minutes, %p - AM/PM
            }
    ]


# Open AI
API_KEY = os.getenv("API_KEY")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key = API_KEY
)

# Function to Generate Response
def generate_response(user_message):
    if model == "Cohere":
        stream = client.chat.completions.create(
            model = "cohere/north-mini-code:free",
            messages = [
                {
                    "role" : "user",
                    "content" : user_message
                    }
                ],
                stream = True
            )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    elif model == "Nvidia":
        stream = client.chat.completions.create(
            model = "nvidia/nemotron-3-ultra-550b-a55b:free",
            messages = [
                {
                    "role" : "user",
                    "content" : user_message
                    }
                ],
                stream = True
            )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    elif model == "Poolside":
            stream = client.chat.completions.create(
                model = "poolside/laguna-xs-2.1:free",
                messages = [
                    {
                        "role" : "user",
                        "content" : user_message
                        }
                    ],
                    stream = True
                )
    
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content

    


    else:
        response = f"You said: {user_message}"
        for word in response.split():
            yield word + " "

st.divider()

#--------------------Displaying the previous messages-----------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])
        st.caption(message["time"])

#--------------------------User Input----------------------
user_message = st.chat_input("Type the message here....")

if user_message:

    current_time = datetime.now().strftime("%I: %M %p")

    # Displaying the user message
    with st.chat_message("user"):
        st.write(user_message)
        st.caption(current_time)

    # Storing user message
    st.session_state["messages"].append(
        {
            "role":"user",
            "content":user_message,
            "time":current_time
         }
        )

    # Using Generate_response() function
    
    assistant_time = datetime.now().strftime("%I:%M %p")

#---------------------Assistant reponse------------------

    with st.chat_message("assistant"):
        # Streaming the response
            with st.spinner("Genertaing response...."):
                    bot_response = st.write_stream(
                        generate_response(user_message)
                    )
            st.caption(assistant_time)

    # Save the complete response

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":bot_response,
            "time":assistant_time
        }
    )

    st.caption(datetime.now().strftime("%I: %M %p"))

    # st.session_state["messages"].append(
    #             {
    #                 "role":"assistant",
    #                 "content":bot_response,
    #                 "time":datetime.now().strftime("%I: %M %p")
    #             }
    #             )

