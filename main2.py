from operator import contains
from search import *


class WolfGoatCabbage(Problem):
    """Represent the state by a set of characters, representing the objects on the left bank.
       Use the characters: ‘F’, ‘G’, ‘W’, ‘C’. Note that it is sufficient to represent the objects on one bank
       since the remaining will be on the other bank.
       E.g., {‘F’, ‘G’} represents Farmer and Goat on the left bank and Wolf and Cabbage on the right """

    initialState = ('W', 'G', 'C', 'F')
    goalState = ()

    def __init__(self, initial=initialState, goal=goalState):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

    # The First move is always going to be [G]oat
    def first_move(self, state):
        if 'F' in state and 'G' in state and 'C' in state and 'W' in state:
            return True
        return False

    # All the scenarios where [G]oat will eat the [C]abbage if [F]armer leaves
    def goat_eats_cabbage(self, state):
        if (('F' in state and 'W' and 'C' in state) or
                ('F' not in state and 'W' not in state and 'C' not in state)):
            return True
        return False

    # All the scenarios where [W]olf will eat the [G]oat if [F]armer leaves
    def wolf_eats_goat(self, state):
        if (('F' in state and 'W' and 'G' in state) or
                ('F' not in state and 'W' not in state and 'G' not in state)):
            return True
        return False

    def wolf_cabbage(self, state):
        if (('F' in state and 'W' in state and 'C' in state and 'G' not in state) or
                ('G' in state and 'F' not in state and 'W' not in state and 'C' not in state)):
            return True
        return False

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
            The result would be a list, since there are only four possible actions
            in any given state of the environment """
        possible_actions = ['W', 'G', 'C', 'F']

        # The First move will always require the G to be moved
        # ['G','F]
        if self.first_move(state):
            # possible_actions.remove('W')
            # possible_actions.remove('C')
            print("1")
            print(" Before POSSIBLE ACTIONS --> ", possible_actions)
            # possible_actions.remove('G')
            # possible_actions.remove('F')
            possible_actions = ['W', '1', 'C', '2']
            print(" After POSSIBLE ACTIONS --> ", possible_actions)

        # If [G]oat Eats Cabbage
        elif self.goat_eats_cabbage(state):
            # If [W]olf does not eat Goat
            if not self.wolf_eats_goat(state):
                # We can safely move [C]abbage
                # ['C', 'F']
                # possible_actions.remove('G')
                # possible_actions.remove('W')
                print("2")
                possible_actions.remove('C')
                possible_actions.remove('F')
            # We have to move [G]oat as it will either:
            # 1. Be eaten by the [W]olf
            # 2. Eat the [C]abbage
            # ['G', 'F']
            else:
                # possible_actions.remove('W')
                # possible_actions.remove('C')
                print("3")
                possible_actions.remove('G')
                possible_actions.remove('F')
        # If [W]olf eats Goat
        elif self.wolf_eats_goat(state):
            # If [G]oat does not eat [C]abbage
            # ['W', 'F']
            if not self.goat_eats_cabbage():
                # possible_actions.remove('G')
                # possible_actions.remove('C')
                print("4")
                possible_actions.remove('F')
                possible_actions.remove('W')
            else:
                # possible_actions.remove('G')
                print("5")
                possible_actions.remove('G')
                possible_actions.remove('F')
        # Else only farmer moves
        else:
            # possible_actions.remove('G')
            # possible_actions.remove('W')
            # possible_actions.remove('C')
            print("6")
            possible_actions.remove('F')

        print(" POSSIBLE ACTIONS --> ", possible_actions)
        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        if contains(state, 'F'):
            print("Farmer on left bank")

            # print(type(state), " --> :", state)
            # print(type(action), " -->", action)
            # print("State: ", state)
            # print("Action: ", action)
            print("Before: ", state)
            print("Before: ", action)
            new_state = set(state) ^ set(action)
            print("After: ", new_state)
            print("After: ", action)
            return tuple(new_state)
        else:
            print("Farmer on right bank")
            # print("State: ", state)
            # print("Action: ", action)
            new_state = set(state) | set(action)
            # print(new_state)
            return tuple(new_state)


def goal_test(self, state):
    """ Given a state, return True if state is a goal state or False, otherwise """
    return state == self.goal


def contains(tuple, given_char):
    if given_char in tuple:
        return True
    return False


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
