from fastapi import FastAPI

app = FastAPI(title="Server Health API")

@app.get("/health")
def health():
    return {"status": "ok", "version": 3}