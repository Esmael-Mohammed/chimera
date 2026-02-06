from storage.trend_repo import TrendRepository

class Planner:
    def plan(self):
        trends = TrendRepository.fetch_latest()
        return [
            {"trend_id": str(t.id), "action": "generate_post"}
            for t in trends
        ]

if __name__ == "__main__":
    planner = Planner()
    print(planner.plan())
