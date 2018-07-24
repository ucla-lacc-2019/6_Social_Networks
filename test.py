from LACC2018_Solution import matrix_load,print_degrees,shortest_path,detect_cycle
mat1=matrix_load("matrix.txt")
print_degrees(mat1)
shortest_path(mat1,1,4)
detect_cycle(mat1)

mat2=matrix_load("matrix2.txt")
print_degrees(mat2)
shortest_path(mat2,2,4)
detect_cycle(mat2)

mat3=matrix_load("matrix3.txt")
print_degrees(mat3)
shortest_path(mat3,3,4)
detect_cycle(mat3)