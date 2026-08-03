from fastapi import FastAPI
from agents.orchestrator import run_review
app=FastAPI(title="CodeGuardian AI")
@app.post("/review")
def review(payload:dict): return run_review(payload.get("diff",""))
