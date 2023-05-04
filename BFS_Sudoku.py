from queue import Queue
import copy
import time

class Problem(object):
    def __init__(self, initial):
        self.initial = initial
        self.size = len(initial) # Size of a grid
        self.height = int(self.size/3) # Size of a quadrant

    # Return set of valid numbers from values that do not appear in used
    def filter_values(self, values, used):
      valid_values = []
      for number in values:
        if number not in used:
            valid_values.append(number)
      return valid_values

    # Return first empty spot on grid (marked with 0)
    def get_spot(self, board, state):
        for row in range(board):
            for column in range(board):
                if state[row][column] == 0:
                    return row, column   

    def actions(self, state):
      number_set = set(range(1, self.size + 1)) # Defines set of valid numbers that can be placed on board
      row, column = self.get_spot(self.size, state) # Get first empty spot on board

      # Filter valid values based on row
      in_row = set()

      for number in state[row]:
        if number != 0:
          in_row.add(number)
          
      options = number_set - in_row

      # Filter valid values based on column
      in_column = set()

      for column_index in range(self.size):
        cell_value = state[column_index][column]
        if cell_value != 0:
          in_column.add(cell_value)

      options = options - in_column

      # Filter with valid values based on quadrant
      row_start = (row // self.height) * self.height
      column_start = (column // 3) * 3

      in_block = set()

      for block_row in range(self.height):
        for block_column in range(3):
          cell_value = state[row_start + block_row][column_start + block_column]
          if cell_value != 0:
            in_block.add(cell_value)
            
      options = options - in_block

      for number in options:
        yield number, row, column

   # Returns updated board after adding new valid value
    def result(self, state, action):
      
        play = action[0]
        row = action[1]
        column = action[2]

        # Add new valid value to board
        new_state = copy.deepcopy(state)
        new_state[row][column] = play

        return new_state
      
    # Use sums of each row, column and quadrant to determine validity of board state
    def check_legal(self, state):
      # Calculate the expected sum of each row, column, and quadrant.
      total = sum(range(1, self.size+1))
  
      # Check each row and column to make sure it has the expected total.
      for i in range(self.size):
          if len(state[i]) != self.size or sum(state[i]) != total:
              return False
  
          if sum(state[j][i] for j in range(self.size)) != total:
              return False
  
      # Check each quadrant to make sure it has the expected total.
      for i in range(0, self.size, self.height):
          for j in range(0, self.size, 3):
              if sum(state[r][c] for r in range(i, i+self.height)
                     for c in range(j, j+3)) != total:
                  return False
  
      # If all checks passed, the state is legal.
      return True


class Node:
    def __init__(self, state, action=None):
        """
        Initializes a new Node instance with a given state and optional action.
        """
        self.state = state
        self.action = action

    def expand(self, problem):
        """
        Returns a list of child nodes obtained by applying each possible action to the current node.
        """
        return [self.child_node(problem, action) for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """
        Returns a new child Node instance with the state resulting from applying the given action to the current state.
        """
        next_state = problem.result(self.state, action)
        return Node(next_state, action)

def BFS(problem):
    # Create initial node of problem tree holding original board
    node = Node(problem.initial)
    # Check if original board is correct and immediately return if valid
    if problem.check_legal(node.state):
        return node, 0

    frontier = Queue()
    frontier.put(node)

    explored = 0  # initialize explored counter
  
    # Loop until all nodes are explored or solution found
    while (frontier.qsize() != 0):
        explored += 1  # increment explored counter
        node = frontier.get()
      
        for child in node.expand(problem):
            if problem.check_legal(child.state):
                return child, explored
            frontier.put(child)

    return None, explored  # return None if no solution found


def BFS_solve(board):
    print ("\nSolving with BFS...")

    start_time = time.time()

    problem = Problem(board)
    solution, explored = BFS(problem)  # update to return explored taken
    elapsed_time = (time.time() - start_time) * 1000 # convert to milisecond 

    if solution:
        print ("Found solution")
        for row in solution.state:
            print (row)
        print("Number of nodes explored: " + str(explored))  # print number of explored
    else:
        print ("No possible solutions")

    if (elapsed_time > 1000):
        print ("Elapsed time: {:.6f} seconds".format(elapsed_time / 1000))
    else:
        print ("Elapsed time: {:.6f} ms".format(elapsed_time))

