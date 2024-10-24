from state_handler import StateHandler
class SearchAlgorithm:
    def __init__(self):
        self.GOAL_STATE= "012345678"
        self.state_handler=StateHandler()

    def search(self, state:int):
        pass

    def is_goal(self,state:str):
        return state==self.GOAL_STATE

    def is_solvable(self,state:str):
        pass
    
    def get_path_to_goal(self):
        pass

    def get_cost_to_goal(self):
        pass

    def get_number_of_nodes_expanded(self):
        pass

    def get_search_depth(self):
        pass
