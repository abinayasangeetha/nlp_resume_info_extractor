import spacy
import json
import os
from utils import extract_text_from_pdf, extract_text_from_txt
from utils import extract_name, extract_education, extract_skills, extract_experience

# Load SpaCy NER model
nlp = spacy.load("en_core_web_sm")

def parse_resume(file_path):
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".txt"):
        text = extract_text_from_txt(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")

    doc = nlp(text)

    return {
        "File": os.path.basename(file_path),
        "Name": extract_name(doc, text),
        "Education": extract_education(text),
        "Skills": extract_skills(text),
        "Experience": extract_experience(text)
    }

if __name__ == "__main__":
    resume_files = [
        "sample_resumes/resume1.pdf",
        "sample_resumes/resume2.txt"
    ]

    results = []
    for file in resume_files:
        print(f"Processing {file}...")
        try:
            result = parse_resume(file)
            results.append(result)
        except Exception as e:
            print(f"Failed to process {file}: {e}")

    os.makedirs("output", exist_ok=True)
    with open("output/all_extracted_data.json", "w") as f:
        json.dump(results, f, indent=4)

    print("All resumes processed. Output saved to 'output/all_extracted_data.json'")
