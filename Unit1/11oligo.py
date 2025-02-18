# write a function that returns the oligo melting point temperature given the number of As, Cs, Gs, Ts, in the oligo. 
def mp(A, G, T, C): # def allows you to define a function; define
    length = A + G + T + C
    if length <= 13:
        return (A + T)*2 +(G + C)*4
    else:
        return 64.9 + 41*(G + C - 16.4)/(length)
        
    

print(mp(8, 10, 3, 4)) # this is a function call; use it
print(mp(4, 2, 3, 4)) # this is a function call; use it
print(mp(26, 80, 3, 100000000)) # this is a function call; use it

#tm = (A+T)*2 +(G+C)*4
#tm = 64.9 +41*(G+C-16.4)/(A+T+G+C)