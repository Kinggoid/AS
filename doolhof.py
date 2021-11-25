from dataclasses import dataclass

from typing import List
import numpy as np


class Maze:
    def __init__(self, matrix: List[List[int]], values: List[int], actions: List[int], endstates):
        self.matrix = matrix  # List of coördinates in the grid
        self.values = values  # List of 16 zero's as inital values for the states
        self.actions = actions  # Possible actions
        self.states = self.create_states(matrix, values, endstates)  # The states
        self.states_matrix = np.reshape(self.states, (4, 4))  # The states but in a 4 x 4 grid

    def create_states(self, matrix: List[List[int]], values: List[int], endstates: List[List[int]]):
        """
        We create our states. For every location in the grid, we create a state.
        """
        if len(matrix) != 16:
            print("Your value list doesn't have exactly 16 items. This is a 4 x 4 matrix.")
            return None
        elif len(values) != 16:
            print("Your value list doesn't have exactly 16 items. This is a 4 x 4 matrix.")
            return None

        # Create states
        states = [State(matrix[location], values[location]) for location in range(len(matrix))]

        # Give the states which are endstates, an endstate status
        for location in endstates:
            for state in states:
                if state.location == location:
                    state.endstate()
        return states

    def step(self, state, action: int):
        """
        Given a state and an action return the state you would encounter if you took that action. If you try and step
        outside of the grid, return the original state.
        """
        location = state.location
        if action == 0:  # Go one step to the top
            new_y = location[1] + 1
            if new_y >= 4:
                return state
            else:
                return self.states_matrix[location[0]][new_y]

        elif action == 1:  # Go one step to the right
            new_x = location[0] + 1
            if new_x >= 4:
                return state
            else:
                return self.states_matrix[new_x][location[1]]

        elif action == 2:  # Go one step to the bottom
            new_y = location[1] - 1
            if new_y < 0:
                return state
            else:
                return self.states_matrix[location[0]][new_y]

        elif action == 3:  # Go one step to the left
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
    new_value: int

    def __init__(self, location: List[int], value: float):
        self.location = location
        self.value = value
        self.checked = False
        self.new_value = 0
        self.is_endstate = False

    def endstate(self):
        """
        Give the state an endstate status.
        """
        self.is_endstate = True


