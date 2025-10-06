# 🧠 Sentiment-Aware AI Text Generator

## Objective
This project is an AI-powered text generator that produces paragraphs aligned with the sentiment of a given prompt. The app detects whether the input is **Positive**, **Negative**, or **Neutral**, and generates coherent text that matches the emotional tone.

---

## How to Run the App

### Prerequisites
- Python 3.13 or higher
- Internet connection to download pre-trained models

### Steps
1. Clone or download this repository.

2. Navigate to the project folder:
   ```bash
   cd AI_TEXT_GENERATOR

3.Install required packages:

python -m pip install -r Requirements.txt


4.Run the Streamlit app:

streamlit run app.py


5.Open the URL provided in your browser (usually http://localhost:8501) and interact with the app:

Enter a prompt in the text box.

Optionally select a sentiment (or leave on Auto-Detect).

Click Generate Text to see sentiment-aligned output.

## Models Used

DistilBERT (distilbert-base-uncased-finetuned-sst-2-english): For sentiment analysis of the input prompt.

GPT-2: For generating coherent paragraphs based on the detected sentiment.

## Challenges Faced

Ensuring GPT-2 output matches the sentiment accurately.

Avoiding repetitive text in generated paragraphs.

Setting up Streamlit frontend in Google Colab/VS Code with correct pip installations.

Handling long input prompts and truncation warnings from Transformers.

## Optional Features

Manual sentiment selection: Users can choose POSITIVE, NEGATIVE, or NEUTRAL instead of auto-detection.

Adjustable creativity: Temperature, top_p, and repetition_penalty can be fine-tuned in app.py for better text diversity.