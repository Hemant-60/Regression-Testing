'''
Created : 12th October 2019
Topic: Regression Testing
Author: Hemant Rana
'''

def is_all_zeros(a):
    for i in a:
        if(i!=0):
            return False
    return True

def find_max_index(a):
    max_index=0
    for i in range(0,len(a)):
        if(a[i]>a[max_index]):
            max_index=i
    return max_index

def has_changed_lines(a):
    for i in a:
        if(i!=-1):
            return True
    return False

# ----------------Input for covered lines by test cases--------------------
nums = int(input("Enter number of test cases: "))
covers = []
for i in range(0, nums):
    covers.append([])
    tests = input("Enter lines covered : ")
    tests = tests.split(" ")
    for j in range(0, len(tests)):
        covers[i].append(int(tests[j]))

# ----------------Changed Lines--------------------------------------------
changedLines = input("Enter changed lines : ")
changedLines = changedLines.split(" ")

for i in range(0, len(changedLines)):
    changedLines[i] = int(changedLines[i])

print("Changed Lines : ",changedLines)

coveredLines = []
# ----------------Checking Changed lines for each test cases---------------
for i in range(0, nums):
    coveredLines.append([])
    for k in covers[i]:
        if k in changedLines:
            coveredLines[i].append(k)

print("Covered Lines by each Test cases : ",coveredLines)

# -----------------Setting Priority----------------------------------------
priority = []
for i in range(0, nums):
    priority.append(len(coveredLines[i]))

print("Priority : ",priority)

#------------------Applying test cases according to their priorities-------

for i in range(0,nums):
    curr_index=find_max_index(priority)
    priority[curr_index]=0

    if(is_all_zeros(priority) or (not has_changed_lines(changedLines))):
        break

    flag=0

    for j in coveredLines[curr_index]:
        for k in range(0,len(changedLines)):
            if(changedLines[k]==j):
                flag=1
                changedLines[k]=-1

    if(flag):
        print("T",curr_index," , ",end="")
