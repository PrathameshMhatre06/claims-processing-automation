from sqlalchemy.orm import Session
from app.models import ClaimDB


def create_claim(db: Session, claim_data, decision):
    db_claim = ClaimDB(
        claim_id=claim_data.claim_id,
        policy_id=claim_data.policy_id,
        patient_name=claim_data.patient_name,
        patient_age=claim_data.patient_age,
        hospital_name=claim_data.hospital_name,
        diagnosis=claim_data.diagnosis,
        claim_amount=claim_data.claim_amount,
        status=decision["status"],
        approved_amount=decision["approved_amount"],
    )

    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)

    return db_claim
