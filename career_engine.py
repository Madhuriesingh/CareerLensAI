from transformers import pipeline

# Load Hugging Face model and create generation pipeline
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_career_advice(user_input):
    prompt = f"""
You are a world-class personality coach, career advisor, and life strategist.
Your task is to write a detailed, empowering personality and career analysis for someone based on a paragraph they wrote about themselves.

Return the response in clean markdown format using the structure below. Use emotional depth, actionable language, and clarity. Avoid repetition.

---

### 🧠 1. Who You Are:
Describe this person’s personality and mindset in 3–4 expressive sentences.

### 🔥 2. Core Motivations:
List what emotionally and intellectually drives this person.

### 💪 3. Strengths:
List 4–6 unique strengths or personal traits they seem to have.

### 🚀 4. Ideal Career Path:
Recommend 2–3 career options that align with their interests, values, and talents.

### 💼 5. Business Niche:
Propose one innovative business idea that fits their mindset and life purpose.

### 🛡️ 6. SWOT Summary:
- **Strengths:**
- **Weaknesses:**
- **Opportunities:**
- **Threats:**

### 🌟 7. Life Purpose Statement:
Write 2 sentences summarizing this person’s mission, impact, and philosophy in life.

---

Paragraph:
\"\"\"
{user_input}
\"\"\"
"""
    result = generator(prompt, max_length=700, do_sample=True)[0]['generated_text']
    return result
