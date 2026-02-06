## Technical Specification

### Trend API Contract

Input:
{
  "platform": "string",
  "region": "string"
}

Output:
{
  "trends": [
    {
      "id": "string",
      "keyword": "string",
      "score": "number"
    }
  ]
}

### Database Schema (ERD)

Table: videos
- id (uuid)
- title (string)
- platform (string)
- views (int)
- created_at (timestamp)
