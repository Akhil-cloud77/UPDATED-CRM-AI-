from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_explanation(score, reasons, similar_leads):

    prompt = f"""
You are an AI sales assistant.

Lead score: {score}

Scoring reasons:
{reasons}

Past similar leads:
{similar_leads}

Explain why this lead received this score.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def generate_next_action(score):

    prompt = f"""
Lead score is {score}.
Suggest the next best action for the sales team.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
