# DeepSeek Code Buddy

🧠 AI Pair Programmer with Debugging Superpowers | Built with Ollama & LangChain

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-FF6C37?style=for-the-badge&logo=python&logoColor=white)](https://python.langchain.com/)
[![Ollama](https://img.shields.io/badge/Ollama-00ADD8?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.ai/)

## 🚀 Features

- 🐍 Python-specific coding assistance
- 🐞 Intelligent debugging with strategic print statements
- 📚 Code documentation generation
- 💡 Multiple model support (Deepseek 1.5B/3B)
- 🎨 Developer-friendly dark mode UI
- 🔄 Context-aware conversation history

## 📦 Prerequisites

- [Ollama](https://ollama.ai/) installed and running
- Python 3.9+
- Required packages:
  ```bash
  pip install streamlit langchain-community langchain-core requests
  ```

## ⚡ Quick Start

1. **Install Ollama models**:
   ```bash
   ollama pull deepseek-r1:1.5b
   ollama pull deepseek-r1:3b
   ```

2. **Clone repository**:
   ```bash
   git clone https://github.com/yourusername/deepseek-code-buddy.git
   cd deepseek-code-buddy
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the app**:
   ```bash
   streamlit run app.py
   ```

## 🛠️ Configuration

- Choose between Deepseek models in the sidebar
- Adjust temperature parameter in `app.py`:
  ```python
  llm_engine = ChatOllama(
      model=selected_model,
      base_url="http://localhost:11434",
      temperature=0.3  # Adjust creativity (0-1)
  )
  ```

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/c0ffcb17-5e10-4384-ac80-6320643dd406)

![App Interface](screenshots/interface-dark.png)
*With Coding Example*

## 🌟 Features Roadmap

- [ ] Add code formatting capabilities
- [ ] Implement session history persistence
- [ ] Add error handling diagnostics
- [ ] Support for additional programming languages
- [ ] Integration with VS Code extension

## 🤝 Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) team for the amazing local LLM framework
- [LangChain](https://python.langchain.com/) for AI orchestration
- [Deepseek](https://deepseek.com/) for their open weights models

---

**Repository Structure**:
```
deepseek-code-buddy/
├── app.py                  # Main application code
├── requirements.txt        # Dependency list
├── LICENSE
├── README.md
├── screenshots/            # Application screenshots
│   └── interface-dark.png
└── .gitignore
```

**requirements.txt**:
```
streamlit>=1.31.0
langchain-community>=0.0.25
langchain-core>=0.1.40
requests>=2.31.0
```

This structure provides:
- Clear installation instructions
- Visual documentation with screenshots
- Roadmap for future development
- Contribution guidelines
- Proper licensing and acknowledgments
- Easy-to-follow configuration options
by Shees Ikram
