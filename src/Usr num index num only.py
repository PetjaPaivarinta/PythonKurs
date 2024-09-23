str = input("Please input your string: ")

strLen = len(str)

print("Printing only even index chars")


for x in range(strLen):
    if x % 2 == 0:
        print(str[x])