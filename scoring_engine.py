from config import FEATURE_WEIGHTS
def calculate_score(lead):

    score = 0
    reasons = []

    if lead["demo_requested"]:
        score += FEATURE_WEIGHTS["demo_requested"]
        reasons.append("Lead requested demo")

    if lead["registration"]:
        score += FEATURE_WEIGHTS["registration"]
        reasons.append("Lead completed registration")

    if lead["enquiry_call_whatsapp"]:
        score += FEATURE_WEIGHTS["enquiry_call_whatsapp"]
        reasons.append("Lead contacted through call or WhatsApp")

    if lead["price_comparison"]:
        score += FEATURE_WEIGHTS["price_comparison"]
        reasons.append("Lead comparing pricing")

    if lead["lead_event"]:
        score += FEATURE_WEIGHTS["lead_event"]
        reasons.append("Lead came through event")

    if lead["lead_call"]:
        score += FEATURE_WEIGHTS["lead_call"]
        reasons.append("Sales call interaction")

    if lead["lead_referral"]:
        score += FEATURE_WEIGHTS["lead_referral"]
        reasons.append("Referral lead")

    days = lead.get("enquiry_from_days", 30)

    if days <= 3:
        score += 10
        reasons.append("Recent enquiry")

    elif days <= 10:
        score += 5
        reasons.append("Moderately recent enquiry")

    return min(score, 100), reasons
