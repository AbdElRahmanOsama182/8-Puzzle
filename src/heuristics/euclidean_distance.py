from heuristics.heuristic import Heuristic

class EuclideanDistance(Heuristic):
    def __init__(self, board_dim:int = 3):
        super().__init__(board_dim)

    def euclidean_distance(self, x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def heuristic(self, state, goal_state):
        sum = 0
        for i in range(len(state)):
            if state[i] == '1':
                continue
            # get the x and y coordinates of the current state and the goal state
            x1, y1 = i // self.board_dim, i % self.board_dim
            x2, y2 = goal_state.index(state[i]) // self.board_dim, goal_state.index(state[i]) % self.board_dim
            # calculate the euclidean distance between the current state and the goal state
            sum += self.euclidean_distance(x1, y1, x2, y2)
        return sum