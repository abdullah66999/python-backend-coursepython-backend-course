from secrets import token_urlsafe

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
from pydantic import AnyHttpUrl, BaseModel


app = FastAPI(title="URL Shortener")
links: dict[str, str] = {}


class LinkCreate(BaseModel):
    url: AnyHttpUrl


@app.post("/links", status_code=status.HTTP_201_CREATED)
def create_link(payload: LinkCreate):
    key = token_urlsafe(5)
    while key in links:
        key = token_urlsafe(5)
    links[key] = str(payload.url)
    return {"key": key, "url": links[key]}


@app.get("/r/{key}")
def redirect(key: str):
    if key not in links:
        raise HTTPException(status_code=404, detail="Ссылка не найдена")
    return RedirectResponse(links[key], status_code=307)
