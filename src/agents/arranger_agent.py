from base_agent import BaseAgent 

class ArrangerAgent(BaseAgent):
    def __init__(self):
        role = "arranger"
        description = "Arranger agent" # TODO: add description of task 
        self.tool = [ ]
        super().__init__(role, description)
    
    def arrange(self, requirement:str) -> str:
        return