from dataclasses import dataclass

from typing import List
import numpy as np
import pandas as pd


class Doolhof:
    def __init__(self, matrix: List[List[int]], values: List[int], actions: List[int], endstates):
        self.matrix = matrix
        self.actions = actions
        self.states, self.states_matrix, self.inverted_states_matrix = self.create_states(matrix, values, endstates)

    def create_states(self, matrix: List[List[int]], values: List[int], endstates):
        if len(matrix) != 16:
            print("Your value list doesn't have exactly 16 items. This is a 4 x 4 matrix.")
            return None
        elif len(values) != 16:
            print("Your value list doesn't have exactly 16 items. This is a 4 x 4 matrix.")
            return None

        states = [State(matrix[location], values[location]) for location in range(len(matrix))]

        for location in endstates:
            for state in states:
                if state.location == location:
                    state.endstate()

        states_matrix = np.reshape(states, (4, 4))
        return states, states_matrix, states_matrix[::-1]

    def step(self, state, action: int):
        location = state.location
        if action == 0:
            new_y = location[1] + 1
            if new_y >= 4:
                return state
            else:
                return self.states_matrix[location[0]][new_y]

        elif action == 1:
            new_x = location[0] + 1
            if new_x >= 4:
                return state
            else:
                return self.states_matrix[new_x][location[1]]

        elif action == 2:
            new_y = location[1] - 1
            if new_y < 0:
                return state
            else:
                return self.states_matrix[location[0]][new_y]

        elif action == 3:
            new_x = location[0] - 1
            if new_x < 0:
                return state
            else:
                return self.states_matrix[new_x][location[1]]



@dataclass
class State:
    """Class for keeping track of a state."""
    location: list
    value: float
    checked: bool
    last_value: int

    def __init__(self, location: List[int], value: float):
        self.location = location
        self.value = value
        self.checked = False
        self.last_value = 0
        self.is_endstate = False

    def endstate(self):
        self.is_endstate = True


