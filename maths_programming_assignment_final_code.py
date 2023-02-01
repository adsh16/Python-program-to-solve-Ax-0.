def rref(M):
    m = len(M)
    n = len(M[0])
    l = 0
    for r in range(m):
        if l >= n:
            return M
        i = r
        while M[i][l] == 0:
            i += 1
            if i == m:
                i = r
                l += 1
                if n == l:
                    return M
        M[i], M[r] = M[r], M[i]
        lv = M[r][l]
        M[r] = [x / lv for x in M[r]]
        for i in range(m):
            if i != r:
                lv = M[i][l]
                M[i] = [M[i][j] - lv * M[r][j] for j in range(n)]
        l += 1
    return M
def pivot_positions(M):
    r_m = rref(M)                                          #taking rref matrix from previous function
    m = len(M)
    n = len(M[0])
    pivot_positions = []
    for i in range(m):                                     #looping through the matrix and noting down the index of first non-zero element(1 for rref   )
        for j in range(n):
            if r_m[i][j] == 1:
                pivot_positions.append((i, j))             #appending the coordiantes with base coordinates(origin (0,0) instead of (1,1))
                break
    return pivot_positions
def column_of_free_variables(l):
    l1=[i for i in range(len(l[0]))]
    l2=[i[1] for i in pivot_positions(l) ]
    l3=[]
    for i in l1:
        if i not in l2:
            l3.append(i)
    return l3  # returns a list having column no. with no pivot points
def parametric_solution(l,a,b,c):
    temp = []                                   #creating an empty 2-D nested list
    for i in c:
        list = [0 for j in range(len(l[0]))]
        # list[i]=1                            # making an empty list with [0,0,0,0.....]
        temp.append(list)
    count1 = 0                                 # for the list no.
    for i in c:
        count2=0                              # for the element no. in list
        for k in a:                           # switching signs of all other values in the corresponding column of the rref
            temp1 = -(k[i])
            if temp1 == 0.0:
                temp[count1][count2]=(-temp1)
            else:
                temp[count1][count2]=(temp1)
            count2+=1
        count1+=1
    for i,j in zip(temp,c):
        i[j]=1
    return temp
def printing_solution(temp,c):
    print("x = [0,0,...] + ", end="")
    for i,j in zip(temp,c):
        print("x({}){}".format(j,i),end= " + ")

l = [[1, -2, -1, 3, 0],[-2, 4, 5, -5, 3],[3, -6, -6, 8, 2]]             # input matrix
a = rref(l)                                                             # rref matrix
b = pivot_positions(l)                                                  # containing coordinates of pivot columns((0,0) as the origin of (1,1))
c = column_of_free_variables(l)                                         # contaning column nos. with free variable (starting from 0)
d = parametric_solution(l,a,b,c)
print("The RREF is : ")
for i in a:
    print(i)
print("The pivot points are : " , b)
print("The columns with free variables are : ",c)
printing_solution(d,c)

