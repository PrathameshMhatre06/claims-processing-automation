def evaluate_claim(claim):
    """
    Simple business rules for claim approval
    """

    # Rule 1: Very high amount → manual review
    if claim.claim_amount > 50000:
        return {
            "status": "MANUAL_REVIEW",
            "approved_amount": 0.0,
            "remarks": "High claim amount, sent for manual review"
        }

    # Rule 2: Senior citizen → manual review
    if claim.patient_age > 60:
        return {
            "status": "MANUAL_REVIEW",
            "approved_amount": 0.0,
            "remarks": "Senior citizen claim, requires review"
        }

    # Rule 3: Otherwise auto approve
    return {
        "status": "APPROVED",
        "approved_amount": claim.claim_amount,
        "remarks": "Auto-approved as per rules"
    }
