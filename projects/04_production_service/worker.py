import asyncio
import json
import os

from redis.asyncio import Redis


async def main() -> None:
    redis = Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"), decode_responses=True)
    while True:
        _, raw = await redis.blpop("jobs")
        job = json.loads(raw)
        await redis.hset(f"job:{job['id']}", mapping={"status": "done", "name": job["name"]})


if __name__ == "__main__":
    asyncio.run(main())
