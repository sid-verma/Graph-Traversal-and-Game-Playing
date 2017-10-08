import sys
def main ():
 #Setting abs_min as minus infinity
 abs_min= -float("inf")
 #Setting abs_max as plus infinity
 abs_max=float("inf")

 #Uncomment to run as examples:
 #tree_value="((4 (7 9 8) 8) (((3 6 4) 2 6) ((9 2 9) 4 7 (6 4 5))))"
 #tree_value= "(((1 4) (3 (5 2 8 0) 7 (5 7 1)) (8 3)) (((3 6 4) 2 (9 3 0)) ((8 1 9) 8 (3 4 ))))"
 #tree_value= "(5 (((4 7 -2) 7) 6))"
 #tree_value="((8 (7 9 8) 4) (((3 6 4) 2 1) ((6 2 9) 4 7 (6 4 5))))"
 #tree_value="(((1 (4 7)) (3 ((5 2) (2 8 9) 0 -2) 7 (5 7 1)) (8 3)) (((8 (9 3 2) 5) 2 (9 (3 2) 0)) ((3 1 9) 8 (3 4 ))))"

 print("Input tree_value is:")
 for value in tree_value:
    print(value)
 print ("\n")
 root=tree_init(tree_value)   #Construct the tree from tree_value
 result=eval_ab(root,abs_min,abs_max)  #Retunrs the final alphabeta value of the tee
 print ("The tree has the following Alpha and Beta Values: %i" % result)
 path_list=[]
 final_path(root,result,path_list)  #Function call to return the final solution

def generate_node(value,play,depth):    #Function call to generate a node
    return NODE(value,play,depth)

#Constructing a tree from given tree_value as input
def  tree_init(tree_value):
  count_open=0                 
  #Initilasing the variable open step which will keep step of open braces
  count_closed=0                 
  #Initilasing the variable closed step which will keep step of closed braces
  list_stack=[]                     
  #A list_stack to hold the nodes of the tree being generated
  total_count=0
  NEG=0         
  #A switch for negative numbers
  flag= 0              
  #A check switch
  value=""
  for char in tree_value:
    if isOpenParantheses(char):  #TO check if we have open parantheses, 
      count_open=count_open + 1
      list_stack.append(generate_node(0,\
      minimax(count_open-count_closed-1),count_open-count_closed-1))
    elif isClosedParantheses(char):    
    #To check for closed brackets
      count_closed=count_closed + 1
      if(flag):
        if(NEG):     
          #If the number is NEG, generate the node will NEG number
          value=-int(value)
          NEG=0
        nodenew=generate_node(int(value),\
        minimax(count_open-count_closed + 1),count_open-count_closed + 1)
        parentnode=list_stack.pop()  
        parentnode.create_child(nodenew) 
        #Creating a child node from a parent node
        list_stack.append(parentnode)
        flag=0
        value=""
      Remove_node=list_stack.pop()
      if len(list_stack)!= 0:         
        parentnode=list_stack.pop()
        parentnode.create_child(Remove_node)
        list_stack.append(parentnode)
      else:                           
        return Remove_node       
    else:
      if char != ' ':        
      #Used to find out the spaces in the tree_value
        if char !='-':       
        #Used to check if we have NEG character in the tree_value
          value=value + char     
          #Used to generate multiple digit number
          flag=1  
          #A flag to indicate that number has started
        else:
          NEG=1
      else:
        if(flag):
          if(NEG):
            value=-int(value)
            NEG=0
          nodenew=generate_node(int(value),\
          minimax(count_open-count_closed),count_open-count_closed)
          parentnode=list_stack.pop()
          parentnode.create_child(nodenew)
          list_stack.append(parentnode)
          flag=0
          value=""  

#Defining the technique for calculating (alpha, beta) value of the tree
def eval_ab(node,abs_min,abs_max):
  if leaf_node_check(node):   #if the node is leaf node, then take its utility values
    return node.value
  if node.play=="MAX":  #If the node type is MAX node, 
    max_val= abs_min  #Iniitalising the max value to abs_min
    for child in node.descendants:   
      max_node_val= eval_ab(child,max_val,abs_max) #take the alphabeta value of each child 
      if max_node_val>max_val:  #Checking for maximum Value
        max_val=max_node_val
        child.update_value(max_node_val)  #update the child value
      if max_val > abs_max:  #If the MAX value is greater than maximma, then prune
        print "Pruning will occur for MAX value of ",( child.value), " at position",
        #for  child in node.descendants:
        #print(child.value, end=" ")
        utility_val(node)  #get node value from utility value
        print ("\n")
        return abs_max
     return max_val  #return the max value for the max node
  if node.play=="MIN":  #if the node type is MIN node,
    min_val= abs_max  #iniitalising the min value to abs_max
    for child in node.descendants:
      min_node_val= eval_ab(child,abs_min,min_val)  #get the alphabeta value of each child  
      if min_node_val<min_val:   #if the min child valus is lesser than min_val, take the min_val
        min_val=min_node_val
        child.update_value(min_node_val)
      if min_val < abs_min:    #if the min_val is lesser than abs_min, then return the abs_min
        print  "Pruning will occur for the MIN value of ", (child.value), "at position",
        utility_val(node) #get node value from utility value
        print ("\n")
        return abs_min
    return min_val        
  return output  #return the aplhabeta value of the game tree

#A function to check if the node is a leaf node or not
def leaf_node_check(node):
  if len(node.descendants)==0:
    return True
  else:
    return False                  

#A function to indicate whether node is max or min
def minimax(value):
  if (value%2==0):
    return "MAX"
  else:
    return "MIN"  

#Defining a function to traverse the tree using the utility values
def utility_val(node):
  step=0
  for nodes in node.descendants:      
    if (len(nodes.descendants)!=0):  
    #If we are at end of tree i.e. at a leaf
      step=step + 1
      print("(")
      utility_val(nodes)
      if step==len(node.descendants): 
      #To check if we have traversed the entire graph
      print(")")
    else:                    
      step=step  +  1
      print(nodes.value)  
      if step==len(node.descendants):
        print (")")     

#A function to find out open parantheses in tree_value
def isOpenParantheses(char):
  if (char=='('):
    return True
  else:
    return False
#A function to find out closed parantheses in tree_value
def isClosedParantheses(char):
  if (char==')'):
    return True
  else:
    return False        
      
#A function to find the final solution path
def final_path(node,result,path_list):
  step=0                      
  if len(node.descendants)==0:     
    print("Solution path is: ") 
    for value in path_list:         
    #Printing the solution path
      print(value)
    return   
  for nodes in node.descendants:        
  #Traverse from root node of the tree to leaf node in order to find the solution path
    step=step + 1
    if(nodes.value) == result:     
    #To check if the node value matches the final minmax value of the tree
      path_list.append(step)
      break
    final_path(nodes,result,path_list)

'''Definition of a Vertex Class with the following attributes
Vertex.value
Vertex.play
Vertex.descendants
Vertex.depth'''
class NODE:
  def __init__ (self,value,play,depth):
  #Class node will have type nodes value, node type (min or max), node depth
    self.value=value
    self.play=play
    self.descendants= []
    self.depth=depth

  def create_child(self,descendants):
  #Adding the descendants in the nodes
    self.descendants.append(descendants)

  def update_value(self,value): #Setting new value for vertex
    self.value=value

if __name__ == '__main__':
  main()
