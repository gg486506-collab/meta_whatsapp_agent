from fastapi import FastAPI, Request
import os

app = FastAPI()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "test_token")

@app.get("/webhook")
async def verify_webhook(
    hub_mode: str | None = None,
    hub_verify_token: str | None = None,
    hub_challenge: str | None = None,
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)
    return {"status": "error", "message": "verification failed"}


@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()
    print("Incoming message:", data)
    return {"status": "received"}


@app.get("/")
async def root():
    return {"status": "Meta WhatsApp Agent running"}
