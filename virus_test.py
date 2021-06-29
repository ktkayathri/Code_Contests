# Virus Test - 
# Input line 1 - Virus composition (string of characters eg- coronavirus)
# Input line 2 - Number of people tested (n)
# Input line 3 to n - Enter the blood composition of each person
# Output - for each blood composition, chek if the blood comp if the subsequence (sequence should be same but not substring) 
#           of virus comp
#       POSITIVE - if blood comp is a subsequence
#       NEGATIVE - if not a subsequence

import sys

def main():
    
    # Set of code to get input line by line

    # virus_comp = input("Enter composition: ")
    # if not virus_comp.islower():
    #     virus_comp = virus_comp.lower()
    # num_people = int(input("Enter Number of people tested: "))
    # blood_comp = [' ' for i in range(num_people)]
    # for i in range(num_people):
    #     blood_comp[i] = input("Enter blood composition of %d : " %(i+1))

    inp = sys.stdin.readlines()

    virus_comp = inp[0]

    if not virus_comp.islower():
        virus_comp = virus_comp.lower()
    
    num_people = int(inp[1])
    blood_comp = [' ' for i in range(num_people)]
    for i in range(num_people):
        blood_comp[i] = inp[i+2]
   
    for i in range(num_people):
        pos = -1
        flag = 0
        for j in range(len(blood_comp[i])):
            pos = virus_comp.find(blood_comp[i][j],pos+1)
            print(pos)
            if (pos == -1):
                flag = 1
                break
        if (flag == 0):
            print ("POSITIVE")
        else:
            print ("NEGATIVE")

if __name__ == "__main__":
    main()