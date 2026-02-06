from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.models import ClaimRequest, ClaimResponse, ClaimDB
from app.rules import evaluate_claim
from app.database import SessionLocal, engine
from app.crud import create_claim

app = FastAPI(title="Claims Processing Automation API")

# Create tables
ClaimDB.metadata.create_all(bind=engine)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def health_check():
    return {"status": "OK"}


@app.post("/submit-claim", response_model=ClaimResponse)
def submit_claim(claim: ClaimRequest, db: Session = Depends(get_db)):
    decision = evaluate_claim(claim)

    create_claim(db, claim, decision)

    return ClaimResponse(
        claim_id=claim.claim_id,
        status=decision["status"],
        approved_amount=decision["approved_amount"],
        remarks=decision["remarks"],
    )
