T = int(input())

def ab(N):
    ab = 'No'
    for i in range(1, 10):
        if N%i == 0 and N//i < 10:
            print(N, i)
            ab = 'Yes'
    return ab
            
for TC in range(1, T + 1):
    N = int(input())
    yn = ab(N)
    
    print(f'{TC} {yn}')