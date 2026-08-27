def sort(arr):

    for i in range (len(arr)-1):
        
        for j in range(len(arr)-1-i):
            
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    print(arr)
    

def main():
    n = int(input("Enter the size of the list: "))

    if n <= 0:
        print("Invalid size")
        return

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i+1}: ")))


    sort(arr)


main()
