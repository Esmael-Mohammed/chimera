from .db import get_session
from .models import AgentState

class AgentStateRepository:
    @staticmethod
    def save(state: AgentState):
        session = get_session()
        session.merge(state)
        session.commit()
        session.close()

    @staticmethod
    def load(agent_id: str):
        session = get_session()
        state = session.query(AgentState).filter_by(agent_id=agent_id).first()
        session.close()
        return state
