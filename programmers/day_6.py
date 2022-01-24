#버블 소트 문제

n = input()
list = list(map(int, input().split()))

def bubble_sort(list):
    unsorted_until_index = len(list) - 1
    sorted = False

    count = 0
    while not sorted :
        sorted = True
        for i in range(unsorted_until_index):
            if list[i]>list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                count += 1
                sorted = False
        unsorted_until_index -= 1

    return list, count


print(bubble_sort(list))