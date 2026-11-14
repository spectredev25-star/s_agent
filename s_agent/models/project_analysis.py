"""Structured project-analysis domain models."""

from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


class ProjectAnalysisStatus(StrEnum):
    """Review state of an analysis draft."""

    DRAFT = "draft"
    VALIDATED = "validated"
    APPROVED = "approved"
    SUPERSEDED = "superseded"


class RequirementCategory(StrEnum):
    FUNCTIONAL = "functional"
    NON_FUNCTIONAL = "non_functional"


class RequirementPriority(StrEnum):
    MUST_HAVE = "must_have"
    SHOULD_HAVE = "should_have"
    COULD_HAVE = "could_have"


class RiskLevel(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ProjectRequirement(BaseModel):
    """A requirement identified during project analysis."""

    model_config = ConfigDict(str_strip_whitespace=True)

    id: UUID = Field(default_factory=uuid4)
    title: str = Field(min_length=3, max_length=160)
    description: str = Field(min_length=5, max_length=2000)
    category: RequirementCategory
    priority: RequirementPriority = RequirementPriority.SHOULD_HAVE
    acceptance_criteria: list[str] = Field(default_factory=list)


class AnalysisRisk(BaseModel):
    """A potential project risk and its assessed severity."""

    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=3, max_length=160)
    description: str = Field(min_length=5, max_length=1500)
    level: RiskLevel = RiskLevel.MEDIUM
    mitigation: str | None = Field(default=None, max_length=1500)


class ProjectAnalysis(BaseModel):
    """Versioned analysis of a project's idea and requirements.

    The analysis is a reviewable artifact. Creating one does not imply that
    its requirements have been approved or that a roadmap has been activated.
    """

    id: UUID = Field(default_factory=uuid4)
    project_id: UUID
    version: int = Field(default=1, ge=1)
    status: ProjectAnalysisStatus = ProjectAnalysisStatus.DRAFT

    problem_statement: str = Field(min_length=10, max_length=3000)
    target_users: list[str] = Field(default_factory=list)
    objectives: list[str] = Field(default_factory=list)
    requirements: list[ProjectRequirement] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    risks: list[AnalysisRisk] = Field(default_factory=list)
    open_questions: list[str] = Field(default_factory=list)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    approved_at: datetime | None = None
