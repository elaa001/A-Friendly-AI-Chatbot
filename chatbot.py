import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory



# Set page config
st.set_page_config(page_title="Elaa's Chatbot", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #ffeef5;
    }
    
    html, body {
    background-color: #ffeef5;
    }

    .main {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 750px;
        margin: auto;
    }

    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 1px solid #ffb6c1;
        padding: 10px;
        background-color: #fff;
    }

    .stChatMessage {
        border-radius: 12px;
        padding: 8px 12px;
        margin-bottom: 8px;
        line-height: 1.4em;
    }

    .stChatMessage p {
        margin-bottom: 0 !important;
    }

    .stButton button {
        background-color: #fff5f8;
        color: #d6336c;
        border: 2px solid #ffb6c1;
        border-radius: 8px;
        padding: 0.5em 1.2em;
        font-weight: 600;
    }

    .stButton button:hover {
        background-color: #ffe4ec;
        color: #c2185b;
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }
    
    
    [data-testid="stChatInput"] > div {
        background-color: #ffeef5 ;
        border: 2px solid #ffb6c1 ;
        border-radius: 30px;
        padding: 6px 14px ;
    }

    
    [data-testid="stChatInput"] textarea {
        background-color: #fff0f5 ;
        color: #333 ;
        font-size: 16px ;
    }

    
    [data-testid="stChatInput"] textarea:focus {
        border-color: #ff80ab ;
        box-shadow: 0 0 4px #ffc0cb ;
    }

    
    </style>
    """, unsafe_allow_html=True)



# App title
st.title("Elaa's AI Chatbot")
st.write("Chat with me just like you're chatting with a friend! 💬🌸")


# Input OpenAI API key
openai_api_key = st.secrets["OPENAI_API_KEY"]

if st.button("🧹 Reset Chat"):
    st.session_state.memory = ConversationBufferMemory()
    st.rerun()


# Initialize memory
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

# Create chatbot model when key is provided
if openai_api_key:
    llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key, model_name="gpt-3.5-turbo")
    conversation = ConversationChain(
        llm=llm,
        memory=st.session_state.memory,
        verbose=False
    )
    
    conversation = ConversationChain(
        llm=llm,
        memory=st.session_state.memory,
        verbose=False
    )
    
    # Display chat history
    for msg in st.session_state.memory.chat_memory.messages:
        if msg.type == "human":
            st.chat_message("user").markdown(msg.content)
        else:
            # Custom assistant layout
            clean_response = msg.content.replace("\n", " ").replace("\n\n", " ").strip()
            st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 12px; background-color: #fff3f8;
                        padding: 10px 14px; border-radius: 12px; margin: 10px 0; max-width: 90%;">
                <span style="font-size: 22px;">🤖</span>
                <span style="font-size: 16px; color: #333;">{clean_response}</span>
            </div>
            """, unsafe_allow_html=True)
    # Chat input
    user_input = st.chat_input("Ask me anything...")
    if user_input:
        with st.spinner("Thinking..."):
            response = conversation.run(user_input)
            st.chat_message("user").markdown(user_input)
            # Clean the message to remove extra newlines
            clean_response = response.replace("\n", " ").strip()

            # Show a horizontal layout: emoji + message inline
            st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 10px; background-color: #fef0f5;
                        padding: 10px 15px; border-radius: 12px; max-width: 90%; margin: 8px 0;">
                <div style="font-size: 24px;">🤖</div>
                <div style="font-size: 16px; color: #333;">{clean_response}</div>
            </div>
            """, unsafe_allow_html=True)

            
else:
    st.error("Missing OpenAI API key. Please add it to your `.env` file as `OPENAI_API_KEY`.")
