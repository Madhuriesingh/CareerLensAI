from transformers import pipeline

# Load the FLAN-T5 model once
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_career_advice(user_input):
    prompt = f"""
Analyze the following paragraph and provide:
1. Strengths
2. Weaknesses
3. Ideal Field of Study
4. Career Path Suggestion
5. SWOT Analysis
6. Skill Recommendations

Paragraph:
{user_input}
"""

    result = generator(prompt, max_length=512, do_sample=True)[0]['generated_text']
    return result
