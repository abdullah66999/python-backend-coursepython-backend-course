import hashlib
import hmac
import os

from fastapi import FastAPI, HTTPException, Request, status


app = FastAPI(title="Webhook Receiver")
SECRET = os.getenv("WEBHOOK_SECRET", "local-dev-secret")
events: set[str] = set()


def verify_signature(body: bytes, header: str, secret: str) -> bool:
    expected = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    received = header.removeprefix("sha256=")
    return hmac.compare_digest(expected, received)


@app.post("/webhooks/provider", status_code=status.HTTP_202_ACCEPTED)
async def receive_webhook(request: Request):
    body = await request.body()
    signature = request.headers.get("X-Signature", "")
    event_id = request.headers.get("X-Event-Id", "")
    if not event_id or not verify_signature(body, signature, SECRET):
        raise HTTPException(status_code=401, detail="Invalid webhook")
    if event_id in events:
        return {"status": "duplicate"}
    events.add(event_id)
    return {"status": "accepted"}
