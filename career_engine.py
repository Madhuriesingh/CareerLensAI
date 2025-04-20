from transformers import pipeline

# Use the larger, more capable model for better output
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
