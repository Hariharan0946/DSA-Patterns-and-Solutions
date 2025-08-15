"""
#average or mean of a list
list1=[1,2,3,4,5,6,7,8]
average=sum(list1)/len(list1)
print(average)

#separate odd and even
number=[1,2,3,4,5,6]
even=[]
odd=[]
for num in number:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(f"even {even}")
print(f"odd {odd}")
        
#get smaller elements
number1=[1,2,3,4,5,6]
threshold=3
smaller=[]
for num in number1:
    if num < threshold:
        smaller.append(num)
print(smaller)

#slicing ----- sequence[start:stop:step]
text="hello"
tup1=(1,2,3,4,5)
list2=[1,2,3,4]
print(text[0:1])
print(tup1[0:1])
print(list1[0:1])

#list_comprehension
#var=[expression you want to add for iterable variable in iterable]
var1=[x+8 for x in range(5)]
print(var1)

#Largest Element in a List
#using max
number5=[1,34,35,56,34,63,23,53]
var2=max(number5)
print("the largest number ", var2)
#without max
number5=[1,34,35,56,34,63,23,53]
largest=number5[0]
for num in number5:
    if num > largest:
        largest=num
print("the largest number ",largest)


#Smallest Element in a List
#using min 
number5=[76
         ,34,35,56,34,63,23,53]
var2=min(number5)
print("the smallest number ", var2)
#without min
number5=[76,34,35,56,34,63,23,53]
smallest=number5[0]
for num in number5:
    if num < smallest:
        smallest=num
print("the smallest number ",smallest)

#Second Largest Element in a list
num1=[3,35,6,43,34]
num1.sort(reverse=True)
print(num1[1])

#Check if a list is Sorted
num1=[1,2,3]
var=sorted(num1)
if num1== var:
      print("True")
else:
       print("False")

#Reverse a List in Python
#manual
num1=[1,2,3]
num2=[]
for i in range(len(num1)-1,-1,-1):
    num2.append(num1[i])
print("reverse num",num2)
#reverse method
num1=[1,2,3]
num1.reverse()
print(num1)
#reversed method
num1=[1,2,3]
reversednum=list(reversed(num1))
print(reversednum)

#Remove duplicates from sorted array(using sliding window algorithm)
num=[1,1,1,1,2,3,3,3,3,3,3,6,7,7,7,7,7]
left=0
right=1
while right < len(num) :
    if num[left] == num[right]:
        del_value=num.pop(right)
    else:
        left=left+1
        right=right+1
print(num)

#Move Zeros to End
num=[0,0,0,0,0,2,3,4]
left=0
right=0
while right < len(num):
    if num[right] != 0:
        num[left],num[right]=num[right],num[left]
        left=left+1
    right=right+1
print(num)

#Leaders in an Array problem
arr = [17, 18, 15,7,2]
large = []


# Start from the last element (it's always a leader)
arr = [17, 18, 5, 4, 6, 1]
max_element=arr[-1]
large=[]
large.append(max_element)
for i in range(len(arr)-2,-1,-1):
    element=arr[i]
    if element > max_element:
         max_element=element
         large.append(max_element)
large.reverse()
print(large)

#Frequencies in a sorted array
arr=[56,56,1,2,3]
count=1
for i in range(1,len(arr)):
    if arr[i] == arr[i-1]:
        count=count+1
    else:
        print(f"{arr[i-1]} --> {count}")
        count=1
print(f"{arr[len(arr)-1]} --> {count}")
    
#Left Rotate a List by one
arr=[1,2,3,4,5,6]
temp=arr.copy()
for i in range(0,len(arr)):
    arr[i-1]=temp[i]
print(arr)

#left rotate by k places
arr=[1,2,3,4,5,6]
temp=arr.copy()
k=int(input("enter how many position to left rotate the array:"))
for i in range(len(arr)):
      arr[i-k]=temp[i]
print(arr)

#Maximum difference
arr = [2, 3, 10, 6, 4, 8, 1]
maxi=max(arr)
print("the largest element in the list ",maxi)
small=[]
arr_copy=arr.copy()
for i in range(0,len(arr)):
    if arr[i] == maxi:
        break
    arr1=arr[i]
    small.append(arr1)
smalli=min(small)
print("smallest element before largest element",smalli)
difference=maxi-smalli
print("difference of smallest element before largest element ", difference)

#Stock Buy &Sell Part 2 (part 1-single transcations , part 2 - multiple transcations)
prices = [1,2]
left=0
right=1
profit=[]
for i in range(0,len(prices)-1):
    if prices[left] < prices[right]:
          difference = prices[right] - prices[left]
          profit.append(difference)
    left=left+1
    right=right+1
profit_sum=sum(profit)
print(profit_sum)

#Trapping Rain Water
arr=[4,2,0,3,2,5]
first=arr[0]
last=arr[-1]
water_hold_height=min(first,last)
water_unit=[]
print(water_hold_height)
for i in range(0,len(arr)):
    difference =water_hold_height - arr[i]
    if difference >0:
        water_unit.append(difference)
print(water_unit)
total_unit=sum(water_unit)
print(total_unit)

#Maximum Consecutive 1s
arr=[1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1]
count=0
counting=[]
for i in range(0,len(arr)):
         if arr[i] == 1:
                count=count+1
         else:
            counting.append(count)
            count=0
counting.append(count)
maxi=max(counting)
print(maxi)
  

#Longest even odd subarray
arr = [1,2,3,4,5,6]
count=0
counting=[]
for i in range(0,len(arr)):
         if arr[i]%2!=0  and arr[i-1]%2==0 or arr[i]%2==0  and   arr[i-1] %2!=0:
                count=count+1
         else:
            counting.append(count)
            count=0
counting.append(count)
maxi=max(counting)
print(maxi)


#Majority element
nums = [1,1,1,1,1,5,65,1,6,7]
n=len(nums)
nums.sort()
count=1
d={}
for i in range(1,len(nums)):
    if nums[i] == nums[i-1]:
        count=count+1
        if count > n // 2:
            print(f"majority element is {nums[i-1]} ==> count:{count}")
    else:
            count=1
"""              
#Minimum Consecutive flips        

arr=[1,1,1,0,0,0,0,1,0]
for i in range(1,len(arr)):
    if arr[i] != arr[i-1]:
        if arr[i]!=arr[0]:
            print("for " ,i , "to",end=" ")
        else:
            print(i-1)
if arr[0]!=arr[-1]:
    print(len(arr)-1)
    










