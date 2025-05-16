Test Cases: AI Resume Screener MVP

1. Upload Functionality

Test Case ID

Description

Input

Expected Output

Status

TC-01

Upload a valid resume file

Valid PDF/Docx file

Successful upload message



TC-02

Upload an invalid file format

Image or unsupported file type

Error message indicating unsupported format



TC-03

Upload without selecting a file

No file selected

Warning message to select a file



2. Scoring and Ranking

Test Case ID

Description

Input

Expected Output

Status

TC-04

Generate resume score

Valid resume data

Resume score displayed on dashboard



TC-05

LinkedIn activity scoring

Valid LinkedIn ID

LinkedIn score displayed separately



TC-06

Suggestion for average resume with high LinkedIn score

Resume and LinkedIn data

Highlighted suggestion on dashboard



3. Dashboard and CSV Export

Test Case ID

Description

Input

Expected Output

Status

TC-07

Display ranked candidates

Multiple uploaded resumes

Ranked list shown on dashboard



TC-08

Download CSV file

Click download button

CSV file downloaded with correct data



4. Error Handling

Test Case ID

Description

Input

Expected Output

Status

TC-09

Missing LinkedIn ID in resume

Resume without LinkedIn ID

Warning message



TC-10

Backend API failure

Server down

Error message indicating server issue

