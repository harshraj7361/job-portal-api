Job Portal API
A simple REST API for managing job listings built with FastAPI.
The project supports CRUD operations and job search by location, with data stored in a local JSON file.

🛠️ Requirements
Python 3.9+

FastAPI

Uvicorn

Pydantic

⚙️ Setup
Clone the repository:

git clone https://github.com/YOUR_USERNAME/job-portal-api.git
cd job-portal-api
Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
▶️ Run
uvicorn main:app --reload
API:

http://127.0.0.1:8000
Swagger documentation:

http://127.0.0.1:8000/docs
🔌 Main Endpoints
Method	Endpoint	Purpose
GET	/	Check API status
GET	/jobs	Get all jobs
GET	/jobs/{job_id}	Get job by ID
POST	/create	Create a job
PUT	/jobs/{job_id}	Update a job
DELETE	/jobs/{job_id}	Delete a job
GET	/jobs/search?location=	Search by location
Create Job
{
  "title": "Backend Developer",
  "company": "Tech Solutions",
  "location": "Delhi",
  "salary": 700000,
  "skills": ["Python", "FastAPI", "SQL"],
  "experience": 1,
  "job_type": "Full-time"
}
🔎 Search
Search jobs by location:

/jobs/search?location=Bengaluru
The search is case-insensitive and supports partial location matching.

💾 Storage
Job data is currently stored in:

jobs.json
📁 Project Structure
job-portal-api/
├── .venv/
├── main.py
├── jobs.json
├── requirements.txt
└── README.md
Built by Harsh Raj 
FastAPI Backend Learning Project
