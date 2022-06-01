import constants as c
from game import Game
import helper
import queue
import numpy as np
import time
from tqdm import tqdm


class BFSAgent:
    def __init__(self):
        # self.env = env
        # self.start_state = [self.env.get_state(), 0, []]

        # self.neighbors_states = []
        # self.neighbors_actions = []
        # self.end_value = end_value
        # self.parent = game.get_state()

        # self.states_queue = self.search_action(self.start_state, 4)
        pass

    def get_neighbors(self, state):
        depth = state[1]
        action_parent = state[2]
        neighbors_states = []
        actions = [c.KEY_LEFT_ALT, c.KEY_RIGHT_ALT, c.KEY_UP_ALT, c.KEY_DOWN_ALT]
        neighbors = [helper.left(state[0])[0], helper.right(state[0])[0], helper.up(state[0])[0], helper.down(state[0])[0]]
        checks = [helper.left(state[0])[1], helper.right(state[0])[1], helper.up(state[0])[1], helper.down(state[0])[1]]
        for i, value in enumerate(checks):
            if value:
                neighbors_states.append([neighbors[i], depth + 1, action_parent + [actions[i]]])
        return neighbors_states

# # Consider max_value and sum   
#     def evaluate(self, final_states):
#         max = 0
#         max_values = [np.max(item[0]) for item in final_states]
#         sum_states = [np.sum(item[0]) for item in final_states]
#         try:
#             max_value = np.max(max_values)
#         except ValueError: 
#             pass
        
#         indexs_max = [i for i, j in enumerate(max_values) if j == max_value]
#         max_index = indexs_max[0]
#         for i in indexs_max:
#             if sum_states[i] >= max:
#                 max = sum_states[i]
#                 max_index = i
 
#         return final_states[max_index][2]

# # Consider max_value  
#     def evaluate(self, final_states):
#         max_index = 0
#         max_values = [np.max(item[0]) for item in final_states]
#         try:
#             max_value = np.max(max_values)
#         except ValueError: 
#             pass
#         for i, value in enumerate(max_values):
#             if value == max_value:
#                 max_index = i
#                 break

#         return final_states[max_index][2]

# Consider max_sum  
    def evaluate(self, final_states):
        max_index = 0
        sum_states = [np.sum(item[0]) for item in final_states]
        try:
            max_value = np.max(sum_states)
        except ValueError: 
            pass
        for i, value in enumerate(sum_states):
            if value == max_value:
                max_index = i
                break

        return final_states[max_index][2]

    # MAIN ALGORITHM
    def search_action(self, start_state, end_depth):
        '''Find the next action
        # parameters: 
        start_state: current state ([matrix, depth, action]): matrix: array, depth: int, action: array
        end_depth: configure how many depth which the agent needs to look for before deciding the best action for current state.
        # return:
        action: the next action for current state
        '''
        states_queue = []
        final_states = []
        visited_states = []
        states_queue.append(start_state)

        while states_queue:
            state = states_queue.pop(0)
            depth = state[1]
            if depth >= end_depth:
                final_states.append(state)
                continue
            neighbors_states = self.get_neighbors(state)
            states_queue += neighbors_states
            visited_states.append(state)
        if len(final_states) == 0:
            depths = [item[1] for item in visited_states]
            max_depth = np.max(depths)
            final_states = [item[0] for item in visited_states if item[1] == max_depth]
        action = self.evaluate(final_states)
        return action

# commands = {c.KEY_UP_ALT: helper.up, c.KEY_DOWN_ALT: helper.down,
#                     c.KEY_LEFT_ALT: helper.left, c.KEY_RIGHT_ALT: helper.right}
# max_values = []
# for i in tqdm(range(100), desc="Loading..."):
#     environment = Game()
#     agent = BFSAgent()
#     status = "not over'"
#     while status != "lose":
#         current_state = environment.get_state()
#         status = helper.game_state(current_state)
#         state = [current_state, 0, []]
#         action = agent.search_action(state, 2)[0] #depth = 6
#         temp_state, done, _ = environment.give_action(action)
        
#         if done:
#             continue
#         else:
#             for move in commands.keys():
#                 temp_state, done, _ = environment.give_action(move)
#                 if done:
#                     break
        
#     max_value =  np.max(environment.get_state())  
#     max_values.append(max_value)
#     print(f"Maximum value for epoch {i}: " + str(max_value))
# print("Average maximum score: ", np.average(max_values))

    
    
