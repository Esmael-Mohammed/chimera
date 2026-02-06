# Technical Specifications

## JSON Schemas
### Agent Task
{
  "task_id": "uuid-v4-string",
  "task_type": "generate_content | reply_comment | execute_transaction",
  "priority": "high | medium | low",
  "context": {...},
  "assigned_worker_id": "string",
  "created_at": "timestamp",
  "status": "pending | in_progress | review | complete"
}

### MCP Tool
{
  "name": "post_content",
  "description": "Publishes text and media to a connected social platform.",
  "inputSchema": {...}
}
