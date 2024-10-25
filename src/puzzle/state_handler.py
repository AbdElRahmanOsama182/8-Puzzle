class StateHandler:
    def is_solvable(self,state:str):
        # TODO: implement is_solvable
        return True
    def increment_state(self, state:str):
        return ''.join([str(int(digit)+1) for digit in state])

    def convert_state_to_string(self, state:int):
        state_str= str(state)
        if len(state_str) == 8:
            state_str = '0' + state_str
        return state_str
    
    def get_children(self, state:str):
        children = []
        child = self.go_up(state)
        if child:
            children.append((child, 'U'))
        child = self.go_right(state)
        if child:
            children.append((child, 'R'))
        child = self.go_down(state)
        if child:
            children.append((child, 'D'))
        child = self.go_left(state)
        if child:
            children.append((child, 'L'))
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