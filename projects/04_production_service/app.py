import json
import os
import uuid

from fastapi import FastAPI, status
from pydantic import BaseModel, Field
from redis.asyncio import Redis


redis = Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"), decode_responses=True)
app = FastAPI(title="Production Service")


class JobCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)


@app.get("/health")
async def health():
    await redis.ping()
    return {"status": "ok"}


@app.post("/jobs", status_code=status.HTTP_202_ACCEPTED)
async def create_job(payload: JobCreate):
    job_id = str(uuid.uuid4())
    await redis.hset(f"job:{job_id}", mapping={"status": "queued", "name": payload.name})
    await redis.rpush("jobs", json.dumps({"id": job_id, "name": payload.name}))
    return {"job_id": job_id, "status": "queued"}


@app.get("/jobs/{job_id}")
async def get_job(job_id: str):
    job = await redis.hgetall(f"job:{job_id}")
    return job or {"status": "not_found"}
