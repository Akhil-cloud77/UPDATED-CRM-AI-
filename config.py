import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-4o-mini"

FEATURE_WEIGHTS = {
    "demo_requested": 25,
    "registration": 15,
    "enquiry_call_whatsapp": 15,
    "price_comparison": 10,
    "lead_event": 10,
    "lead_call": 5,
    "lead_referral": 20
}
