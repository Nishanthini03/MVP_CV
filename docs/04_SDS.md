**Software Design Specification (SDS): AI Resume Screener**

**1. System Architecture**

The AI Resume Screener is designed as a modular system with the following core components:

Frontend: Web-based user interface for uploading resumes, job descriptions, and viewing results.

Backend: API server handling data processing, scoring, and result management.

Database: Stores resumes, job descriptions, scores, and LinkedIn data.

AI Models: Responsible for resume parsing, scoring, and LinkedIn activity analysis.


**2. Module Descriptions**

2.1 Frontend Module

Purpose: Allow users to upload resumes and job descriptions, view ranked candidates.

Technologies: Streamlit, CSS

Features:

Resume and job description upload

Visualization of ranking and suggestions

Download CSV of results

2.2 Backend Module

Purpose: Handle data processing and score calculation.

Technologies: Python (Flask/Django), REST API

Features:

Resume parsing

LinkedIn activity analysis

Candidate ranking

Data storage and retrieval

2.3 AI Models Module

Purpose: Process resumes and LinkedIn data to calculate scores.

Technologies: Python (Scikit-learn, NLTK, Spacy), open-source TF-IDF/NLP matcher, ML models (e.g., BERT for NLP)

Features:

Text extraction from resumes

LinkedIn activity scoring

2.4 Database Module

Purpose: Store resumes, job descriptions, scores, and LinkedIn data.

Technologies: PostgreSQL, SQLAlchemy

Features:

Efficient storage and retrieval of candidate data

**3. API Endpoints**

POST /upload-resume: Upload a resume file.

POST /upload-job-desc: Upload a job description.

GET /ranked-candidates: Retrieve ranked candidates list.

GET /csv-export: Download ranked candidates as CSV.

**4. Data Structures**

Resume Data:

Name: String

Contact: String

Full Text: String (entire resume content)

LinkedIn ID: String

Ranking Data:

Resume Score: Float

LinkedIn Score: Float

Total Score: Float


**5. Database Design**

Tables:

Users

Resumes

Job Descriptions

Scores

**6. Technology Stack**

Frontend: Streamlit, CSS

Backend: Python (Flask/Django), REST API

AI Models: Python (Scikit-learn, NLTK, BERT)

Database: PostgreSQL

Hosting: AWS

Version Control: GitHub

