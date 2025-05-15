**Software Requirements Specification (SRS): AI Resume Screener**

**1. Introduction**

1.1 Purpose

The purpose of this document is to specify the requirements for the AI Resume Screener MVP. The system aims to streamline the resume screening process by ranking resumes based on content and job description matching while providing additional insights using LinkedIn activity analysis.

1.2 Scope

The AI Resume Screener is designed to assist HR professionals and SMEs in shortlisting candidates efficiently. It will rank resumes based on their content and separately score LinkedIn activities to enhance decision-making. The system will present the results on a dashboard with CSV export functionality.

1.3 Definitions

MVP: Minimum Viable Product
SME: Subject Matter Expert
CSV: Comma-Separated Values
LinkedIn Activity: Recent professional engagement on LinkedIn

1.4 References

IEEE Standard 830-1998, Recommended Practice for Software Requirements Specifications

**2. Overall Description**

2.1 Product Perspective

The AI Resume Screener is an automated tool that integrates resume parsing and LinkedIn activity analysis to rank candidates efficiently. The system will offer separate scores for resume content and LinkedIn engagement, displayed on a user-friendly dashboard.

2.2 Product Functions

Upload resumes and job descriptions
Parse resumes to extract information
Analyze LinkedIn activities
Rank candidates based on resume content and LinkedIn activity
Display results on a dashboard
Export rankings as a CSV file

2.3 User Classes

HR Managers: To manage candidate shortlisting
SMEs: To provide domain-specific insights

2.4 Constraints

The system must comply with data protection regulations (e.g., GDPR)
Processing time should not exceed 2 seconds for up to 100 resumes

2.5 Assumptions

Resumes will contain LinkedIn profile information
Users will upload job descriptions for context

**3. Specific Requirements**

3.1 Functional Requirements

Resume Upload (PDF, DOCX)
Job Description Upload
Resume Parsing and LinkedIn ID extraction
LinkedIn Activity Scoring
Candidate Ranking and Scoring
Dashboard Visualization
CSV Export of Results

3.2 Non-functional Requirements

Performance: Efficient processing of bulk resumes
Scalability: Support for increasing data volume
Security: Data protection and user authentication
Usability: Intuitive interface and easy navigation

3.3 External Interfaces

User Interface: Web-based dashboard
Database: Stores resumes, scores, and LinkedIn data
Third-Party APIs: LinkedIn data extraction

**4. Appendices**

A. Glossary of Terms
Resume Parsing: Extracting key information (like name, contact details, skills) from resumes.
LinkedIn Activity Analysis: Assessing professional activities on LinkedIn to derive a score.
Ranking: Arranging candidates in order of suitability based on scores.
CSV Export: Downloading data in a structured, comma-separated format.

B. Acronyms

MVP: Minimum Viable Product
SME: Subject Matter Expert
CSV: Comma-Separated Values
GDPR: General Data Protection Regulation

C. Data Flow Diagrams (DFDs)

DFD Level 0: Overall data flow from user input (resumes, job descriptions) to output (ranked candidates)
DFD Level 1: Detailed flow including resume parsing, LinkedIn analysis, scoring, and export

D. User Interface Mockups

Upload Page: Interface for uploading resumes and job descriptions
Dashboard: Visualization of ranked candidates and suggestions
Results Export: Option to download CSV of ranked candidates

