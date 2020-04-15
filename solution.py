def solution(A, B, K):

    if K <= B:
        # number of ints from B divisible by K
        c1 = B / K
        # number of ints from A divisible by K
        c2 = A / K
        # number of ints divisible between A and B
        counter = c1 - c2  

        # if counter decimal is 0.5 or above then round up, but 
        # only if B will not include any decimals above 0.5 when divided by K
        if A % K == 0 or c1 % 1 < 0.5 and counter % 1 >= 0.5:
            return int(counter) + 1
        
        # if A is divisible by K but our counter decimal is below 0.5, then
        #  we still need to count 1 up because of the former
        elif A % K == 0 and counter % 1 < 0.5:
            return int(counter) + 1
        else:
            return int(counter)  
    elif A == 0:
        return 1
    else:
        return 0

    
# Test Cases #
# Should output 12345
a = solution(101, 123456789, 10000)
print(a)

# Should output 20
b = solution(11, 345, 17)
print(b)

# Should output 2
c = solution(11, 14, 2)
print(c)