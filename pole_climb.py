# A drunk person is climbing a pole. During day time he climbs X metre and during night he slides
# Y metre. The height of the pole is N. Calculate how many days it might take him to reach the 
# top of the pole.
# Input line 1 --> No. of testcases (T)
# Input lines 2 to T --> X, Y, N  (X - metres climbed, Y - meters slid, N - height of the pole)



import sys

def main():

    inp = sys.stdin.readlines()
    
    test_case = inp[0]
    
    for i in range(1,len(inp)):
        X,Y,N = inp[i].split()
        print("X,Y,N : ", X,Y,N)
        days = find_days(int(X),int(Y),int(N))
        print(days)
    
def find_days(X,Y,N):
    t = 0
    days = 0
    if Y > X:
        print(str(Y) + " > " + str(X) + "  Not a valid case. Try again!")
        quit()
    while (t < N):
        t = t + X - Y
        if (t < N ):
            days += 1
    return(days)  

if __name__ == "__main__":
    main()