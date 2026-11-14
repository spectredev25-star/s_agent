"""Milestone domain model."""

from datetime import date, datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


class MilestoneStatus(StrEnum):
    """Progress state of a project milestone."""

    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    AT_RISK = "at_risk"
    COMPLETED = "completed"


class Milestone(BaseModel):
    """A measurable checkpoint within a project roadmap."""

    model_config = ConfigDict(str_strip_whitespace=True)

    id: UUID = Field(default_factory=uuid4)
    project_id: UUID
    title: str = Field(min_length=3, max_length=160)
    description: str | None = Field(default=None, max_length=2000)
    sequence: int = Field(ge=1)
    status: MilestoneStatus = MilestoneStatus.NOT_STARTED
    target_date: date | None = None
    acceptance_criteria: list[str] = Field(default_factory=list)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: datetime | None = None
