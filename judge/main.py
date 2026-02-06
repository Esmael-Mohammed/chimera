from datetime import datetime
from storage.agent_state_repo import AgentStateRepository
from storage.models import AgentState

class Judge:
    def validate(self, result):
        state = AgentState(
            agent_id="judge",
            last_run=datetime.utcnow(),
            checkpoint=result,
            status="approved"
        )
        AgentStateRepository.save(state)
        return True

if __name__ == "__main__":
    judge = Judge()
    print(judge.validate({"status": "completed"}))
