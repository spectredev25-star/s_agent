"""Project domain models.

These Pydantic models describe validated application data. They do not perform
database persistence; repositories will handle that in a later implementation.
"""

from datetime import date, datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


class ProjectStatus(StrEnum):
    """Lifecycle state of a project workspace."""

    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class ProjectBase(BaseModel):
    """Fields shared by project creation and stored project records."""

    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=3, max_length=120)
    description: str | None = Field(default=None, max_length=2000)
    objectives: list[str] = Field(default_factory=list)
    tech_stack: list[str] = Field(default_factory=list)
    target_date: date | None = None


class ProjectCreate(ProjectBase):
    """Validated input required to create a project."""


class ProjectUpdate(BaseModel):
    """Partial project update.

    Use model_dump(exclude_unset=True) when applying updates so omitted fields
    are not confused with fields explicitly set to None.
    """

    model_config = ConfigDict(str_strip_whitespace=True)

    name: str | None = Field(default=None, min_length=3, max_length=120)
    description: str | None = Field(default=None, max_length=2000)
    objectives: list[str] | None = None
    tech_stack: list[str] | None = None
    target_date: datetime | None = None
    status: ProjectStatus | None = None


class Project(ProjectBase):
    """Persistable project record returned by the application."""

    id: UUID = Field(default_factory=uuid4)
    status: ProjectStatus = ProjectStatus.DRAFT
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
