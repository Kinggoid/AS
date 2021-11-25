from Inleveropdracht_1.doolhof import Doolhof

from typing import List
import numpy as np
import random


class Policy:
    def __init__(self, maze: Doolhof, values: List[int], gamma: int):
        self.maze = maze
        self.values = values
        self.value_matrix = np.reshape(values, (4, 4))[::-1]
        self.gamma = gamma
        self.policies = self.create_policy_grid()

    def create_policy_grid(self):
        policy_grid = []
        for state in self.maze.states:
            if not state.is_endstate:
                policy_grid.append(['→, ←, ↑, ↓'])
            else:
                policy_grid.append([None])
        return np.reshape(policy_grid, (4, 4))

    def get_surrounding_states(self, state):
        surrounding_states = []
        for direction in range(0, 4):
            surrounding_states.append(Doolhof.step(self.maze, state, direction))
        return [i for i in surrounding_states if i.location != state.location]

    def bellman_equation(self, state):
        reward = self.value_matrix[state.location[0]][state.location[1]]
        value = state.value
        print(state)
        print(reward)
        print(value)

        equation = reward + value * self.gamma

        print(equation)

        state.last_value = value
        state.value = equation

        return equation

    def select_action(self, origional_state):
        if origional_state.is_endstate:
            return [[None]]

        surrounding_states = self.get_surrounding_states(origional_state)
        value_surrounding_state = [self.bellman_equation(surrounding_state) for surrounding_state in surrounding_states]

        # print(origional_state)
        # print(surrounding_states)
        # print(value_surrounding_state)
        # print('+++++')

        max_value = max(value_surrounding_state)
        max_value_states = []
        for state in range(len(value_surrounding_state)):
            if value_surrounding_state[state] == max_value:
                difference = np.subtract(surrounding_states[state].location, origional_state.location)

                if np.array_equal(difference, [0, 0]):
                    max_value_states.append('Itself')
                elif np.array_equal(difference, [1, 0]):
                    max_value_states.append('↓')
                elif np.array_equal(difference, [0, 1]):
                    max_value_states.append('←')
                elif np.array_equal(difference, [-1, 0]):
                    max_value_states.append('↑')
                elif np.array_equal(difference, [0, -1]):
                    max_value_states.append('→')

        self.policies[origional_state.location[0]][origional_state.location[1]] = max_value_states
        return max_value_states

    # def test(self):
    #     state = self.maze.states_matrix[3][3]
    #     return self.select_action(state)


# →, ←, ↑, ↓
