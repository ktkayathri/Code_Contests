# To find the max cost Karn can spend while travelling across N shops through P paths
# each path with cost C. Cost has to be paid only the first time. 
# Input line 1 --> 'No. of Test cases' 1 < T <= 10
# Input Line 2 --> 'No. of shops' : 1<= N <=100000 and 'No. of Paths' : 1<= P <=1000000
# Input Line 3 --> P lines of three space separated X, Y and C where X and Y represents the 
# numbers and indicate a path between the two. C is the cost to travel on the path.

def main():
    
    # Read first line --> No. of testcases 
    test_case = file.readline()   
    print (test_case)

    if (int(test_case) > 10):
        print("Test case exceeding Maximum limit. Give value between 1 and 10")
        quit()

    # Loop for each test case
    for each_case in range(int(test_case)):
        get_input()

# Method to get the second line --> No. of shops and paths
def get_input():

    line2 = file.readline()
    shops, paths = line2.split()
    print (shops , paths)  
    
    if ((int(shops) > 100000) or (int(paths) > 1000000)):
        print("Number of shops/Paths exceeding the limit.")
        quit()

    global path,work_path

    # Initializing the lists before storing the path cost
    rows = cols = int(shops)
    path = [[0 for i in range(rows)] for j in range(cols) ]
    work_path = [0 for i in range(rows)]
    
    # Read every path input and save it in form of 2D matrix
    for each_path in range(int(paths)):
        next_line = file.readline()
        ip1, ip2, ip3 = next_line.split()
        ip1, ip2, ip3 = int(ip1), int(ip2), int(ip3)    

        path[ip1-1][ip2-1] = ip3
        path[ip2-1][ip1-1] = ip3

    # Start with Vertex number 0
    first_vertex = 0
    work_path = path[first_vertex]
    visited_vertices.append(first_vertex)
    build_graph(work_path)

# Build the graph with maximum cost 
def build_graph(work_path):
    
    max_cost = 0 
    for j in range(len(work_path)):
        if (work_path[j] > max_cost):
            max_cost = work_path[j]
            next_vertex = j

    check_visited(work_path, next_vertex)

# Check if the vertex is already visited, if yes, visit the next vertex with max cost
def check_visited(work_path, next_vertex):

    global total_cost
    global visited_vertices
    if (len(visited_vertices) == len(work_path)):
        print ("All vertices visited! TOTAL COST IS  ", total_cost)
        visited_vertices = []
        total_cost = 0
    else:
        if next_vertex in visited_vertices:
            work_path[next_vertex] = 0
            build_graph(work_path)
        else:
            total_cost += work_path[next_vertex]
            visited_vertices.append(next_vertex)
            build_graph(path[next_vertex])


if __name__ == "__main__":

    file = open("input_shop.txt","r")  #Input file
    visited_vertices = []
    total_cost = 0
    main()
    file.close()