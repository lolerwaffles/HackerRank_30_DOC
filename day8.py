entry = input()
entry = input()
PhoneBook = {}

while entry != None:
    split_entry = entry.split()
    if len(split_entry) > 1:
        PhoneBook[split_entry[0]] = split_entry[1]
    else:
        if split_entry[0] in PhoneBook:
            print("{}={}".format(split_entry[0],PhoneBook[split_entry[0]]))
        else:
            print("Not found")
    try:
        entry = input()
    except:
        entry = None
