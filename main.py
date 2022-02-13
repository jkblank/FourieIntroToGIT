inputvar = int(input( "Input a number to converto to binary: "))
outputvar=""
while (inputvar>0):
    if(inputvar%2==1):
        outputvar="1"+outputvar
        inputvar=(inputvar-1)/2
    else:
        outputvar="0"+outputvar
        inputvar=(inputvar)/2

print("Binary is: " + outputvar)