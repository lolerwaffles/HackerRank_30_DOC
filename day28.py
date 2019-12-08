if __name__ == '__main__':
    dataSet = {}
    inputLine = input()
    inputLine = input()

    while inputLine != None:
        firstNameEmailID = inputLine.split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        dataSet[emailID] = firstName
        try:
            inputLine = input()
        except:
            inputLine = None

for i in sorted(dataSet.items(), key = lambda kv:(kv[1], kv[0])):
    if "@gmail.com" in i[0]:
        print(i[1])
        
