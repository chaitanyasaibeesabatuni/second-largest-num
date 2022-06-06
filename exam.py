def find():
    n = int(input("enter the size of your array :"))
    a = list(map(int, input("enter your array values :").split()))
    k = sorted(a)
    print("value:", k[-2])
    print("position:", a.index(k[-2]) + 1)

if __name__=="__main__":
    for _ in range(int(input("enter how many times you have run the program :"))):
        find()
