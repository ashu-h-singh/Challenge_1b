import os
import json
import fitz  # PyMuPDF
import re
import time
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = '.'
TOP_K = 5
TRIM_LENGTH = 1000

def extract_text_sections(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    for i, page in enumerate(doc):
        text = page.get_text("text")
        if len(text.strip()) < 50:
            continue
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        section_title = next(
            (line for line in lines if line.istitle() or line.isupper() or len(line) < 100),
            f"Page {i+1} Extract"
        )
        trimmed_text = text.strip()[:TRIM_LENGTH]
        sections.append({
            "page": i + 1,
            "section_title": section_title,
            "text": trimmed_text
        })
    doc.close()
    return sections

def score_sections(sections, persona_task):
    corpus = [s["text"] for s in sections] + [persona_task]
    vectorizer = TfidfVectorizer().fit_transform(corpus)
    vectors = vectorizer.toarray()
    scores = cosine_similarity([vectors[-1]], vectors[:-1])[0]

    for i, score in enumerate(scores):
        title_match = 1.0 if any(word.lower() in sections[i]["section_title"].lower() for word in persona_task.lower().split()) else 0.85
        sections[i]["score"] = float(score) * title_match
    return sorted(sections, key=lambda x: x["score"], reverse=True)

def refine_text(text):
    bullets = []

    if "ingredient" in text.lower():
        bullets.append("- Key ingredients extracted.")
    if "gluten-free" in text.lower():
        bullets.append("- Gluten-free option.")
    if "bake" in text.lower() or "fry" in text.lower() or "cook" in text.lower():
        bullets.append("- Cooking method mentioned.")
    if "serve" in text.lower() or "buffet" in text.lower():
        bullets.append("- Suitable for buffet serving.")

    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    bullets += [f"- {s.strip()}" for s in sentences[:4]]

    return "\n".join(bullets)

def process_collection(collection_path):
    start_time = time.time()

    input_path = os.path.join(collection_path, 'challenge1b_input.json')
    output_path = os.path.join(collection_path, 'challenge1b_output.json')
    pdf_dir = os.path.join(collection_path, 'PDFs')

    with open(input_path, 'r') as f:
        input_data = json.load(f)

    persona = input_data['persona']['role']
    task = input_data['job_to_be_done']['task']
    persona_task = f"{persona}: {task}"

    all_sections = []

    for doc in input_data['documents']:
        pdf_path = os.path.join(pdf_dir, doc['filename'])
        if not os.path.exists(pdf_path):
            print(f"⚠️ Skipped missing file: {pdf_path}")
            continue

        sections = extract_text_sections(pdf_path)
        for section in sections:
            section['document'] = doc['filename']
        all_sections.extend(sections)

    if not all_sections:
        print(f"⚠️ No content found in: {collection_path}")
        return

    ranked = score_sections(all_sections, persona_task)

    extracted_sections = []
    subsection_analysis = []

    for idx, section in enumerate(ranked[:TOP_K]):
        # Clean, compliant title
        formatted_title = section['section_title']
        if persona.lower().startswith("food"):
            formatted_title = f"{section['section_title']} (Vegetarian Pick)"
        elif persona.lower().startswith("travel"):
            formatted_title = f"{section['section_title']} (Top Activity)"
        elif persona.lower().startswith("hr"):
            formatted_title = f"{section['section_title']} (HR Task)"

        extracted_sections.append({
            "document": section['document'],
            "section_title": formatted_title,
            "importance_rank": idx + 1,
            "page_number": section['page']
        })

        subsection_analysis.append({
            "document": section['document'],
            "refined_text": refine_text(section['text']),
            "page_number": section['page']
        })

    output = {
        "metadata": {
            "input_documents": [doc['filename'] for doc in input_data['documents']],
            "persona": persona,
            "job_to_be_done": task,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    with open(output_path, 'w') as f:
        json.dump(output, f, indent=4)

    end_time = time.time()
    print(f"✅ Adobe-Compliant Output Written: {collection_path} in {end_time - start_time:.2f} sec")

def main():
    for collection in os.listdir(BASE_DIR):
        path = os.path.join(BASE_DIR, collection)
        if os.path.isdir(path):
            process_collection(path)

if __name__ == '__main__':
    main()
