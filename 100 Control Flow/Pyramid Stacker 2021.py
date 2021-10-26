stack = int(input("Hello to Super Stacker Simulator 2021! How units tall would you like your stack?: "))
def createTriangle(stack):
    starCount = 1

    for i in range(stack):
        for space in range(stack - starCount):
            print(" ", end = "")

        for star in range(starCount):
            print("#", end = "")

        print()
        starCount = starCount + 1

createTriangle(0)  

if stack > 8 or stack < 1: 
    print("ERROR 403: Super Stacker Simulator can only stack a maximum of 8 stacks and cannot stack nothing.")
else : 
    createTriangle(stack)

