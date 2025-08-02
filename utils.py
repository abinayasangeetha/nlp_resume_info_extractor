import re
import spacy
from PyPDF2 import PdfReader

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    text = ""
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def extract_text_from_txt(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        return f.read()

def extract_name(doc, text):
    # 1. Use SpaCy NER
    for ent in doc.ents:
        if ent.label_ == "PERSON" and ent.text.lower() != "lorem":
            return ent.text.strip()

    # 2. Heuristic: Look for uppercase lines near "Web Designer" or similar
    lines = text.split("\n")
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if (
            line_clean.upper() == line_clean
            and 2 <= len(line_clean.split()) <= 4
            and "DESIGNER" in "".join(lines[i + 1 : i + 4]).upper()
        ):
            return line_clean

    # 3. Fallback: Look around phone/email lines
    for i, line in enumerate(lines):
        if any(x in line.lower() for x in ["email", "phone", "www", "@"]):
            for j in range(i - 3, i + 3):
                if 0 <= j < len(lines):
                    candidate = lines[j].strip()
                    if candidate.isupper() and 2 <= len(candidate.split()) <= 4:
                        return candidate

    return "Not Found"

def extract_education(text):
    degrees = ['Bachelor', 'Master', 'B.Tech', 'M.Tech', 'PhD', 'B.E.', 'M.E.', 'B.Sc', 'M.Sc']
    results = []
    for line in text.split('\n'):
        if any(degree.lower() in line.lower() for degree in degrees):
            results.append(line.strip())
    return list(set(results))

def extract_skills(text):
    keywords = [
        "Web Design", "UI/UX Design", "Python", "Java", "C++", "SQL", "HTML", "CSS", "JavaScript",
        "Conflict resolution", "Inventory control", "Marketing", "Advertising", "Typography", "SEO Fundamentals"
    ]
    return list({kw for kw in keywords if kw.lower() in text.lower()})

def extract_experience(text):
    lines = text.split("\n")
    experience = []
    for i, line in enumerate(lines):
        if re.search(r'\b\d{4}\b', line) or any(role in line.lower() for role in ['manager', 'designer', 'team leader']):
            block = "\n".join(lines[i:i+3]).strip()
            if block and block not in experience:
                experience.append(block)
    return experience
