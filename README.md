# Prodia AI Image Generator

[![CI](https://github.com/Huzaifa-zuberi/prodia-app/actions/workflows/ci.yml/badge.svg)](https://github.com/Huzaifa-zuberi/prodia-app/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey?logo=flask)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-success)](LICENSE)
![Last Commit](https://img.shields.io/github/last-commit/Huzaifa-zuberi/prodia-app)
![Stars](https://img.shields.io/github/stars/Huzaifa-zuberi/prodia-app?style=social)

A Flask web application that generates AI images using Hugging Face's Inference API. Features a clean, modern UI with prompt suggestions and real-time image generation.

**Repo:** [Huzaifa-zuberi/prodia-app](https://github.com/Huzaifa-zuberi/prodia-app)

## Screenshots

*(Add a screenshot of the app here)*

## Features

- AI image generation via Hugging Face models
- Modern dark-themed UI
- Prompt example suggestions
- Real-time image display with download option

## Quick Start

```bash
git clone https://github.com/Huzaifa-zuberi/prodia-app.git
cd prodia-app
pip install flask flask-cors requests python-dotenv
echo "HF_API_TOKEN=your_huggingface_token" > .env
python server.py
```

Open http://127.0.0.1:5000

## Configuration

Set your Hugging Face API token in a `.env` file:

```
HF_API_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxx
```

Get a free token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).

## Project Structure

```
prodia-app/
├── server.py          # Flask backend (API proxy)
├── public/
│   ├── index.html     # Frontend UI
│   ├── style.css      # Styling
│   └── app.js         # JavaScript logic
├── .env               # API token (not tracked)
├── .gitignore
└── README.md
```

## License

MIT © 2026 Huzaifa Zuberi
