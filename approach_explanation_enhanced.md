Adobe India Hackathon – Challenge 1B
Persona-Driven Document Intelligence – Simplified Summary

Section: Objective
Build a document analysis system

Targeted to personas and their job-to-be-done

Must work across domains (HR, travel, finance, etc.)

Constraints: CPU-only, <1GB model, <60s processing, no internet

Section: System Workflow
1. Input Parsing

JSON input: documents, persona, task

2. PDF Content Extraction

Tool: PyMuPDF

Output: title, page number, trimmed text

3. Section Scoring

Method: TF-IDF + Cosine Similarity

Heuristics: Boost if title matches task keywords

4. Title Enhancement

Add persona-friendly suffixes (e.g., "Top Activity")

5. Subsection Summary

Bullet points

Sentence slicing (first 3–5 lines)

6. Output Structure

Metadata: persona, task, document list, timestamp

Extracted Sections: title, page, rank

Subsection Analysis: refined bullets, page

Section: Constraints Met
Runs on CPU

Model size < 1GB

3–5 docs processed in under 60s

Works offline

Section: Unique Strengths
Adaptable across domains

No black-box AI; logic is interpretable

Summaries are personalized and clean

Lightweight, scalable design

Section: Final Message
Helps users extract the most relevant insights fast

Based on who they are and what they need to do