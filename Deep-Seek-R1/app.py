# Import necessary libraries
import streamlit as st
from langchain_community.chat_models.ollama import ChatOllama  # Corrected import
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# =============================================================================
# Streamlit UI Configuration
# =============================================================================
# Custom CSS styling for dark theme
st.markdown("""
<style>
    .main {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #2d2d2d;
    }
    .stTextInput textarea {
        color: #ffffff !important;
    }
    .stSelectbox div[data-baseweb="select"] {
        color: white !important;
        background-color: #3d3d3d !important;
    }
    .stSelectbox svg {
        fill: white !important;
    }
    .stSelectbox option {
        background-color: #2d2d2d !important;
        color: white !important;
    }
    div[role="listbox"] div {
        background-color: #2d2d2d !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# App title and caption
st.title("🧠 DeepSeek Code Buddy")
st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers Made by Shees Ikram")

# =============================================================================
# Sidebar Configuration
# =============================================================================
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Model selection dropdown
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:1.5b", "deepseek-r1:3b"],  # Must match Ollama model names
        index=0
    )
    
    st.divider()
    st.markdown("### Model Capabilities")
    st.markdown("""
    - 🐍 Python Expert
    - 🐞 Debugging Assistant
    - 📝 Code Documentation
    - 💡 Solution Design
    """)
    st.divider()
    st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/) by Shees Ikram")

# =============================================================================
# AI Engine Initialization
# =============================================================================
llm_engine = ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",  # Local Ollama server
    temperature=0.3  # Controls randomness (0 = deterministic, 1 = creative)
)

# System prompt template for consistent AI behavior
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions "
    "with strategic print statements for debugging. Always respond in English."
)

# =============================================================================
# Session State Management
# =============================================================================
if "message_log" not in st.session_state:
    st.session_state.message_log = [{
        "role": "ai", 
        "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"
    }]

# =============================================================================
# Chat Interface
# =============================================================================
# Container for chat history display
chat_container = st.container()

# Display existing chat messages
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# =============================================================================
# Chat Processing Logic
# =============================================================================
def build_prompt_chain():
    """Constructs the conversation history for context-aware responses"""
    prompt_sequence = [system_prompt]
    
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
            
    return ChatPromptTemplate.from_messages(prompt_sequence)

def generate_ai_response(prompt_chain):
    """Executes the processing pipeline"""
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

# Handle user input
user_query = st.chat_input("Type your coding question here...")

if user_query:
    # Add user message to history
    st.session_state.message_log.append({"role": "user", "content": user_query})
    
    # Generate and display AI response
    with st.spinner("🧠 Processing..."):
        try:
            prompt_chain = build_prompt_chain()
            ai_response = generate_ai_response(prompt_chain)
            st.session_state.message_log.append({"role": "ai", "content": ai_response})
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
    
    # Refresh the interface
    st.rerun()