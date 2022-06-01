"""
    Name: Byron Dowling
    Class: 4143 Programming Techniques
    Date: 10/25/2021

    To-Do List:
        - printing string indexes
        - string compare
        - Lists
            - printing list with index
            - printing list without index
            - Heterogenous vs Homogenous Lists

        - Convert Java spiral matrix to Python
"""


## - sri    = starting row index 
## - max_ri = ending row index 
## - sci    = starting column index 
## - max_ci = ending column index 

def spiralArray(max_ri, max_ci, matrix) : 
    sri = 0
    sci = 0

    while (sri < max_ri and sci < max_ci) : 

        for i in range(sci, max_ci) : 
            print(matrix[sri][i], end = " ") 

        sri += 1

        for i in range(sri, max_ri - 1) : 
            print(matrix[i][max_ci - 1], end = " ") 

        max_ci -= 1


        if ( sri < max_ri) : 

            for i in range(max_ci - 1, sci, -1) : 
                print(matrix[max_ri - 2][i], end = " ") 

            max_ri -= 1


        if (sci < max_ci) : 
            for i in range(max_ri - 1, sri - 1, -1) : 
                print(matrix[i][sci], end = " ") 

            sci += 1



## Square Matrix/2D array to be passed in 
sqr_matrix = [ [1, 2, 3, 4, 5, 6, 7, 8], 
                [9, 10, 11, 12, 13, 14, 15, 16], 
                [17, 18, 19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30, 31, 32],
                [33, 34, 35, 36, 37, 38, 39, 40],
                [41, 42, 43, 44, 45, 46, 47, 48],
                [49, 50, 51, 52, 53, 54, 55, 56], 
                ] 

## Matrix Dimensions
Row = 8
Col = 8

## Calling the function to print the spiral array
spiralArray(Row, Col, sqr_matrix)
print('\n')


mes = "It's all good in the hood"
mess = "It'sallgoodinthehood"
messs = " but in reality there were many socio-economic problems in the hood"

## Print the Message
print(mes)

## Print the message in chunks
print(mes[0:4])
print(mes[5:8])
print(mes[9:13])
print(mes[14:16])
print(mes[17:20])
print(mes[21:25])


## String concatenation
mes = mes + messs
print(mes)


## String should not be equal here
if mes == mess:
    print("strings are equal")

else:
    print("strings are not equal")


## After replacing the whitespace, the strings should now be equal
new = mes.replace(" ", "")

if new == mess:
    print("strings are equal")

else:
    print("strings are not equal")



## List Stuff

List1 = []      ## New Empty List
List2 = [1, 2, 3, 4, 5]
List3 = ['Mercedes', 'AMG', 'C', 63, 6.0, 469]
List4 = [6,7,8,9,10]

print("Length of List 2 is:", len(List2))

## Print the Whole List at a time
print(List2)
print(List3)


## Print the list by individual index
## This method is useful if we need to know the index
for index in range(0, len(List2), 1):
    print(List2[index])


print('\n')

## Printing the list without range
for x in List2:
    print(x)

for i in range(0, len(List2), 1):
    val = List2[i] + List4[i]
    print(val)
    
    List1.append(val)
    print(List1)


