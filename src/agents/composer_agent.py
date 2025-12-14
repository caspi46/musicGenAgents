from base_agent import BaseAgent 

class ComposerAgent(BaseAgent):
    def __init__(self):
        role = "composer" 
        description = "Composer agent" # TODO: add description of task 
        self.tool = [ ]
        super().__init__(role, description)
    
    def compose(self, requirement:str) -> str:
        return