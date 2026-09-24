from fastapi import FastAPI

app = FastAPI(title="Insify Fingerprint Service")


@app.get("/health")
async def health_check():
    return {"status": "ok"}