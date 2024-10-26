from puzzle.puzzle_board import PuzzleBoard
from puzzle.search_result import SearchResult


initial_state = "273560841"
# initial_state = "410263758"
# game = PuzzleBoard("410263758", "a_star", "euclidean")
# game = PuzzleBoard(initial_state, "iterative_dfs", None, "012345678")
game = PuzzleBoard(initial_state, "bfs", None, "123456780")
# game = PuzzleBoard(initial_state, "bfs", None, "012345678")
results:SearchResult = game.solve()
print(results)