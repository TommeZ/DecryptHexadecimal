def convertHexToDec(hexSubString):
    return chr(int(hexSubString, 16))   # int allows us to convert base easily!

hexaString = "54686973206973206120737472696E6720656e636f64656420696e2068657869646563696d616c21"
outString = ""

if len(hexaString) % 2 == 0:
    for i in range(0,len(hexaString),2):
        subStr = hexaString[i] + hexaString[i+1]
        outString += convertHexToDec(subStr)

print(outString)
