from Inleveropdracht_1.doolhof import Doolhof
from Inleveropdracht_1.agent import Agent
from Inleveropdracht_1.policy import Policy


matrix = []
for i in range(0, 4):
    for j in range(0, 4):
        matrix.append([i, j])

rewards = [-1, -1, -1, 40,
          -1, -1, -10, -10,
          -1, -1, -1, -1,
          10, -2, -1, -1
]

values = [0 for i in range(len(rewards))]

actions = [0, 1, 2, 3]

endstates = [[0, 0], [3, 3]]

omgeving = Doolhof(matrix, values, actions, endstates)

gamma = 1

delta = 0.1

policy = Policy(omgeving, rewards, gamma)

agent = Agent(omgeving, policy, [0, 1], gamma, delta)

# print(policy.value_matrix)
print(agent.value_iteration())

