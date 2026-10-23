from fastapi import FastAPI,HTTPException,Query
from pydantic import BaseModel,Field
from typing import Annotated
import json

app = FastAPI()

class jobcreation(BaseModel):
    

    title: Annotated[str,Field(..., description="which role you are applying for")]
    company: Annotated[str,Field(...,description="tell your company name ")]
    location: Annotated[str,Field(...,description="tell me your location ")]
    salary: Annotated[ int ,Field(...,description="how much salary do you except")]
    skills: Annotated[list[str],Field(...,description="what do you know")]
    experience: Annotated[ int ,Field(..., description="how much you are exprienced")]
    job_type: Annotated[str,Field(...,description="how much time time will you invest in your job ")]



@app.get("/")
def home():
    return {"message: api is running"}
@app.get("/api/health")
async def health_check():
    return {
        "status": "online",
        "message": "Job Portal API is running smoothly.",
        "version": "2.0.0"
    }

def load_data():
    with open("jobs.json" , "r") as f:
        data= json.load(f)

    return data

def save_data(data):
    with open("jobs.json","w") as f :
        data=json.dump(data,f)


@app.get("/jobs")
def get_job():

    data= load_data()

    return data 

@app.post("/create")
def create_job(jobcreation:jobcreation):
    data=load_data()

    if data:
       new_id=max(map(int, data.keys())) + 1
    else:
        new_id=1

    new_job=jobcreation.model_dump()

    new_job["job_id"]=new_id

    data[str(new_id)] = new_job

    save_data(data)

    return new_job

    

@app.get("/jobs/{job_id}")
def search_job(job_id:int):

    data= load_data()

    if str(job_id) not in data:
        raise HTTPException(status_code=404,detail="job id do not found")
    else:
        return data[str(job_id)]


@app.put("/jobs/{job_id}")
def update_job(job_id:int,jobcreation:jobcreation):
    data=load_data()
    if str(job_id) not in data:
        raise HTTPException(status_code=404,detail="job id do not found")

    new_job=jobcreation.model_dump()

    new_job["job_id"]=job_id

    data[str(job_id)] = new_job

    save_data(data)

    return new_job

@app.delete("/jobs/{job_id}")
def delete_job(job_id:int):
        data=load_data()

        if str(job_id) not in data:
            raise HTTPException(status_code=404,detail="job_id not found")

        del data[str(job_id)]

        save_data(data)

        return {"message": "job_id deleted successfully"}

    
@app.get("/jobs/serach/")
def search_jobs(location:str):

    data=load_data()

    results=[]

    for jobs in data.values():
        if location.lower() in jobs["location"].lower():
            results.append(jobs)

    if not results:
        raise HTTPException(status_code=404,detail="no job found with this location")

    return results




    





