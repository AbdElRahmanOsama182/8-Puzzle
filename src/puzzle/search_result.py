class SearchResult:
    def __init__(
        self, 
        success: bool = False, 
        runtime_duration: float = 0.0, 
        nodes_expanded: int = 0, 
        search_depth: int = 0, 
        path_to_goal = [], 
        path_cost: int = 0,
        states_to_goal = []
    ):
        self.success = success
        self.runtime_duration = runtime_duration
        self.nodes_expanded = nodes_expanded
        self.search_depth = search_depth
        self.path_to_goal = path_to_goal
        self.path_cost = path_cost
        self.states_to_goal = states_to_goal

    def __str__(self):
        return (f"SearchResult(\n"
                f"  Success: {self.success}\n"
                f"  Runtime Duration: {self.runtime_duration:.2f} seconds\n"
                f"  Nodes Expanded: {self.nodes_expanded}\n"
                f"  Search Depth: {self.search_depth}\n"
                f"  Path to Goal: {self.path_to_goal}\n"
                f"  Path Cost: {self.path_cost}\n"
                f"  States to Goal: {self.states_to_goal}\n"
                f")")