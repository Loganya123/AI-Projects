

#  AI-Projects

🤖 AI Chatbot — Multi-Model Streaming Chat App
A conversational AI web application built with Streamlit that lets users chat with multiple LLM providers in real time, with streaming responses, persistent chat history, live analytics, and a downloadable transcript — all in a single, lightweight Python app.

📌 Overview

This project is an end-to-end AI chatbot interface that demonstrates practical skills in LLM API integration, real-time streaming UX, and stateful web app design. Users can select from multiple language model providers via OpenRouter, watch responses stream token-by-token, and track conversation stats — all without writing a single line of frontend JavaScript, thanks to Streamlit.

The project was built as part of a hands-on portfolio to demonstrate applied ML/AI engineering skills for real-world chat-based applications.

✨ Features

💬 Real-Time Streaming Responses — Assistant replies are streamed token-by-token using Python generators and st.write_stream() for a natural, ChatGPT-like typing experience.

🔀 Multi-Model Selection — Users can switch between multiple LLMs at runtime via a sidebar dropdown:
Cohere (north-mini-code)
  NVIDIA (nemotron-3-ultra)
  Poolside (laguna-xs-2.1)
  Offline "Echo Bot" fallback (no API key required)

🌡️ Adjustable Temperature Control — Sidebar slider to configure response randomness/creativity.

🕒 Message Timestamps — Every message (user and assistant) is timestamped in 12-hour format.

📊 Live Chat Analytics — Real-time metrics for user messages, assistant messages, and total conversation length.

📥 Exportable Chat History — One-click download of the full conversation as a .txt transcript.

🧹 Clear Chat / Session Reset — Instantly reset the conversation back to a fresh state.

🔐 Secure API Key Management — API credentials loaded via environment variables (python-dotenv), never hardcoded.

🛠️ Tech Stack

Category:	Technology

Frontend / UI:	Streamlit

Language:	Python 3.10+
LLM Access:	OpenAI SDK routed through OpenRouter API
Models:	Cohere, NVIDIA Nemotron, Poolside
State Management:	Streamlit session_state
Environment Config:	python-dotenv

🏗️ How It Works

Session State persists the full chat history, so the conversation survives every Streamlit rerun (Streamlit re-executes the whole script on each user interaction).

Model Router (generate_response()) is a Python generator function that dynamically calls the selected LLM's streaming endpoint via the OpenAI-compatible OpenRouter client, or falls back to a local echo response.

Streaming UI uses st.write_stream() to render each token as it arrives, then persists the completed message back into session state.

Sidebar Controls let the user configure the model and temperature without reloading the page.

Analytics Panel recalculates message counts live from session state on every rerun.

🚀 Getting Started

Prerequisites
  Python 3.10+
  An OpenRouter API key (free tier supports the models used here)

Installation
# Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# Install dependencies
pip install streamlit openai python-dotenv

# Run the app
streamlit run chatbotcreation.py

The app will open automatically at http://localhost:8501.

📂 Project Structure

├── chatbotcreation.py     # Main Streamlit application
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

🎯 What I Learned

Building interactive, stateful web apps with Streamlit's rerun-based execution model

Integrating and abstracting multiple LLM providers behind a single unified interface using OpenRouter

Implementing real-time token streaming using Python generators

Managing application state safely across UI reruns with st.session_state

Secure API key handling using environment variables

📄 License

This project is open source and available under the MIT License.
