import streamlit as st
from transformers import pipeline

# -----------------------------
# Load models
# -----------------------------
st.title("🧠 Sentiment-Aware Text Generator")

st.write("""
This app detects the sentiment of your input and generates a paragraph with a similar emotional tone using **GPT-2**.
""")

# Load sentiment analysis and GPT-2 pipelines
@st.cache_resource
def load_pipelines():
    sentiment_analyzer = pipeline("sentiment-analysis")
    text_generator = pipeline("text-generation", model="gpt2")
    return sentiment_analyzer, text_generator

sentiment_analyzer, text_generator = load_pipelines()

# -----------------------------
# Input Section
# -----------------------------
user_input = st.text_area("✍️ Enter your prompt:", placeholder="e.g., I just got a promotion at work!")

manual_sentiment = st.selectbox(
    "🎭 Choose sentiment (optional):",
    ["Auto Detect", "POSITIVE", "NEGATIVE"]
)

if st.button("Generate Text"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        # Auto-detect sentiment or use manual one
        if manual_sentiment == "Auto Detect":
            sentiment = sentiment_analyzer(user_input)[0]['label']
        else:
            sentiment = manual_sentiment

        # Create the prompt for GPT-2
        prompt = f"Write a {sentiment.lower()} paragraph about: {user_input}"

        with st.spinner("Generating text... Please wait ⏳"):
            generated = text_generator(
                prompt,
                max_new_tokens=150,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                repetition_penalty=1.2,
                pad_token_id=text_generator.tokenizer.eos_token_id
            )[0]['generated_text']

        # Clean the generated text
        generated_clean = generated.replace(prompt, "").strip()

        st.success(f"Detected Sentiment: {sentiment}")
        st.write("### 📝 Generated Text:")
        st.write(generated_clean)
