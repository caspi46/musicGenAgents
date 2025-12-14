from base_agent import BaseAgent 

class ProducerAgent(BaseAgent):
    def __init__(self):
        role = "producer"
        description = "Producer agent" # TODO: add description of task 
        self.tool = [ ]
        super().__init__(role, description)
    
    def produce(self, requirement:str) -> str:
        return