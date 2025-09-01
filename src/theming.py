from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from src.store import SessionLocal, Article

MODEL_PATH = "/mnt/d/models/llm/Llama-3.2-3B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map="auto")

text_gen = pipeline("text-generation", model=model, tokenizer=tokenizer)


def analyze_themes(min_articles=5):
    session = SessionLocal()
    try:
        articles = session.query(Article).all()
        if len(articles) < min_articles:
            print("Not enough articles for theme analysis")
            return []

        texts = [a.text for a in articles]
        combined_text = "\n".join(texts)

        prompt = f"Read the following news articles and summarize the main themes:\n\n{combined_text}\n\nList the themes in bullet points."
        output = text_gen(prompt, max_new_tokens=256, do_sample=True)[0]['generated_text']

        themes = [line.strip("- ").strip() for line in output.splitlines() if line.strip()]
        return themes

    finally:
        session.close()
