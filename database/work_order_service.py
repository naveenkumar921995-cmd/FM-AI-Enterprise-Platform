import uuid

work_orders = []


def create_work_order(
        system,
        issue,
        priority="Medium"
):

    wo = {
        "wo_id": str(uuid.uuid4())[:8],
        "system": system,
        "issue": issue,
        "priority": priority,
        "status": "Open"
    }

    work_orders.append(wo)

    return wo