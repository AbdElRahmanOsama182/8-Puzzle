from puzzle.puzzle_board import PuzzleBoard
from puzzle.search_result import SearchResult


initial_state = "413268750"
# initial_state = "867254301"
# game = PuzzleBoard("410263758", "a_star", "euclidean")
game = PuzzleBoard(initial_state, "dfs", None, "123456789")
results:SearchResult = game.solve()
print(results)