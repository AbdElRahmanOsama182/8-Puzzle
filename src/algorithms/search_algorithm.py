from puzzle.state_handler import StateHandler
class SearchAlgorithm:
    def __init__(self):
        self.GOAL_STATE= "012345678"
        self.state_handler=StateHandler()
        self.number_of_nodes_expanded = 0
        self.search_depth = 0
        self.path_to_goal = [] # list of U, D, L, R characters representing directions
        self.states_to_goal = [] # list of integers representing states

    def search(self, state:int):
        pass

    def is_goal(self,state:str):
        return state==self.GOAL_STATE
    
    def rebuild_path(self, parent:list):
        curr = int(self.GOAL_STATE)
        while parent[curr] != -1:
            self.states_to_goal.append(curr) # the goal state
            self.path_to_goal.append(parent[curr][1]) # the direction
            curr = parent[curr][0]
        self.states_to_goal.append(curr)
        self.path_to_goal.reverse()
        self.states_to_goal.reverse()

    def get_path_to_goal(self):
        return self.path_to_goal
    
    def get_states_to_goal(self):
        return self.states_to_goal

    def get_cost_to_goal(self):
        return len(self.path_to_goal)

    def get_number_of_nodes_expanded(self):
        return self.number_of_nodes_expanded

    def get_search_depth(self):
        return self.search_depth
