# 🎥 MovieGPT: A RAG, Gen AI application for Movie Recommendations

![version](https://img.shields.io/badge/version-0.0.1-red?style=for-the-badge) ![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white) ![python](https://img.shields.io/badge/python-3.10-blue?style=for-the-badge) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![ruff](https://img.shields.io/badge/lint-ruff-gold?style=for-the-badge) ![poetry](https://img.shields.io/badge/packaging-poetry-cyan?style=for-the-badge) ![LlamaIndex](https://img.shields.io/badge/LlamaIndex-%F0%9F%A6%99-black?labelColor=purple&style=for-the-badge)

## Getting started
### Docker

🤖 Set up your OpenAI API Token:
```bash
export OPENAI_API_TOKEN=#YOUR_TOKEN
```

🐋 Build the Docker image:
```bash
make docker
```

🏃‍♂️ Run the container:
```bash
make run
```

🕸️ Open the API docs and try it out: http://localhost/docs