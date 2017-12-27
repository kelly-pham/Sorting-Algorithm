# sort a list inserted by Insert Sort

def insertsort(list1):                  # call function Insert Sort
    for index in range(1,len(list1)):
        key=list1[index]
        j=index

        while j>0 and list1[j-1]>key:
            list1[j]=list1[j-1]
            j=j-1
        list1[j]=key

list2=[]            # create empty list to store value inserted from user

for item in range(1):
   item=input("Enter a number from 1 to 100:")
   list2.append(item)
   list1= [x for x in list2[0].split(",")]     # convert string to int with split()
   print("Orginal list:", list1)
   insertsort(list1)    # call function to sort value from user
   print("Sorted list: ",list1)






