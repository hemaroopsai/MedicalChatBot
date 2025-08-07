# 🩺 Medical AI Chatbot Assistant

A **Streamlit-based AI chatbot** built using **LangChain** and **Ollama** that answers medical questions with contextual awareness, PDF document ingestion, multilingual support, voice input, and relevant visual media suggestions.

![Streamlit App Screenshot](chatbot.jpg)

---

## 🚀 Features

- ✅ **Medical Contextual Q&A** powered by local LLM (`wizardlm2`)
- 📄 **PDF Ingestion**: Upload and embed your own medical documents
- 🎙️ **Voice Input**: Ask questions via microphone using speech-to-text
- 🌍 **Multilingual Responses**: Translate answers into **English**, **Telugu**, or **Tamil**
- 🧠 **Semantic Search** using vector embeddings (`nomic-embed-text`)
- 🖼️ **Visual Aid Suggestions**: Auto-display relevant images/GIFs based on the query
- 🛠️ **Local Deployment** using Ollama + LangChain + Chroma vector store

---

## 🛠️ Tech Stack

| Tool/Library           | Purpose                                      |
|------------------------|----------------------------------------------|
| **Streamlit**          | Web UI framework                             |
| **LangChain**          | LLM orchestration and chaining               |
| **Ollama**             | Local LLM and embedding model runner         |
| **Chroma**             | Vector store for semantic retrieval          |
| **Whisper/SpeechRecognition** | Voice-to-text conversion              |
| **PDFPlumber**         | PDF document reading                         |
| **Deep Translator**    | Answer translation                          |

---

## 📂 Folder Structure

```plaintext
project/
│
├── app.py                  # Main Streamlit app
├── chatbot.jpg             # UI image
├── pdf/                    # Uploaded medical PDFs
├── db/                     # Chroma vector store
├── medibot/                # Media folders (e.g., bleeding/, cpr/)
│   ├── bleeding/
│   │   ├── img1.jpg
│   │   └── img2.gif
│   └── burns/
│       └── example.png
