#from colorama import Fore

triangle = [ [75],
             [95, 64],
             [17, 47, 82],
             [18, 35, 87, 10],
             [20, 4, 82, 47, 65],
             [19, 1, 23, 75, 3, 34],
             [88, 2, 77, 73, 7, 63, 67],
             [99, 65, 4, 28, 6, 16, 70, 92],
             [41, 41, 26, 56, 83, 40, 80, 70, 33],
             [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
             [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
             [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
             [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
             [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
             [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] ]
smol = [ [3], [7, 4], [2, 4, 6], [8, 5, 9, 3] ]
path = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

sum = 0
max = 0
prev_inx = 0

for x in range(len(triangle)):
    for y in range(len(triangle[x])):
        flag = 0
        try:
            if y == prev_inx:
                if triangle[x][y] >= max:
                    max = triangle[x][y]
                    flag = 1

                if triangle[x][y+1] >= max:
                    max = triangle[x][y+1]
                    flag = 2

                if flag == 1:
                    prev_inx = y
                elif flag == 2:
                    prev_inx = y+1
                else:
                    exit(1)
                break
        except:
            print(end="")
    path[x] = max
    print("adding ", max, " to sum at index ", prev_inx)
    sum = sum + max
    max = 0

print("\n", sum)

print(path)

z = 0
for row in triangle:
    for num in row:
        if num == path[z]:
            #print(Fore.RED + str(num), end="")
            print("No", end="")
        else:
            print(num, end=" ")
    z = z + 1
    print()
