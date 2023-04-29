# Python-program-to-solve-Ax=0.
A python program to find the solution for Ax=0 and then represent them in parametric form without using external libraries/modules.
The attached file with python contains various function namely : 
1. rref() : 
- parameters : a 2-d list representing the matrix
- used for finding the reduced-row-eechlon form the matrix
- return : returns a 2-d list represting a matrix with is row-equivalent the passed matrix
2. pivot_positions():
- parameters : a 2-d list representing a matrix which is in row-reduced-eechlon form
- used for find the coordinates of pivots in a row-reduced matrix.
- return : a 2-d list containg the coordinates of pivot-positions(first non-zero entry in a row) in the matrix.
3. column_of_free_variable():
- parameters : a 2-d list containg the coordiantes of pivot positions
- used : for finding the column no. of columns which have no pivot and thus correspond to free-variable
- return : a list containg column no. of free variables
4. parametric_solution():
- parameters : - l : originial input list(hard-coded for this code)
               - a : a 2-d list containg the row-reduced eechlon form of the matrix
               - b : a 2-d list containg the coordinates of pivot position in row-reduced matrix
               - c : a list containg column_no. of columns with no pivots
- used for find the parametric solution.
- return : a 2-d list containg the corresponding matrix for each free variable
5. printing_solution():
 - parameters : - temp : 2-d list containing column matrices which are part of parametric solution corresponding to the free variables.
                - c : the free-variable no. corresponding to the matrices in temp.
- used : for combining outputs for various functions are then printing the output in desired form.
- return : NONE


NOTE : 
1. This function,{parametric_solution()}, finds out the column matrices correponding to the free variable by inverting the sign of entries in the rref matrix.And then, it makes the entry=1 in the matrix correspond to the free variable no.
2. All the functions are written synchronously because they are used one after another.
3. There is no GUI attached to this code.Therefore, changes have to be made in the code itself in main function. Comments have been added in the code for the same.

