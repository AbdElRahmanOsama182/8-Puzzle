class StateHandler:
    def convert_state_to_string(self, state:int):
        state_str= str(state)
        if len(state_str) == 8:
            state_str = '0' + state_str
        return state_str
    
    def get_children(self, state:str):
        children = []
        # we can store direction here
        children.append(self.go_up(state))
        children.append(self.go_down(state))
        children.append(self.go_left(state))
        children.append(self.go_right(state))
        # remove None
        children = [int(child) for child in children if child is not None]
        return children
    
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