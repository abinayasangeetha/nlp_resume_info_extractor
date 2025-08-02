#  NLP Resume Extractor

This project is an NLP-based system to extract structured information (Name, Skills, Degree, Institutions, Work Experience) from resumes in PDF or TXT format.

##  Technologies Used

- Python
- SpaCy
- PyPDF2
- Regex
- Named Entity Recognition (NER)

## Features

- Extracts:
  - Name
  - Skills
  - Degree/Education
  - Work Experience
- Accepts `.pdf` and `.txt` resumes

##  Setup Instructions

```bash
git clone https://github.com/aryabaisakhiya/resume_parser_ner.git
cd resume_parser_ner
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
