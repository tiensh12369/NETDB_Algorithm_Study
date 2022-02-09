
T = int(input())
sudoku_2d = []
for test_case in range(1, T + 1):
    for i in range(9):
        sudoku_1d = list(map(int, input().split(" ")))
        if len(sudoku_1d) != len(set(sudoku_1d)):
            print(f'#{test_case} 0')
            break
        else:
            sudoku_2d.append(sudoku_1d) 
    print(sudoku_2d)