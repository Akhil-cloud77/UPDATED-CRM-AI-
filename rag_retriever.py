import json
def retrieve_similar_leads(path="leads_database.json"):
    try:
        with open(path) as f:
            leads = json.load(f)
    except:
        leads = []
        return leads[:3]
