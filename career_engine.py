from transformers import pipeline

# Load the FLAN-T5 Large model for higher-quality outputs
generator = pipeline("text2text-generation", model="google/flan-t5-large")

def generate_career_advice(user_input):
    prompt = f"""
You are a world-class personality coach and career strategist.
You are writing a detailed, inspiring personality and career report based on a paragraph someone wrote about themselves.

Respond using this exact format with markdown-style formatting and emotional richness:

### 🧠 Who You Are:
(3–4 sentence description of the person's personality, mindset, and emotional qualities.)

### 🔥 Core Motivations:
- Bullet list of deep internal drivers (values, desires, beliefs)

### 💪 Strengths:
- Bullet list of 4–6 strong personal traits or abilities

### 🚀 Career Path Suggestions:
- List 2–3 ideal roles this person could thrive in

### 💼 Business Niche Idea:
(One innovative or purpose-driven business idea tailored to them)

### 🛡️ SWOT Summary:
- **Strengths:** 
- **Weaknesses:** 
- **Opportunities:** 
- **Threats:** 

### 🌟 Life Purpose Statement:
(A powerful, motivational 2-sentence summary of their mission or philosophy)

---

Paragraph:
\"\"\"{user_input}\"\"\"
"""

    result = generator(
        prompt,
        max_length=1024,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95
    )[0]['generated_text']

    return result
