from puzzle.puzzle_board import PuzzleBoard
from puzzle.search_result import SearchResult


# initial_state = [7, 6, 8, 4, 5, 2, 1, 0, 3]
initial_state = 768452103
game = PuzzleBoard(initial_state, "bfs")
results:SearchResult = game.solve()
print(results)