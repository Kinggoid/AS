from Inleveropdracht_1.doolhof import Doolhof
from Inleveropdracht_1.policy import Policy

import random


class Agent:
    def __init__(self, maze, policy, location, gamma, delta):
        self.maze = maze
        self.location = location
        self.values = self.init_values()
        self.gamma = gamma
        self.delta = delta
        self.policy = policy

    def init_values(self):
        return [0 for location in self.maze.values]

    def delta_check(self):
        for state in self.maze.states:
            if self.check_difference(state) > self.delta:
                return False
        return True

    def check_difference(self, state):
        new_value = abs(state.new_value)
        value = abs(state.value)
        return abs(new_value - value)

    def get_action(self, state):
        actions = Policy.select_action(self.policy, state)
        return random.choice(actions)

    def value_iteration(self):
        k = 1  # Amount of iterations
        while True:
            print('Iteration ' + str(k))
            for state in self.maze.states:
                action = self.get_action(state)

            if self.delta_check():
                break

            print('These are the new values of the matrix after the value iteration.')
            self.nieuwe_value_matrix()

            print('\n')

            print('These are the new policies after the value iteration.')
            self.print_policies()

            k += 1

            print('\n')

    def print_policies(self):
        for i in self.policy.policies[::-1]:
            row = []
            for j in i:
                row.append(j)
            print(row)

    def nieuwe_value_matrix(self):
        values = []
        for i in self.maze.states_matrix[::-1]:
            row = []
            for j in i:
                row.append(j.new_value)
                j.value = j.new_value
            print(row)
            values.append(row)
        return values



