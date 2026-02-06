# Project Chimera - Autonomous Influencer Network
## Vision
Build a scalable swarm of autonomous AI influencers with economic and creative agency.

## Constraints
- All external interactions via MCP.
- Strict HITL governance for low-confidence or sensitive tasks.
- Multi-tenant, cloud-native architecture.
- Planner-Worker-Judge fast-render swarm pattern.

## Architecture Summary
- Hub-and-Spoke: Central Orchestrator + agent swarms
- MCP for all Resources/Tools/Prompts
- Redis queues: task_queue, review_queue
- PostgreSQL for transactional data, Weaviate for long-term memory
- Coinbase AgentKit for financial autonomy
