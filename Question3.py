# 3 Question

def maxConsecutive(list, n):
    count=0 
    maximum=0  
    for i in range(0, n):      
        if (list[i] == 0):
            count=0
        else:
            count=count+1 
            maximum=max(maximum, count) 
          
    return maximum

    
list =[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
#list=eval(input("Enter the List  0's  and  1's  form:"))  
n = len(list) 
print("Maximum Consecutive is = ",maxConsecutive(list, n))
