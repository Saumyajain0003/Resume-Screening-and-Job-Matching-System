import spacy
from typing import Dict, List

# Load the lightweight English model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Fallback if the user hasn't downloaded the model yet
    nlp = None

def extract_entities(text: str) -> Dict[str, List[str]]:
    """
    Extracts key entities (Organizations and Locations) from the text.
    """
    if not nlp:
        return {"organizations": [], "locations": []}

    doc = nlp(text)
    
    entities = {
        "organizations": [],
        "locations": []
    }

    for ent in doc.ents:
        if ent.label_ == "ORG":
            # Avoid duplicates and very short noise
            if ent.text not in entities["organizations"] and len(ent.text) > 2:
                entities["organizations"].append(ent.text)
        elif ent.label_ in ["GPE", "LOC"]:
            if ent.text not in entities["locations"]:
                entities["locations"].append(ent.text)

    return entities

if __name__ == "__main__":
    test_text = "I worked at Google in New York as a Python Developer. I also studied at Stanford University."
    print(extract_entities(test_text))
