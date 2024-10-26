class StateHandler:
    def __init__(self, goal_state:str = "123456789"):
        self.goal_state = goal_state

    def is_solvable(self,state:str):
        x = self.count_inversions(state) % 2
        y = self.count_inversions(self.goal_state) % 2
        return x == y
    
    def get_children(self, state:str):
        children = []
        child = self.go_up(state)
        if child:
            children.append((int(child), 'U'))
        child = self.go_right(state)
        if child:
            children.append((int(child), 'R'))
        child = self.go_down(state)
        if child:
            children.append((int(child), 'D'))
        child = self.go_left(state)
        if child:
            children.append((int(child), 'L'))
        return children
    
    def go_up(self, state:str):
        one_pos = state.index('1')
        if one_pos >= 3:
            return self.swap(state, one_pos, one_pos-3)
        else:
            return None

    def go_down(self, state:str):
        one_pos = state.index('1')
        if one_pos <= 5:
            return self.swap(state, one_pos, one_pos+3)
        else:
            return None

    def go_left(self, state:str):
        one_pos = state.index('1')
        if one_pos % 3 != 0:
            return self.swap(state, one_pos, one_pos-1)
        else:
            return None

    def go_right(self, state:str):
        one_pos = state.index('1')
        if one_pos % 3 != 2:
            return self.swap(state, one_pos, one_pos+1)
        else:
            return None

    def swap(self, state: str, pos1: int, pos2: int):
        state_list = list(state)
        state_list[pos1], state_list[pos2] = state_list[pos2], state_list[pos1]
        return ''.join(state_list)
    
    def set_goal_state(self, goal_state:str):
        self.goal_state = goal_state

    def count_inversions(self, state:str):
        inv_cnt = 0
        for i in range(len(state)-1):
            if state[i] == '1':
                continue
            for j in range(i+1,len(state)):
                if state[j] != '1' and int(state[i])>int(state[j]):
                    inv_cnt+=1
        return inv_cnt
    
    def increment_state(self, state:str):
        return ''.join([str(int(digit)+1) for digit in state])
