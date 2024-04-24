#Bubble sort. Uses no auxiliary space (I think?). Slow, only use for small lists unless you like waiting.
def bubble_manual_sort(list: list, *, order: str) -> int:
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            match order:
                case "asc":
                    if list[j] > list[j + 1]:
                        list[j], list[j + 1] = list[j + 1], list[j]
                case "desc":
                    if list[j] < list[j + 1]:
                        list[j], list[j + 1] = list[j + 1], list[j]
    return list

#Quick sort. Left as manual_sort to function with pre written unit tests.
#This implementation uses auxiliary lists, so could be more memory efficient.
def manual_sort(list: list, *, order: str) -> int:
    if len(list) < 2:
        return list
    else:
        pivot= list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        match order:
            case "asc":
                return manual_sort(less, order="asc") + [pivot] + manual_sort(greater, order="asc")
            case "desc":
                return manual_sort(greater, order="desc") + [pivot] + manual_sort(less, order="desc")

#Selection sort. Also pretty slow
def selection_manual_sort(list: list, *, order: str) -> int:
    for i in range(len(list)):
        minimum_index = i
        for j in range(i + 1, len(list)):
            match order:
                case "asc":
                    if list[j] < list[minimum_index]:
                        minimum_index = j
                case "desc":
                    if list[j] > list[minimum_index]:
                        minimum_index = j
        list[i], list[minimum_index] = list[minimum_index], list[i]
    return list    

data = [4,3,2,6,5]


if __name__ == "__main__":
    print(manual_sort(data, order="asc"))
