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
        last_value = abs(state.last_value)
        value = abs(state.value)
        return abs(last_value - value)

    def get_action(self, state):
        actions = Policy.select_action(self.policy, state)
        return random.choice(actions)

    def value_iteration(self):
        print('hello')
        k = 1
        while self.delta_check():
            print('Iteration ' + str(k))
            for state in self.maze.states:
                action = self.get_action(state)

            for i in self.policy.policies[::-1]:
                row = []
                for j in i:
                    row.append(j)
                print(row)

            self.nieuwe_value_matrix()

            if k == 2:
                break

            k += 1

            print('\n')

    def nieuwe_value_matrix(self):
        values = []
        for i in self.maze.states_matrix[::-1]:
            row = []
            for j in i:
                row.append(j.value)
            values.append(row)
            print(row)

        return values



