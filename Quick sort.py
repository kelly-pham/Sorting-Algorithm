#Quick sort the given list

from random import randint


def QuickSort(list1,start,end):             #define Quick Sort function
    if start < end:
        pivot=randint(start,end)            #choose pivot: a random number in the list
                                                # could be start/end/middle or median of start,end,middle
        p = Partition(list1, start,end)          # choose start/ end will generate worst case scenario when the list is already sorted

        QuickSort(list1,start,p-1)          # sort from start to pivot -1
        QuickSort(list1,p+1,end)            # sort from p +1 to end

def Partition(list1,start,end):
    newIndex=start-1
    for index in range(start,end):
        if list1[index]< list1[end]:                # if index is smaller than end

            newIndex = newIndex + 1                     # increase index

            list1[index],list1[newIndex]=list1[newIndex],list1[index]      #and swap index and newIndex (Tuple)
            #temp=list1[index]
            #list1[index]=list1[newIndex]
            #list1[newIndex]=temp


    return newIndex + 1


list1=[40,15,12,5,5,9,78]
QuickSort(list1,0,len(list1)-1)
print(list1)

