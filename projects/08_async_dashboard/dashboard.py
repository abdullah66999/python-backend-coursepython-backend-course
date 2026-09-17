import asyncio

import httpx


async def load_with_client(client: httpx.AsyncClient, user_id: int) -> dict:
    responses = await asyncio.gather(
        client.get(f"https://profile.test/users/{user_id}"),
        client.get(f"https://billing.test/users/{user_id}"),
        client.get(f"https://notify.test/users/{user_id}"),
        return_exceptions=True,
    )
    result = {"profile": None, "balance": None, "notifications": None, "warnings": []}
    names = ("profile", "balance", "notifications")
    for name, response in zip(names, responses):
        if isinstance(response, Exception) or response.status_code >= 400:
            result["warnings"].append(name)
        else:
            result[name] = response.json()
    return result


def transport(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={"service": request.url.host, "ok": True})


async def main() -> None:
    async with httpx.AsyncClient(transport=httpx.MockTransport(transport), timeout=3) as client:
        print(await load_with_client(client, 42))


if __name__ == "__main__":
    asyncio.run(main())
