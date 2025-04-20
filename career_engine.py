from transformers import pipeline

# Load Hugging Face FLAN-T5 model
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_career_report(user_input):
    prompt = f"""
You are a compassionate career coach and personality analyst.
Analyze the following paragraph and return a report in this format:

### 1. Who You Are:
(A short description of personality, mindset, and style)

### 2. Core Motivations:
(What drives this person deep down?)

### 3. Strengths:
(A list of major strengths)

### 4. Ideal Career Path:
(One or two ideal career roles)

### 5. Business Niche:
(Suggest a niche business idea based on their interests and traits)

### 6. SWOT Summary:
- Strengths:
- Weaknesses:
- Opportunities:
- Threats:

### 7. Life Purpose Statement:
(A two-sentence personal mission inspired by their values and goals)

Paragraph:
\"\"\"
{user_input}
\"\"\"
"""
    result = generator(prompt, max_length=600, do_sample=True)[0]['generated_text']
    return result
