Persona-Driven Document Intelligence :- 

A lightweight, offline-capable document analysis system that extracts and ranks the most relevant sections from a collection of PDF documents — customized for a specific user persona and their job-to-be-done.

Project Overview :- 

This project was developed for the Adobe India Hackathon – Challenge 1B under the theme:
“Connect What Matters — For the User Who Matters.”

The system :-

Accepts 3–5 PDF documents along with a persona and their job description.

Extracts, ranks, and summarizes the most relevant sections.

Returns structured output in JSON format.

Works offline, on CPU, and completes in under 60 seconds per collection.

Key Features :- 

Persona-driven section extraction and ranking.

Uses TF-IDF and cosine similarity for scoring.

Provides bullet-style summaries of extracted sections.

Offline-only execution, requiring no internet access.

Model-free and lightweight (under 1GB).

Compliant with Adobe’s output specification.

Tech Stack :- 

Language – Python 3.10
PDF Processing – PyMuPDF (fitz)
NLP – Scikit-learn, NLTK
Containerization – Docker

Folder Structure :- 

CHALLENGE_1B/
│
├── Collection_1/
│ ├── PDFs/
│ ├── challenge1b_input.json
│ └── challenge1b_output.json
│
├── Collection_2/
├── Collection_3/
│
├── process_collections.py # Main processing script
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build file
├── approach_explanation_enhanced.md
└── README.md # You are here


How It Works :- 

Input is parsed from JSON containing the persona, task, and PDF filenames.

PDFs are processed to extract section titles and content using PyMuPDF.

TF-IDF is applied to score relevance to the persona’s task.

Section titles are enhanced for clarity (e.g., “(HR Task)” or “(Top Activity)”).

The most relevant sections are summarized into bullet points.

All output is structured into an Adobe-compliant JSON format.

Input/Output Example

Sample Input (challenge1b_input.json) :-

Persona: HR Manager

Task :- Identify key employee onboarding steps

Documents: onboarding_policy.pdf, company_handbook.pdf

Sample Output (challenge1b_output.json):

Metadata with timestamp, persona, task, document list

Extracted sections with rank and page

Sub-section analysis with refined bullet points

Docker Instructions

Build the Docker image :-

docker build -t adobe-doc-ai .

Run the Docker container :-

docker run --rm -v (your-folder-path):/app adobe-doc-ai

Make sure the folder containing the collections is correctly mounted inside the container.

Requirements (for Local Execution)

Python 3.10+

Run the following to install dependencies :-

pip install -r requirements.txt

Future Improvements

Add semantic search models if size and performance constraints are relaxed.

Build a user-friendly interface for personas and job descriptions.

Support documents in multiple languages using language detection.
