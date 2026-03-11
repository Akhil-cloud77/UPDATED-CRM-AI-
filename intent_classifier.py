def classify_intent(score):

    if score >= 80:
        return "High Buying Intent"

    elif score >= 50:
        return "Medium Intent"

    else:
        return "Low Intent"
