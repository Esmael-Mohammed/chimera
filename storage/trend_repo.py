from .db import get_session
from .models import Trend

class TrendRepository:
    @staticmethod
    def save(trend: Trend):
        session = get_session()
        session.add(trend)
        session.commit()
        session.close()

    @staticmethod
    def fetch_latest(limit=5):
        session = get_session()
        trends = (
            session.query(Trend)
            .order_by(Trend.ingested_at.desc())
            .limit(limit)
            .all()
        )
        session.close()
        return trends
