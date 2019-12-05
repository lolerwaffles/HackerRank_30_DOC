NumEntries = int(input())
PhoneBook = {}

for i in range(NumEntries * 2):
    entry = input()
    split_entry = entry.split()
    if len(split_entry) ==2:
        PhoneBook[split_entry[0]] = split_entry[1]
    if len(split_entry) == 1:
        try:
            print("{}={}".format(split_entry[0],PhoneBook[split_entry[0]]))
        except:
            print("Not found")
