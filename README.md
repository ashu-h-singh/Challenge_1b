Project Overview :- 

This is an offline document intelligence system designed to extract and prioritize the most relevant sections from a set of documents, tailored to a user persona and a specific task. Built for the Adobe India Hackathon – Challenge 1B.

Key Features :- 

1. Extracts relevant content based on persona and task
2. Ranks sections using TF-IDF and cosine similarity
3. Provides clean bullet-point summaries
4. Runs on CPU only, within 1GB model limit
5. Completes processing within 60 seconds for 3–5 documents
6. Internet-free execution

Folder Structure :- 

CHALLENGE_1B/
│
├── Collection_1/
│   ├── PDFs/
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
│
├── Collection_2/
│   ├── PDFs/
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
│
├── Collection_3/
│   ├── PDFs/
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
│
├── process_collections.py          # Main processing script
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker build file
├── approach_explanation_enhanced.md
└── README.md                       # You are here


Run Instructions :- 

Option 1 – Run Locally (Python)

Step 1: Install Python 3.10+
Step 2: Install dependencies

pip install -r requirements.txt
Step 3: Run the script

python process_collections.py
Output files will be saved as challenge1b_output.json inside each Collection_X folder.

Option 2 – Run Using Docker

Step 1: Build the Docker image

docker build -t adobe-doc-ai .
Step 2: Run the container (make sure your directory is mounted)

docker run --rm -v %cd%:/app adobe-doc-ai  (Windows)
                      or
docker run --rm -v $(pwd):/app adobe-doc-ai  (Linux/macOS)

How It Works :-

1. Reads persona and task from JSON.
2. Scans PDFs and extracts section-wise text.
3. Scores relevance using TF-IDF and task keywords.
4. Ranks sections and adds custom titles.
5. Generates refined bullet summaries.
6. Outputs structured JSON with metadata, rankings, and analysis.

System Requirements :-

Python 3.10+
Docker 
No GPU or internet needed
Max 1GB memory usage
Processes 3–5 documents under 60 seconds

Input/Output :-

Input: challenge1b_input.json
Output: challenge1b_output.json

Includes :-

Input Metadata: persona, task, timestamp
Ranked Sections: title, page, score rank
Sub-section Summary: bullet-style insights

Future Enhancements :-

Use semantic embeddings or domain-aware transformers (if model size permits)
Add GUI for user interaction
Multilingual document support

Docker Repository
You can access and pull the Docker image from Docker Hub here:
🔗 Docker Repo – https://hub.docker.com/repositories/11222750

