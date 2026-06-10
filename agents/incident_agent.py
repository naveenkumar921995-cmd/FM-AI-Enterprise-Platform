from database.work_order_service import create_work_order
import uuid


def incident_agent(query):

    incident_id = str(uuid.uuid4())[:8]

    wo = create_work_order(
        system="Incident",
        issue=query,
        priority="High"
    )

    return {
        "agent": "Incident Agent",
        "incident_id": incident_id,
        "work_order": wo,
        "answer":
            "Incident registered and work order created."
    }