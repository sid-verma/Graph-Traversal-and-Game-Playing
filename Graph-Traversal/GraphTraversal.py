
# Defining the goal state
goal_items = [1, 2, 3, 8, 0, 4, 7, 6, 5]
visited_vertices = []
# Defining imput states with increasing levels of difficulty
easy_initial_state = [1, 3, 4, 8, 6, 2, 7, 0, 5]
medium_initial_state = [2, 8, 1, 0, 4, 3, 7, 6, 5]
hard_initial_state = [5, 6, 7, 4, 0, 8, 3, 2, 1]
max = 0

import sys
import time

'''Defining a class vertex with the following attributes:
vertex.items is the current state of the elements of 8-puzzle in the vertex
vertex.ancestor is the ancestor of the vertex
vertex.operator is the decision to move the null "0" element in the 8-puzzle
vertex.depth is the depth level of the vertex'''
class vertex:
  def __init__( self, items, ancestor, operator, depth, cost ):
    # Contains the items of the vertex
    self.items = items
    # Contains the ancestor vertex that generated this vertex
    self.ancestor = ancestor
    # Contains the operation that generated this vertex from the ancestor
    self.operator = operator
    # Contains the depth of this vertex (ancestor.depth +1)
    self.depth = depth
    # Contains the path cost of this vertex from depth 0. Not used for depth/breadth first.
    self.cost = cost

# Main method
def main():
  print("------- SEARCH RUN MENU ------")
  print("1. BFS - Easy") 
  print("2. BFS - Medium")
  print("3. BFS - Hard")
  print("4. DFS - Easy")
  print("5. DFS - Medium")
  print("6. DFS - Hard")
  print("7. IDS - Easy")
  print("8. IDS - Medium")
  print("9. IDS - Hard")
  print("10. A* - Easy")
  print("11. A* - Medium")
  print("12. A* - Hard")
  print("13. Greedy BFS - Easy")
  print("14. Greedy BFS - Medium")
  print("15. Greedy BFS - Hard")
  print("16. IDA* - Easy")
  print("17. IDA* - Medium")
  print("18. IDA* - Hard")
  n = raw_input("Enter what would you like to run: ")
  n = int(n)
  start = time.clock() #Starting time.clock() to count time taken for the function to execute
  if(n == 1):
    print "Initial Puzzle State:"
    print_vertices(easy_initial_state)
    print "\nGoal Puzzle State: "
    output = bfs( easy_initial_state, goal_items )
  elif(n == 2):
    print_vertices(medium_initial_state)
    print "\nGoal Puzzle State: "
    output = bfs( medium_initial_state, goal_items )
  elif(n == 3):
    print_vertices(hard_initial_state)
    print "\nGoal Puzzle State: "
    output = bfs( hard_initial_state, goal_items )
  elif(n == 4):
    print_vertices(easy_initial_state)
    print "\nGoal Puzzle State: "
    output = dfs( easy_initial_state, goal_items )
  elif(n == 5):
    print_vertices(medium_initial_state)
    print "\nGoal Puzzle State: "
    output = dfs( medium_initial_state, goal_items )
  elif(n == 6):
    print_vertices(hard_initial_state)
    print "\nGoal Puzzle State: "
    output = dfs( hard_initial_state, goal_items )
  elif(n == 7):
    print_vertices(easy_initial_state)
    print "\nGoal Puzzle State: "
    output = ids( easy_initial_state, goal_items )
  elif(n == 8):
    print_vertices(medium_initial_state)
    print "\nGoal Puzzle State: "
    output = ids( medium_initial_state, goal_items )
  elif(n == 9):
    print_vertices(hard_initial_state)
    print "\nGoal Puzzle State: "
    output = ids( hard_initial_state, goal_items )
  elif(n == 10):
    print_vertices(easy_initial_state)
    print "\nGoal Puzzle State: "
    output = astar( easy_initial_state, goal_items )
  elif(n == 11):
    print_vertices(medium_initial_state)
    print "\nGoal Puzzle State: "
    output = astar( medium_initial_state, goal_items )
  elif(n == 12):
    print_vertices(hard_initial_state)
    print "\nGoal Puzzle State: "
    output = astar( hard_initial_state, goal_items )
  elif(n == 13):
    print_vertices(easy_initial_state)
    print "\nGoal Puzzle State: "
    output = gbfs( easy_initial_state, goal_items )
  elif(n == 14):
    print_vertices(medium_initial_state)
    print "\nGoal Puzzle State: "
    output = gbfs( medium_initial_state, goal_items )
  elif(n == 15):
    print_vertices(hard_initial_state)
    print "\nGoal Puzzle State: "
    output = gbfs( hard_initial_state, goal_items )
  elif(n == 16):
    print_vertices(easy_initial_state)
    print "\nGoal Puzzle State: "
    output = idastar( easy_initial_state, goal_items )
  elif(n == 17):
    print_vertices(medium_initial_state)
    print "\nGoal Puzzle State: "
    output = idastar( medium_initial_state, goal_items )
  elif(n == 18):
    print_vertices(hard_initial_state)
    print "\nGoal Puzzle State: "
    output = idastar( hard_initial_state, goal_items ) 
  else:
    print "Wrong Input!"           
  print "Direction of Moves:"
  print output
  print "Moves taken: ", len(output)
  print "Nodes visited: ", len(visited_vertices) - 1
  print "Max. length of Node List: ", max
  print "Time taken: ", time.clock() - start

def print_vertices( vertex_items ):
  print "| %i  %i  %i |" % (vertex_items[0], vertex_items[1], vertex_items[2])
  print "| %i  %i  %i |" % (vertex_items[3], vertex_items[4], vertex_items[5])
  print "| %i  %i  %i |" % (vertex_items[6], vertex_items[7], vertex_items[8])
  
def traverse_left( items ):
  new_state = items[:]
  index = new_state.index( 0 )
  # Sanity check
  if index not in [0, 3, 6]:
    temp = new_state[index - 1] #Exchanging null element with positioned element
    new_state[index - 1] = new_state[index]
    new_state[index] = temp
    return new_state
  else: #
      return None

#Function defined for moving the "null" element one place right in the 8-puzzle
def traverse_right( items ):
  # Perform object copy
  new_state = items[:]
  index = new_state.index( 0 )
  # Sanity check
  if index not in [2, 5, 8]:
    # Swap the values.
    temp = new_state[index + 1]
    new_state[index + 1] = new_state[index]
    new_state[index] = temp
    return new_state
  else:
    #Return non if no moves possible
    return None

#Function defined for moving the "null" element one place up in the 8-puzzle
def traverse_up( items ):
  new_state = items[:]
  index = new_state.index( 0 )
  # Sanity check
  if index not in [0, 1, 2]:
    # Swap the values.
    temp = new_state[index - 3]
    new_state[index - 3] = new_state[index]
    new_state[index] = temp
    return new_state
  else:
    # Can't move it, return None
    return None

#Function defined for moving the "null" element one place up in the 8-puzzle
def traverse_down( items ):
  new_state = items[:]
  index = new_state.index( 0 )
  # Sanity check
  if index not in [6, 7, 8]:
    # Swap the values.
    temp = new_state[index + 3]
    new_state[index + 3] = new_state[index]
    new_state[index] = temp
    return new_state
  else:
    # Can't move, return None
    return None

#Defining a function for initializing a node
def vertex_init(items, ancestor, operator, depth, cost ):
  return vertex(items, ancestor, operator, depth, cost )

def expand_vertex( vertex, vertices, visited_vertices):
  #Returns a list of expanded child vertices
  child_vertices = []
  if vertex.items not in visited_vertices:
    visited_vertices.extend([vertex.items])
    child_vertices.append( vertex_init( traverse_up( vertex.items ), vertex, 'UP ->', vertex.depth + 1, 0 ) )
    child_vertices.append( vertex_init( traverse_down( vertex.items ), vertex, 'DOWN ->', vertex.depth + 1, 0 ) )
    child_vertices.append( vertex_init( traverse_left( vertex.items ), vertex, 'LEFT ->', vertex.depth + 1, 0 ) )
    child_vertices.append( vertex_init( traverse_right( vertex.items), vertex, 'RIGHT ->', vertex.depth + 1, 0 ) )
  child_vertices = [vertex for vertex in child_vertices if vertex.items != None] 
  return child_vertices

#Defining a breadth first search function
def bfs( start, goal ):
    global max
    vertices = []
    # Create the queue with the root vertex in it.
    vertices.append( vertex_init( start, None, None, 0, 0 ) )
    while True:
      # If no states exist
      if len( vertices ) == 0: 
        return None
      vertex = vertices.pop(0)
      #returning list of directions/moves taken to get to goal state
      if vertex.items == goal:
        moves = []
        print_vertices(vertex.items)
        temp = vertex
        while True:
          moves.insert(0, temp.operator)
          if temp.depth == 1: break
          temp = temp.ancestor
        return moves                
      # Expand the vertex and add all the expansions to the front of the stack
      vertices.extend( expand_vertex( vertex, vertices, visited_vertices ) )
      if len(vertices) > max: max = len(vertices)

#Defining a depth first search function
def dfs( start, goal, depth= 150 ):
  global max
  depth_limit = depth
  vertices = []
  vertices.append( vertex_init( start, None, None, 0, 0 ) ) #Appending the queue with the root vertex
  while True:
    if len( vertices ) == 0: return None #No solution if states are over
    vertex = vertices.pop(0)
    if vertex.items == goal: #code for returning the goal state and moves it took to reach there
      moves = []
      print_vertices(vertex.items)
      temp = vertex
      while True:
        moves.insert(0, temp.operator)
        if temp.depth <= 1: break
        temp = temp.ancestor
      return moves                
    #Append the child_nodes to the front of the stack
    if vertex.depth < depth_limit:
      child_vertices = expand_vertex( vertex, vertices, visited_vertices )
      child_vertices.extend( vertices )
      vertices = child_vertices
    if len(vertices) > max: max = len(vertices)

#Defining an iterative-depeening search function, with a variable for depth, which can be modified.
def ids( start, goal, depth = 150 ):
  for i in range( 100, depth ):
    output = dfs( start, goal, i )
    if output != None:
      return output

def astar( start, goal ):
  global max #Define an informed search A* based on a heuristic function
  vertices = []
  vertices.append( vertex_init( start, None, None, 0, 0 ) )
  while True:
    # If no states exist
    if len( vertices ) == 0: 
      return None
    # Vertices behaves as a priority Queue using the dort function
    vertices.sort( cmpastar )
    # Popping the head of the priority Queue
    vertex = vertices.pop(0)
    # if this vertex is the goal, return the moves it took to get here.
    print "Checking state", vertex.items, " with direction: ", vertex.operator
    if vertex.items == goal:
      moves = []
      print_vertices(vertex.items)
      temp = vertex
      while True:
        moves.insert( 0, temp.operator )
        if temp.depth <=1: break
        temp = temp.ancestor
      return moves
    #Expand the vertex and add all expansions to the end of the queue
    vertices.extend( expand_vertex( vertex, vertices, visited_vertices ))
    if len(vertices) > max: max = len(vertices)

def gbfs(start, goal):
  global max
  vertices = []
  vertices.append( vertex_init( start, None, None, 0, 0 ) )
  while True:
    # If no states exist
    if len( vertices ) == 0: 
      return None
    #Sorting by making list behave as a proirity queue on basis of compare function. We need to manually change the heuristic
    vertices.sort( cmpgbfs )
    # take the vertex from the front of the queue
    vertex = vertices.pop(0)
    #if we reach the goal vertex, returm the directions to reach here
    print "Checking state", vertex.items, " with direction: ", vertex.operator
    #print visited_vertices
    if vertex.items == goal:
      moves = []
      print_vertices(vertex.items)
      temp = vertex
      while True:
        moves.insert( 0, temp.operator )
        if temp.depth <=1: break
        temp = temp.ancestor
      return moves
    #Expand the vertex and add all expansions to the end of the queue
    vertices.extend( expand_vertex( vertex, vertices, visited_vertices ))
    if len(vertices) > max: max = len(vertices)

def idastar(start, goal, depth_limit = 300):
  global max
  for i in range( 100, depth_limit ):
    vertices = []
    vertices.append( vertex_init( start, None, None, 0, 0 ) )
    while True:
      # If no states exist
      if len( vertices ) == 0: 
        return None
      # Vertices behaves as a priority Queue using the dort function
      vertices.sort( cmpastar )
      # Popping the head of the priority Queue
      vertex = vertices.pop(0)
      # If this vertex is the goal, return the moves it took to get here.
      print "Checking state", vertex.items, " with direction: ", vertex.operator
      if vertex.items == goal:
        moves = []
        print_vertices(vertex.items)
        temp = vertex
        while True:
          moves.insert( 0, temp.operator )
          if temp.depth <=1: break
          temp = temp.ancestor
        return moves
      # Append the vertices in front of the queue
      if vertex.depth < depth_limit:
        child_vertices = expand_vertex( vertex, vertices, visited_vertices )
        child_vertices.extend( vertices )
        vertices = child_vertices
      if len(vertices) > max: max = len(vertices)
        
def cmpastar( a, b ):
  #Compare function for astar. f(n) = g(n) + h(n)
  return (a.depth + h( a.items, goal_items )) - (b.depth + h( b.items, goal_items ))

def cmpgbfs( a, b ):
  #Compare function for gbfs - h(n)
  return h( a.items, goal_items ) - h( b.items, goal_items )

def h(items, goal ):
  # Defining a heuristic h1(n) for the Informed search algorithms
  score = 0
  for i in range( len( items ) ):
    if items[i] != goal[i]:
      score = score + 1
  return score

def h2 ( items, goal_items):
  value = 0
  for i in items:
    if not i:
      continue
    row_idx = items.index(i) / 3
    col_idx = items.index(i) % 3
    row_idx_goal = goal_items.index(i) / 3
    col_idx_goal = goal_items.index(i) % 3
    value += abs(row_idx_goal - row_idx) + abs(col_idx_goal - col_idx)
  return value

def cmpastar2(a, b):
  return h2( a.items, goal_items ) - h2( b.items, goal_items )

def cmpgbfs2(a, b):
  return h2( a.items, goal_items ) - h2( b.items, goal_items )      

# For execuing the main() function
if __name__ == "__main__":
  main()