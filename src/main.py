from puzzle.puzzle_board import PuzzleBoard
from puzzle.search_result import SearchResult


# initial_state = 413268750
initial_state = 867254301
game = PuzzleBoard(initial_state, "bfs", None, "012345678")
results:SearchResult = game.solve()
print(results)