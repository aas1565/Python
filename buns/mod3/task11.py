matrix=[list(map(str, input().split())) for row in range (int(input('N= ')))]

column=[]

for column_index in range (len(matrix[0])):
    for row in matrix:
        column.append((row[column_index]))

    if all(element== column[0] and element=='X' for element in column):
        print("X")
        break
    elif all(element== column[0] and element=='Y' for element in column):
        print("Y")
        break

for row in matrix:
    if all(element==row[0] and element=='X' for element in row):
        print("X")
        break
    elif all(element==row[0] and element=='Y' for element in row):
        print("Y")
        break

print(*matrix, sep='\n')










