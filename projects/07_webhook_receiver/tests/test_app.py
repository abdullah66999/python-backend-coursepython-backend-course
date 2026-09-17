import hashlib
import hmac

from fastapi.testclient import TestClient

from app import SECRET, app, events


client = TestClient(app)


def signature(body: bytes) -> str:
    digest = hmac.new(SECRET.encode(), body, hashlib.sha256).hexdigest()
    return f"sha256={digest}"


def test_webhook_is_idempotent():
    events.clear()
    body = b'{"type":"payment.succeeded"}'
    headers = {"X-Signature": signature(body), "X-Event-Id": "evt-1"}
    first = client.post("/webhooks/provider", content=body, headers=headers)
    second = client.post("/webhooks/provider", content=body, headers=headers)
    assert first.status_code == 202
    assert second.json() == {"status": "duplicate"}


def test_invalid_signature_is_rejected():
    response = client.post("/webhooks/provider", content=b"{}", headers={"X-Event-Id": "evt-2", "X-Signature": "bad"})
    assert response.status_code == 401
