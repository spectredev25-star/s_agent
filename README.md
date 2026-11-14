# S Agent

**An AI Engineering Companion that turns software ideas into clear, actionable development plans.**

S Agent helps developers move from an early project idea to a structured engineering workflow. It combines an AI assistant with validated project data so that requirements, milestones, tasks and progress remain understandable and traceable.

> **Project status:** Early MVP development. The repository currently contains the project license and foundational documentation/models are being established. Features described below are the intended MVP scope; they should not be assumed to be implemented yet.

## The problem

A project idea can be exciting but difficult to execute. Requirements may be vague, tasks may be poorly ordered, deadlines may be unrealistic and progress can become disconnected from the original plan. A conversational AI can help with ideas, but its answers alone are not a reliable record of project state.

S Agent is designed to connect AI-assisted planning with structured, verifiable engineering records.

## MVP objective

Enable a user to:

1. Create a project and describe its goals, technology choices and target date.
2. Turn the idea into a structured project analysis.
3. Review and validate the analysis before planning.
4. Organise the work into milestones and actionable tasks.
5. Track task status and inspect project progress.
6. Receive a development report based on saved project information.

The first release prioritises a dependable planning and tracking workflow over autonomous code generation.

## Core principles

- **AI assists; the engineer decides.** Generated analysis and plans are drafts until reviewed.
- **Structured data over chat-only state.** Important project information should be stored in typed records.
- **Deterministic logic for facts.** Validation and progress calculations belong in Python application logic, not in model-generated guesses.
- **Small, testable components.** Domain models, services, agent tools and the interface should have clear responsibilities.
- **Human approval for consequential actions.** The MVP does not give the agent unrestricted authority to modify a user's codebase.

## Initial technical direction

| Area | MVP direction |
|---|---|
| Language | Python 3.12+ |
| Agent runtime | OpenMinion Python SDK (public API) |
| Data validation | Pydantic |
| Initial persistence | SQLite |
| Initial interface | Streamlit |
| Testing | pytest |

The exact OpenMinion package version and provider configuration will be pinned after the team verifies the SDK setup. Model inference may use a configured external provider; a local runtime does not automatically mean local inference.

## High-level architecture

```text
User
 |
Streamlit interface
 |
Application workflow
 |----------------------|
 |                      |
OpenMinion agent     Direct UI actions
 |
Registered agent tools
 |
Python domain services
 |
Repositories
 |
SQLite database
```

**Responsibility boundaries**

- **Models:** define and validate the shape of project information.
- **Services:** implement business rules such as analysis validation, milestone rules and progress calculations.
- **Agent tools:** expose selected service operations to the OpenMinion agent.
- **Repositories:** handle database reads and writes.
- **Interface:** presents information and captures user decisions.

The AI agent should not become the source of truth for project status or calculated metrics.

## Initial domain concepts

- **Project:** the workspace containing a project's identity, goals, technology choices and lifecycle status.
- **Project analysis:** a structured understanding of the idea, including its problem statement, users, objectives, requirements, constraints, assumptions, risks and open questions.
- **Milestone:** a meaningful checkpoint that groups work toward a project outcome.
- **Task:** an actionable unit of work associated with a milestone. Task management will be introduced as the planning workflow is implemented.

## Repository layout

The codebase will grow incrementally. The initial domain layer is organised around:

```text
s_agent/
└── models/
    ├── project.py
    ├── project_analysis.py
    └── milestone.py
```

Additional application, agent, service, database, interface and test modules will be introduced when their implementation begins. This keeps the repository focused and avoids creating empty structures for features that are not yet part of the working MVP.

## Development approach

Work is organised into small, reviewable increments:

1. Agree on domain language and data contracts.
2. Add and test the foundational models.
3. Establish persistence and repository boundaries.
4. Implement the first project-analysis workflow.
5. Add milestone and task planning.
6. Integrate OpenMinion tools with the application services.
7. Build the initial interface and end-to-end demonstration.

Each contribution should include relevant tests and update documentation when it changes a shared contract.

## Project status and contribution

This is an actively developing project. Interfaces and data contracts may evolve as the team validates the MVP. Before adding a new feature, check the existing models and service responsibilities to avoid duplicating logic.

For team contributions:

- Work on a focused feature branch.
- Keep pull requests small and explain the design decision.
- Add tests for validation and business rules.
- Do not commit API keys, local databases or private project data.
- Coordinate changes to shared models before implementing dependent modules.

## License

S Agent is distributed under the Apache License 2.0. See [LICENSE](LICENSE).
