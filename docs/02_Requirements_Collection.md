**Requirements Collection: AI Resume Screener**

**Product Expectations**
The AI Resume Screener aims to enhance the recruitment process by automating resume screening and incorporating LinkedIn activity analysis. The system should be efficient, user-friendly, and capable of handling bulk resume uploads. It should offer separate scoring for resume content and LinkedIn activity, along with suggestions for candidates with moderate resume scores but high LinkedIn engagement.

**Functional Requirements**

Resume Upload:
    Support for PDF and DOCX formats.
    Batch upload of multiple resumes.

Job Description Upload:
    Support for text.

Resume Parsing:
    Extract relevant information, including LinkedIn IDs.

LinkedIn Activity Analysis:
    Analyze professional activities from the last year.
    Provide a separate LinkedIn activity score.

Scoring and Ranking:
    Generate a resume score based on content and job description matching.
    Generate a LinkedIn score based on professional activity.
    Display both scores separately on the dashboard.

Dashboard Visualization:
    Show ranked candidates based on resume and LinkedIn scores.
    Highlight suggestions for candidates with high LinkedIn scores and moderate resume scores.

CSV Export:
    Export the list of ranked candidates as a CSV file.

**Non-Functional Requirements**

Performance:
Process and rank up to 100 resumes within 2 seconds.

Scalability:
Handle increasing data volume efficiently.

Data Privacy:
Ensure compliance with data protection regulations (e.g., GDPR).

User Experience:
Intuitive and responsive UI.
Clear presentation of ranking results.

Reliability:
High availability and minimal downtime.

Security:
Protect sensitive information and credentials.