import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_career_report(user_input):
    prompt = f"""
You are a highly experienced career counselor and strategic life coach.
Analyze the following paragraph and provide:
1. Strengths
2. Weaknesses
3. Ideal Field of Study
4. Recommended Career Path
5. SWOT Analysis
6. Niche Business Suggestions
7. Skill Roadmap with learning platforms

Paragraph:
\"\"\"
{user_input}
\"\"\"

Respond in markdown format with clear section headers.
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
