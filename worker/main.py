from storage.content_repo import ContentRepository
from storage.models import ContentMetadata

class Worker:
    def execute(self, task):
        content = ContentMetadata(
            trend_id=task["trend_id"],
            platform="twitter",
            content_url="https://example.com",
            caption="Auto-generated post"
        )
        ContentRepository.save(content)
        return {"status": "completed", "trend_id": task["trend_id"]}

if __name__ == "__main__":
    worker = Worker()
    print(worker.execute({"trend_id": "demo"}))
