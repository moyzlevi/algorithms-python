def insertion_sort(n, list):
    for i in range(1, n):
        key = list[i]
        j = i - 1
        while j > -1 and list[j] > key:
            list[j+1] = list[j]
            j-=1
        list[j+1] = key
        print(list)
