#Bubble sort. Uses a temp variable for comparisons. Slow, only use for small lists unless you like waiting.
def bubble_manual_sort(list: list, *, order: str) -> int:
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            match order:
                case "asc":
                    if list[j] > list[j + 1]:
                        temp = list[j]
                        list[j] = list[j+1]
                        list[j+1] = temp
                case "desc":
                    if list[j] < list[j + 1]:
                        temp = list[j]
                        list[j] = list[j+1]
                        list[j+1] = temp
    return list

#Quick sort. Left as manual_sort to function with pre written unit tests.
#This implementation uses auxiliary lists, so could be more memory efficient.
def manual_sort(list: list, *, order: str) -> int:
    if len(list) < 2:
        return list
    else:
        match order:
            case "asc":
                pivot= list[0]
                less = [i for i in list[1:] if i <= pivot]
                greater = [i for i in list[1:] if i > pivot]
                return manual_sort(less, order="asc") + [pivot] + manual_sort(greater, order="asc")
            case "desc":
                pivot= list[0]
                less = [i for i in list[1:] if i <= pivot]
                greater = [i for i in list[1:] if i > pivot]
                return manual_sort(greater, order="desc") + [pivot] + manual_sort(less, order="desc")
            
data = [5,2,1,6,4,34,2365,234,236,642,62345,435]

if __name__ == "__main__":
    print(manual_sort(data, order="asc"))
