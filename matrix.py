def extended_gcd(a : int, b : int):

    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while(r):
        quotient = old_r//r
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t

    return old_r, old_s, old_t

def mod_inverse(a : int, m : int):

    gcd, x, y = extended_gcd(a, m)
    if(gcd!=1):
        raise ValueError
    else:
        return x%m
    
def mat_mul_mod(A : list[list[int]], B : list[list[int]], m : int):

    if(len(A[0]) != len(B)):
        raise ValueError
    
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                C[i][j] = (C[i][j]+A[i][k]*B[k][j])%m
    
    return C

def mat_inv_mod(A : list[list[int]], m : int):
    n = len(A)
    aug = [A[i][:] + [1 if i==j else 0 for j in range(n)] for i in range(n)]

    for i in range(n):
        correct_row = i
        if extended_gcd(aug[i][i], m)[0] != 1:  
            for k in range(i + 1, n):
                if extended_gcd(aug[k][i], m)[0] == 1:
                    correct_row = k
                    break
        
        aug[i], aug[correct_row] = aug[correct_row], aug[i]

        pivot = aug[i][i]
        if extended_gcd(pivot, m)[0]!=1:
            raise ValueError
        
        for j in range(0, len(aug[0])):
            aug[i][j] = aug[i][j]*mod_inverse(pivot, m)%m

        for k in range(n):
            if(k!=i):
                factor = aug[k][i]
                for j in range(0, len(aug[0])):
                    aug[k][j] = (aug[k][j] - factor*aug[i][j])%m

    return [row[n:] for row in aug]
    
