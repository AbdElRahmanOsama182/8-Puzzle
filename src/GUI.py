import streamlit as st
import time
import random
from puzzle.search_result import SearchResult
from puzzle.puzzle_board import PuzzleBoard  

def generate_random_state():
    base_state = list("123456780")  
    random.shuffle(base_state)  
    return ''.join(base_state)

def display_board_html(board):
    """Convert board list to HTML/CSS grid layout."""
    html = '<div class="puzzle-grid">'
    for idx, tile in enumerate(board):
        tile_class = "empty" if tile == '0' else "tile"
        html += f'<div class="{tile_class}" id="tile-{idx}">{tile if tile != "0" else ""}</div>'
    html += "</div>"
    return html

def apply_move(board, move):
    idx = board.index('0')
    row, col = divmod(idx, 3)

    if move == 'U' and row > 0:
        swap_idx = idx - 3
    elif move == 'D' and row < 2:
        swap_idx = idx + 3
    elif move == 'L' and col > 0:
        swap_idx = idx - 1
    elif move == 'R' and col < 2:
        swap_idx = idx + 1
    else:
        return board

    board[swap_idx], board[idx] = board[idx], board[swap_idx]
    return board

def reverse_move(move):
    """Reverse the move direction for backtracking."""
    return {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}.get(move, move)

st.set_page_config(page_title="8-Puzzle Solver", layout="wide", page_icon="🧩")
st.title("8-Puzzle Solver")
if "results" not in st.session_state:
    st.session_state.results = {
        "success": "",
        "runtime_duration": "",
        "nodes_expanded": "",
        "search_depth": "",
        "path_cost": ""
    }
_,input_col, puzzle_col, output_col,_ = st.columns([4, 6, 9, 6, 4]) 

with input_col:
    if st.button("Shuffle Puzzle", key="shuffle", help="Generate a new random puzzle!"):
        initial_state = generate_random_state()
        st.session_state.initial_state = initial_state 
        st.session_state.current_board = list(initial_state)  
    else:
        initial_state = st.session_state.get("initial_state", "410263758")  

    DEFAULT_GOAL_STATE="012345678"
    st.text_input("Enter initial state, from top-left to right-bottom, 10 characters, e.g. \"012345678\"", initial_state, key="initial_state")
    goal_state = st.text_input("Enter goal state", DEFAULT_GOAL_STATE)

    method = st.selectbox("Choose Algorithm", [
        "BFS", 
        "DFS", 
        "IDS", 
        "A* (Euclidean)", 
        "A* (Manhattan)"
    ])

    if st.button("Solve Puzzle", key="solve"):
        if ''.join(sorted(initial_state)) == DEFAULT_GOAL_STATE and ''.join(sorted(goal_state)) == DEFAULT_GOAL_STATE:
            heuristic = None
            if "A*" in method:  
                heuristic = "euclidean" if "Euclidean" in method else "manhattan"
                method = "A*"
            game = PuzzleBoard(initial_state, method.lower(), heuristic, goal_state)
            results: SearchResult = game.solve()

            st.session_state.results = {
                "success": results.success,
                "runtime_duration": str(round(results.runtime_duration, 2)) + " sec",
                "nodes_expanded": results.nodes_expanded,
                "search_depth": results.search_depth,
                "path_cost": results.path_cost
            }
            st.session_state.solution_path = results.path_to_goal
            st.session_state.path_index = 0
            st.session_state.current_board = list(initial_state)  
            st.session_state.animate = True  

with output_col:
    if "results" in st.session_state:
        output_col.markdown(
            """
            <div style='border-radius: 8px; padding: 20px;height:340px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>
                <h3 style='color: #4A90E2;'>Results</h3>
                <p><strong>Success</strong>: {}</p>
                <p><strong>Runtime Duration</strong>: {}</p>
                <p><strong>Nodes Expanded</strong>: {}</p>
                <p><strong>Search Depth</strong>: {}</p>
                <p><strong>Path Cost</strong>: {}</p>
            </div>
            """.format(
                st.session_state.results["success"],
                st.session_state.results["runtime_duration"],
                st.session_state.results["nodes_expanded"],
                st.session_state.results["search_depth"],
                st.session_state.results["path_cost"]
            ),
            unsafe_allow_html=True
        )

with puzzle_col:
    if "current_board" not in st.session_state:
        st.session_state.current_board = list(initial_state)  
    if "solution_path" not in st.session_state:
        st.session_state.solution_path = []
    if "path_index" not in st.session_state:
        st.session_state.path_index = 0  
    if "animate" not in st.session_state:
        st.session_state.animate = False  
        
    board_html = display_board_html(st.session_state.current_board)
    board_placeholder = st.empty()  
    board_placeholder.markdown(board_html, unsafe_allow_html=True)

    _,prev, next = st.columns([2,5,5])
    
    with prev:
        if st.button("◀ Prev", key="prev", help="Go to previous move"):
            if st.session_state.path_index > 0:
                st.session_state.path_index -= 1
                move = st.session_state.solution_path[st.session_state.path_index]
                reverse = reverse_move(move)
                st.session_state.current_board = apply_move(st.session_state.current_board, reverse)
                board_html = display_board_html(st.session_state.current_board)
                board_placeholder.markdown(board_html, unsafe_allow_html=True)

    with next:
        if st.button("Next ▶", key="next", help="Go to next move"):
            if st.session_state.path_index < len(st.session_state.solution_path):
                move = st.session_state.solution_path[st.session_state.path_index]
                st.session_state.current_board = apply_move(st.session_state.current_board, move)
                st.session_state.path_index += 1
                board_html = display_board_html(st.session_state.current_board)
                board_placeholder.markdown(board_html, unsafe_allow_html=True)

st.markdown("""
    <style>
    body {
        background-color: #f9f9f9;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    h1 {
        color: #4A90E2; /* Header color */
        text-align: center;
        font-size: 3em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    h2, h3 {
        color: #333;
    }
    .puzzle-grid {
        display: grid;
        grid-template-columns: repeat(3, 100px);
        gap: 10px;
        margin: 20px auto;
        justify-content: center;
    }
    .tile {
        width: 100px;
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #2196F3;  /* Tile color */
        color: white;
        font-size: 2em;
        border-radius: 8px;
        transition: transform 0.5s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .tile:hover {
        transform: scale(1.05);
    }
    .empty {
        width: 100px;
        height: 100px;
        background-color: transparent;
    }
    </style>
""", unsafe_allow_html=True)

if "solution_path" in st.session_state and st.session_state.animate:
    while st.session_state.path_index < len(st.session_state.solution_path):
        move = st.session_state.solution_path[st.session_state.path_index]
        st.session_state.current_board = apply_move(st.session_state.current_board, move)

        # Update the display
        board_html = display_board_html(st.session_state.current_board)
        board_placeholder.markdown(board_html, unsafe_allow_html=True)

        st.session_state.path_index += 1
        time.sleep(0.3) 

    st.session_state.animate = False  
