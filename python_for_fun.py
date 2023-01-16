
## Source: http://openbookproject.net/py4fun/dynamic/dynamic.html
## Learned on 16 Jan 2023 


# The Fibonacci sequence
def fibonacci_ori(n):
    if n < 2: return n 
    else: return fibonacci_ori(n-1) + fibonacci_ori(n-2)

known = {}
def fibonacci_opt(n):
    ans = known.get(n,None)
    if ans: return ans
    elif n < 2: return n 
    else: 
        ans = fibonacci_opt(n-2) + fibonacci_opt(n-1)
        known[n] = ans
    return ans
    
if __name__ == "__main__":
    print(fibonacci_opt(50))
    for i in range(10,-1,-1):
        print(i)



# Finding an optimum contiguous sequence

