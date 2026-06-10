from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date

from database.db import Base


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(String, unique=True)
    asset_name = Column(String)
    system = Column(String)
    location = Column(String)
    status = Column(String)
    health_score = Column(Integer)


class WorkOrder(Base):
    __tablename__ = "work_orders"

    id = Column(Integer, primary_key=True, index=True)

    wo_id = Column(String, unique=True)

    asset_id = Column(String)

    issue = Column(String)

    priority = Column(String)

    status = Column(String)

    assigned_to = Column(String)


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    incident_id = Column(String, unique=True)

    description = Column(String)

    severity = Column(String)

    status = Column(String)


class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)

    vendor_id = Column(String, unique=True)

    vendor_name = Column(String)

    service_type = Column(String)

    amc_expiry = Column(Date)