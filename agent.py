from dataclasses import dataclass

from Inleveropdracht_1.doolhof import Maze
from Inleveropdracht_1.policy import Policy

import random
from typing import List


class Agent:
    def __init__(self, maze: Maze, policy: Policy, location: List[int], delta: float):
        self.maze = maze  # Our maze
        self.location = location  # Location of the agent
        self.delta = delta  # A number to indicate how little the difference between two value iterations has to be
        # in order for the iterations to stop
        self.policy = policy  # Our policy

    def check_difference_in_number(self, state):
        """Check the difference between two numbers."""
        new_value = abs(state.new_value)
        value = abs(state.value)
        return abs(new_value - value)

    def delta_check(self):
        """Check whether any states have changes since the last iteration."""
        for state in self.maze.states:
            if self.check_difference_in_number(state) > self.delta:
                return False
        return True

    def print_policies(self):
        """Print the current policies of our value iteration."""
        for i in self.policy.policies[::-1]:
            row = []
            for j in i:
                row.append(j)
            print(row)

    def nieuwe_value_matrix(self):
        """Print the current values of our value iteration."""
        values = []
        for i in self.maze.states_matrix[::-1]:
            row = []
            for j in i:
                row.append(j.new_value)
                j.value = j.new_value  # Update the values of the states to their new values
            print(row)
            values.append(row)
        return values

    def value_iteration(self):
        """The value iteration main loop."""
        k = 1  # Amount of iterations

        while True:
            print('Iteration ' + str(k))
            k += 1

            for state in self.maze.states:  # For every state
                if state.is_endstate:  # If a state is an endstate, we ignore it. Their value cannot go up.
                    continue

                surrounding_states = Policy.get_surrounding_states(self.policy, state)  # Get surrounding states

                value_surrounding_states = []  # Get the value of these surrounding states
                for surrounding_state in surrounding_states:
                    value_surrounding_states.append(Policy.bellman_equation(self.policy, surrounding_state))

                # Update the policies and get the best value of this best action
                new_value = Policy.select_action(self.policy, state, surrounding_states, value_surrounding_states)

                # The state's new value is the value of his best choice (value iteration)
                state.new_value = new_value

            if self.delta_check():  # The value iteration has come to a stop
                print('These are the new values of the matrix after the value iteration.')
                self.nieuwe_value_matrix()

                print('\n')

                print('These are the new policies after the value iteration.')
                self.print_policies()
                break

            print('These are the new values of the matrix after the value iteration.')
            self.nieuwe_value_matrix()

            print('\n')

            print('These are the new policies after the value iteration.')
            self.print_policies()

            print('\n')

    def agent_path(self):
        """Simulate an agent going through the maze and taking the value iterations best path."""
        k = 1  # How many steps are necesarry for the Agent to find the endstate

        while True:
            k += 1
            policy = self.policy.policies[self.location[1]][self.location[0]]  # Find the policy
            self.location = self.maze.step(self.location, random.choice(policy))  # Find hte coordinates of our next location
            print('The agent is currently on coördinates: ' + str(self.location))

            state = self.maze.states_matrix[self.location[0]][self.location[1]]  # Our next state

            if state.is_endstate:  # If we land on an endstate, we stop the simulation
                break

        print("..." + str(k) + " steps for the agent to get to the endstate.")
