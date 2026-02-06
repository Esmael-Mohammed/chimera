# Functional Specifications

## User Stories
1. As an Agent, I need to fetch trends from news and social media to stay up to date.
2. As a Planner, I need to decompose a goal into tasks and enqueue them for Workers.
3. As a Worker, I need to execute tasks using MCP tools and return results.
4. As a Judge, I need to approve or reject tasks based on confidence score and persona constraints.

## Swarm Roles
- Planner: DAG task generator
- Worker: Executes atomic task
- Judge: Validates outputs, OCC enforcement
