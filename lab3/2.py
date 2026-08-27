def selection(arr):

    for i in range(len(arr)-1):

        Min = i

        for j in range(i+1,len(arr)):

            if arr[j]<arr[Min]:
                Min = j


        arr[Min],arr[i]=arr[i],arr[Min]


    print(arr)


def main():
    n = int(input("Enter the size of the list: "))

    if n <= 0:
        print("Invalid size")
        return

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i+1}: ")))


    selection(arr)


main()
