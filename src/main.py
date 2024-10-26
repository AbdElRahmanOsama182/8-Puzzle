from puzzle.puzzle_board import PuzzleBoard
from puzzle.search_result import SearchResult


# initial_state = "768452103"
initial_state = "410263758"
# game = PuzzleBoard("410263758", "a_star", "euclidean")
# game = PuzzleBoard(initial_state, "iterative_dfs", None, "123456789")
game = PuzzleBoard(initial_state, "bfs", None, "012345678")
# game = PuzzleBoard(initial_state, "bfs", None, "123456789")
results:SearchResult = game.solve()
print(results)