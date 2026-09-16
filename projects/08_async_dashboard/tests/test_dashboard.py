import asyncio

import httpx

from dashboard import load_with_client


def handler(request: httpx.Request) -> httpx.Response:
    if "billing" in request.url.host:
        return httpx.Response(503)
    return httpx.Response(200, json={"ok": True})


def test_partial_failure_becomes_warning():
    async def scenario():
        transport = httpx.MockTransport(handler)
        async with httpx.AsyncClient(transport=transport) as client:
            return await load_with_client(client, 42)

    result = asyncio.run(scenario())
    assert result["profile"] == {"ok": True}
    assert "billing" in result["warnings"]
