from heuristics.heuristic import Heuristic

class LinearConflict(Heuristic):
    def __init__(self, board_dim: int = 3):
        super().__init__(board_dim)

    def manhattan_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def linear_conflict(self, state, goal_state):

        conflict = 0
        # Row-wise Linear Conflict
        for row in range(self.board_dim):
            # get the tiles in the current row
            row_tiles = state[row * self.board_dim: row * self.board_dim + self.board_dim]
            # get the goal row indices of the tiles in the current row
            goal_row_indices = [goal_state.index(tile) // self.board_dim for tile in row_tiles]

            for i in range(len(goal_row_indices)):
                for j in range(i + 1, len(goal_row_indices)):
                    # check if the tiles are in the same row and the tiles are in the wrong order
                    if (goal_row_indices[i] == row and goal_row_indices[j] == row and 
                        goal_state.index(row_tiles[i]) > goal_state.index(row_tiles[j])):
                        conflict += 1

        # Column-wise Linear Conflict
        for col in range(self.board_dim):
            # get the tiles in the current column
            col_tiles = state[col::self.board_dim]
            # get the goal column indices of the tiles in the current column
            goal_col_indices = [goal_state.index(tile) % self.board_dim for tile in col_tiles]

            for i in range(len(goal_col_indices)):
                for j in range(i + 1, len(goal_col_indices)):
                    # check if the tiles are in the same column and the tiles are in the wrong order
                    if (goal_col_indices[i] == col and goal_col_indices[j] == col and 
                        goal_state.index(col_tiles[i]) > goal_state.index(col_tiles[j])):
                        conflict += 1
        # Multiply the linear conflict by 2 as it takes at least 2 moves to resolve a linear conflict
        return 2 * conflict  

    def heuristic(self, state, goal_state):

        sum_manhattan = 0
        for i in range(len(state)):
            # get the x and y coordinates of the current state and the goal state 
            x1, y1 = i // self.board_dim, i % self.board_dim
            x2, y2 = goal_state.index(state[i]) // self.board_dim, goal_state.index(state[i]) % self.board_dim
            # calculate the manhattan distance between the current state and the goal state
            sum_manhattan += self.manhattan_distance(x1, y1, x2, y2)
        # add the linear conflict to the manhattan distance
        sum_linear_conflict = self.linear_conflict(state, goal_state)
        return sum_manhattan + sum_linear_conflict
