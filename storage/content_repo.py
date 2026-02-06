from .db import get_session
from .models import ContentMetadata

class ContentRepository:
    @staticmethod
    def save(content: ContentMetadata):
        session = get_session()
        session.add(content)
        session.commit()
        session.close()
