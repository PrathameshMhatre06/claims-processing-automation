from pydantic import BaseModel
from typing import Optional


class ClaimRequest(BaseModel):
    claim_id: str
    policy_id: str
    patient_name: str
    patient_age: int
    hospital_name: str
    diagnosis: str
    claim_amount: float


class ClaimResponse(BaseModel):
    claim_id: str
    status: str
    approved_amount: float
    remarks: Optional[str] = None

from sqlalchemy import Column, String, Integer, Float
from app.database import Base


class ClaimDB(Base):
    __tablename__ = "claims"

    claim_id = Column(String, primary_key=True, index=True)
    policy_id = Column(String)
    patient_name = Column(String)
    patient_age = Column(Integer)
    hospital_name = Column(String)
    diagnosis = Column(String)
    claim_amount = Column(Float)
    status = Column(String)
    approved_amount = Column(Float)
