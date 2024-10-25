class StateHandler:
    def __init__(self, goal_state:str = "012345678"):
        self.goal_state = goal_state

    def is_solvable(self,state:int):
        x = self.count_inversions(self.convert_state_to_string(state)) % 2
        y = self.count_inversions(self.goal_state) % 2
        return x == y

    def convert_state_to_string(self, state:int):
        state_str= str(state)
        if len(state_str) == 8:
            state_str = '0' + state_str
        return state_str
    
    def get_children(self, state:str):
        children = []
        # we can store direction here
        children.append( (self.go_up(state), 'U') )
        children.append( (self.go_down(state), 'D') )
        children.append( (self.go_left(state), 'L') )
        children.append( (self.go_right(state), 'R') )
        new_children = []
        for child, dir in children:
            if child is not None:
                new_children.append((int(child), dir))
        return new_children
    
    def go_up(self, state:str):
        zero_pos = state.index('0')
        if zero_pos >= 3:
            return self.swap(state, zero_pos, zero_pos-3)
        else:
            return None

    def go_down(self, state:str):
        zero_pos = state.index('0')
        if zero_pos <= 5:
            return self.swap(state, zero_pos, zero_pos+3)
        else:
            return None

    def go_left(self, state:str):
        zero_pos = state.index('0')
        if zero_pos % 3 != 0:
            return self.swap(state, zero_pos, zero_pos-1)
        else:
            return None

    def go_right(self, state:str):
        zero_pos = state.index('0')
        if zero_pos % 3 != 2:
            return self.swap(state, zero_pos, zero_pos+1)
        else:
            return None

    def swap(self, state: str, pos1: int, pos2: int):
        state_list = list(state)
        state_list[pos1], state_list[pos2] = state_list[pos2], state_list[pos1]
        return ''.join(state_list)
    
    def count_inversions(self, state:str):
        inv_cnt = 0
        for i in range(len(state)-1):
            if state[i] == '0':
                continue
            for j in range(i+1,len(state)):
                if state[j] != '0' and int(state[i])>int(state[j]):
                    inv_cnt+=1
        return inv_cnt