import spacy
from typing import Dict, List

# Load the lightweight English model
try:
    nlp = spacy.load("en_core_web_sm")
    # Add custom entity ruler for Tech Skills
    if not nlp.has_pipe("entity_ruler"):
        ruler = nlp.add_pipe("entity_ruler", before="ner")
        patterns = [
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "python"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "java"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "c++"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "c#"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "javascript"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "typescript"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "aws"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "docker"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "kubernetes"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "react"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "angular"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "vue"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "sql"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "nosql"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "machine"}, {"LOWER": "learning"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "data"}, {"LOWER": "science"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "artificial"}, {"LOWER": "intelligence"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "nlp"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "git"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "django"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "flask"}]},
            {"label": "TECH_SKILL", "pattern": [{"LOWER": "fastapi"}]}
        ]
        ruler.add_patterns(patterns)
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
        "locations": [],
        "tech_skills": []
    }

    for ent in doc.ents:
        if ent.label_ == "ORG":
            # Avoid duplicates and very short noise
            if ent.text not in entities["organizations"] and len(ent.text) > 2:
                entities["organizations"].append(ent.text)
        elif ent.label_ in ["GPE", "LOC"]:
            if ent.text not in entities["locations"]:
                entities["locations"].append(ent.text)
        elif ent.label_ == "TECH_SKILL":
            if ent.text not in entities["tech_skills"]:
                entities["tech_skills"].append(ent.text)

    return entities

if __name__ == "__main__":
    test_text = "I worked at Google in New York as a Python Developer. I also studied at Stanford University."
    print(extract_entities(test_text))
