# BaseAgent class for all agents 

class BaseAgent:
    def __init__(self, role: str, description: str): 
        self.role = role 
        self.description = description 
        self.tool = [ ]