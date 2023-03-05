# python3

import sys
import threading
import numpy


def compute_height(n, parents, masss,Alex,S):
    # Write this function
    if (Alex[n]==1):
        return S[n]
    else:
        Alex[n]=1
        if(parents!=-1):
            max_height = 1+compute_height(parents, masss[parents], masss,Alex,S)
            S[n]=max_height
        else:
            max_height=1
            S[n]=1
    
    # Your code here
        return max_height


def main():
    Alex=[] #we was here
    S=[]    #size
    # implement input form keyboard and from files
    com=input()
    TF = False
    if ("I" in com):
        n=int(input())
        masss=[int(i) for i in input().split()]
        TF = True
    
    if ("F" in com):
        T="test/"+input()
        if not("a" in T):
            TF=True
            with open(T) as file:
                n=int(next(file))
                for line in file:
                    masss=[int(i) for i in line.split()]
    
    if (TF):
        sus=0 #min
        for i in range(0, n, 1):
            Alex.append(0)
            S.append(0)
        
        for i in range(0, n, 1):
            imum = compute_height(i, masss[i], masss,Alex,S)
            if(sus<imum):
                sus=imum

        print(sus)



    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))