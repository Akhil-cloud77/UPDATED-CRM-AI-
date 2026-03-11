from fastapi import FastAPI

from scoring_engine import calculate_score
from rag_retriever import retrieve_similar_leads
from genai_service import generate_explanation, generate_next_action
from intent_classifier import classify_intent
from email_generator import generate_sales_email

app = FastAPI(title="GenAI CRM Lead Scoring Agent")


@app.get("/")
def home():

    return {"message": "GenAI Lead Scoring Assistant Running"}


@app.post("/score-lead")
def score_lead(lead: dict):

    score, reasons = calculate_score(lead)

    similar_leads = retrieve_similar_leads()

    explanation = generate_explanation(score, reasons, similar_leads)

    action = generate_next_action(score)

    intent = classify_intent(score)

    email = generate_sales_email(intent)

    return {
        "lead_score": score,
        "intent_level": intent,
        "rule_reasons": reasons,
        "ai_explanation": explanation,
        "next_best_action": action,
        "suggested_sales_email": email
    }
