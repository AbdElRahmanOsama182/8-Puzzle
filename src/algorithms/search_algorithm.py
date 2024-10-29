from puzzle.state_handler import StateHandler
class SearchAlgorithm:
    def __init__(self, goal_state:str="123456789"):
        self.goal_state= goal_state
        self.state_handler=StateHandler(goal_state)
        self.number_of_nodes_expanded = 0
        self.search_depth = 0
        self.path_to_goal = [] # list of U, D, L, R characters representing directions
        self.states_to_goal = [] # list of integers representing states
        self.running_time = 0.0

    def search(self, state:str):
        pass

    def is_goal(self,state:str):
        return state==self.goal_state
    
    def rebuild_path(self, parent:list):
        # rebuild the path to the goal state from the parent dictionary
        curr = int(self.goal_state)
        while parent[curr] != -1:
            self.states_to_goal.append(curr) # the goal state
            # the direction
            self.path_to_goal.append(self.state_handler.get_transition(str(parent[curr]), str(curr)))
            curr = parent[curr]
            
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
    
    def get_running_time(self):
        return self.running_time