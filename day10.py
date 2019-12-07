if __name__ == '__main__':
    n = int(input())
    binArray = bin(n).replace('b','').split('0')
    print(len(sorted(binArray, key=len)[-1]))
    
