# sorted list by using Merge Sort


def mergeSort(list1):
    if len(list1) > 1:
        middle = len(list1)//2            # find a mid point in a list
        LeftArray = list1[:middle]             # divide Array (Left side )
        RightArray = list1[middle:]            # divide Array (Right side)


        mergeSort(LeftArray)                # best case happen
        mergeSort(RightArray)               # best case happen

        i = j = k = 0
        while i<len(LeftArray) and j <len(RightArray):
            if LeftArray[i] < RightArray[j]:
                list1[k] = LeftArray[i]
                i=i+1
            else:
                list1[k]= RightArray[j]
                j=j+1
            k=k+1

        while i<len(LeftArray):             # merge Left Array then merge back to original list
            list1[k]=LeftArray[i]
            i=i+1
            k=k+1

        while j < len(RightArray):          # merge Right Array then merge back to original list
            list1 [k] = RightArray[j]
            j=j+1
            k=k+1


list2=[]            # create empty list to store value inserted from user

for item in range(1):
   item=input("Enter a number from 1 to 100:")
   list2.append(item)
   list1= [x for x in list2[0].split(",")]     # convert string to int with split()
   print("Orginal list:", list1)
   mergeSort(list1)
   print("Merge sort: ",list1)
