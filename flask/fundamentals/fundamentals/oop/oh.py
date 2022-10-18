def countdown(num):
    print(f"input: {num}")
    output=[]
    for i in range(num, -1, -1):
        print(f"i:{i}")
        output.append(i)
    print(f"output: {output}")  
    return output
num = 5
#countdown(num)

def goldilocks(input):


    if(input[1]> len(input)):
        print("Too big")
    elif(input[1]< len(input)):
        print ("Too small")
    else:
        print("just right")

goldilocks([6,1,7,54,2])