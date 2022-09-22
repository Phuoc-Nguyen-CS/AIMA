from search import *


class WolfGoatCabbage(Problem):
    def __init__(self, initial=('F', 'G', 'W', 'C'), goal=()):
        super().__init__(initial, goal)

    def goal_test(self, state):
        return state == self.goal

    def actions(self, state):
        possible_actions = {'F'}

        if self.goat_eats_cabbage():
            possible_actions.add('G')
        if self.wolf_eats_goat():
            possible_actions.add('G')
        print(possible_actions)
        return possible_actions

    def results(self, state, action):
        """Given a state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state"""
        pass


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
