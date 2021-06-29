import sys

def main():

    # Reads input from the user STDIN
    # Line 1 - No. of ingredients
    # Line 2 - qunatity of each ingredient to make a dessert
    # Line 3 - quantity of each ingredient's stock available

    inp = sys.stdin.readlines()
    
    num_ingred = inp[0]
    ingred = inp[1].split()
    stock  = inp[2].split()

    Calculate_stock(num_ingred, ingred, stock)

# Calculates the maximum number of desserts that can be prepared with available ingredients
def Calculate_stock(num_ingred, ingred, stock):
    
    dessert = [0 for i in range(int(num_ingred))]
    for i in range(int(num_ingred)):
        dessert[i] = int(stock[i]) / int(ingred[i]) 
    
    print(min(dessert))

if __name__ == "__main__":
    main()