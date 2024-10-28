class StateHandler:
    # This class is responsible for handling the state of the puzzle
    def __init__(self, goal_state:str = "123456789"):
        self.goal_state = goal_state

    # check if the state is solvable by comparing the number of inversions
    def is_solvable(self,state:str):
        x = self.count_inversions(state) % 2
        y = self.count_inversions(self.goal_state) % 2
        return x == y

    # get the children of the state
    def get_children(self, state:str):
        children = []
        child = self.go_up(state)
        if child:
            children.append(int(child))
        child = self.go_right(state)
        if child:
            children.append(int(child))
        child = self.go_down(state)
        if child:
            children.append(int(child))
        child = self.go_left(state)
        if child:
            children.append(int(child))
        return children
    
    # move the blank space up
    def go_up(self, state:str):
        one_pos = state.index('1')
        if one_pos >= 3:
            return self.swap(state, one_pos, one_pos-3)
        else:
            return None

    # move the blank space down
    def go_down(self, state:str):
        one_pos = state.index('1')
        if one_pos <= 5:
            return self.swap(state, one_pos, one_pos+3)
        else:
            return None

    # move the blank space left
    def go_left(self, state:str):
        one_pos = state.index('1')
        if one_pos % 3 != 0:
            return self.swap(state, one_pos, one_pos-1)
        else:
            return None

    # move the blank space right
    def go_right(self, state:str):
        one_pos = state.index('1')
        if one_pos % 3 != 2:
            return self.swap(state, one_pos, one_pos+1)
        else:
            return None

    # Get the Direction of the transition
    def get_transition(self, from_value:str, to_value:str):
        if self.go_right(from_value)==to_value:
            return 'R'
        elif self.go_left(from_value) == to_value:
            return 'L'
        elif self.go_up(from_value) == to_value:
            return 'U'
        elif self.go_down(from_value) == to_value:
            return 'D'

    # swap two positions in the state
    def swap(self, state: str, pos1: int, pos2: int):
        state_list = list(state)
        state_list[pos1], state_list[pos2] = state_list[pos2], state_list[pos1]
        return ''.join(state_list)
    
    def set_goal_state(self, goal_state:str):
        self.goal_state = goal_state

    # count the number of inversions in the state
    def count_inversions(self, state:str):
        inv_cnt = 0
        for i in range(len(state)-1):
            if state[i] == '1':
                continue
            for j in range(i+1,len(state)):
                if state[j] != '1' and int(state[i])>int(state[j]):
                    inv_cnt+=1
        return inv_cnt
    
    # Make the state 1-based 
    def increment_state(self, state:str):
        return ''.join([str(int(digit)+1) for digit in state])
