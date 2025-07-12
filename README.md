
# 🤖 ElaaChat – A Friendly AI Chatbot

Welcome to **ElaaChat**, a cozy, aesthetic, and intelligent chatbot built with 💬 **LangChain**, 🖥️ **Streamlit**, and 🔑 **OpenAI GPT**. This app offers a charming conversational experience with memory, creativity control, and a soft pink UI – perfect for chatting, experimenting, or learning AI development!

---

## 🌟 Features

-  GPT-powered conversational AI (GPT-3.5 or GPT-4)
-  Memory support using LangChain’s `ConversationBufferMemory`
-  Custom soft pink aesthetic and emoji avatars (🤖, 👩‍💻)
-  Chat reset button
-  Adjustable model and temperature (creativity)
-  Deployed with HTTPS via Streamlit Cloud

---

## 🧑‍💻 Technologies Used

| Tool             | Purpose                            |
|------------------|------------------------------------|
| Streamlit        | Web UI framework                   |
| LangChain        | Conversational memory + LLM logic  |
| OpenAI API       | GPT-based language generation      |
| Python           | Core programming language          |
| GitHub           | Version control + deployment       |

---

## 🚀 Getting Started (Local)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/a-friendly-ai-chatbot.git
cd a-friendly-ai-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key

Create a file called:

```
.streamlit/secrets.toml
```

With the content:

```toml
OPENAI_API_KEY = "your-api-key"
```

### 4. Run the app

```bash
streamlit run chatbot.py
```

---

## 🌐 Deploy on Streamlit Cloud

1. Push this repo to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **“New app”**
4. Choose your repo and select:
   - Main file: `chatbot.py`
   - Branch: `main`
5. Add your API key under **Settings → Secrets**:

```toml
OPENAI_API_KEY = "your-api-key"
```

6. Click **Deploy** – You’ll get a secure HTTPS URL 🎉

---

## 📸 Screenshot

<img width="957" height="747" alt="image" src="https://github.com/user-attachments/assets/d4acae4f-b60b-41e7-bb78-8826105b1525" widh = "70px" height = "70px"/>
<img width="937" height="792" alt="image" src="https://github.com/user-attachments/assets/f329f2e2-6b68-4ed7-8fa7-366969980f20" widh = "70px" height = "70px" />


---

## ✨ Credits

Made with love by [@elaa001](https://github.com/YOUR_USERNAME)  
Built using OpenAI and LangChain

---
