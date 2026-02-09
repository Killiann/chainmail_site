import uuid
from sqlalchemy import Column, Float, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Weave(Base):
    __tablename__ = "weaves"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    min_ar = Column(Float)
    max_ar = Column(Float)
    picture = Column(String)
    tutorial_link = Column(String)
    multi_ringsize = Column(Boolean)    

    family_weaves = relationship(
        "FamilyWeave",
        back_populates="weave",
        cascade="all, delete-orphan"
    )

    families = relationship(
        "Family",
        secondary="family_weave",
        back_populates="weaves",
        viewonly=True
    )

class Family(Base):
    __tablename__ = "families"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    family_weaves = relationship(
        "FamilyWeave",
        back_populates="family",
        cascade="all, delete-orphan"
    )

    weaves = relationship(
        "Weave",
        secondary="family_weave",
        back_populates="families",
        viewonly=True
    )

class FamilyWeave(Base):
    __tablename__ = "family_weave"

    weave_uuid = Column(UUID(as_uuid=True), ForeignKey("weaves.uuid"), primary_key=True)
    family_uuid = Column(UUID(as_uuid=True), ForeignKey("families.uuid"), primary_key=True)

    weave = relationship("Weave", back_populates="family_weaves")
    family = relationship("Family", back_populates="family_weaves")
