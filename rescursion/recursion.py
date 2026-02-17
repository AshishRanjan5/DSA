"""
Print 1 to N using recursion
"""

def print1toNRecursion(N, i: int = 1):
    if i > N:
        return
    
    print(i)
    print1toNRecursion(N, i+1)


"""
Print N to 1 using recursion
"""

def printNto1Recursion(N):
    if N < 1:
        return
    
    print(N)
    printNto1Recursion(N-1)


"""
Print 1 to N using Backtracking
"""
def print1toNBacktracking(i, N):
    if i < 1:
        return
    
    print1toNBacktracking(i-1, N)
    print(i)


"""
Print N to 1 using Backtracking
"""
def printNto1Backtracking(i, N):
    if i > N:
        return
    
    printNto1Backtracking(i+1, N)
    print(i)


"""
Sum of N numbers using recursion
"""

def sumOfN_NaturalNumbersusingRecursion(N):
    
    if N == 0:
        return 0
    
    return N + sumOfN_NaturalNumbersusingRecursion(N-1)

"""
Reverse an array using Recursion
"""

def reverseArrayUsingRecursion(A, left, right):
     if left == right:
         return A
     
     A[left], A[right] = A[right], A[left]
     return reverseArrayUsingRecursion(A, left + 1, right - 1)
         
"""
Check if String is Palindrome using recursion
"""

def checkPalindromeUsingRecursion(S, left, right):
    if left >= right:
        return True
    
    if S[left] != S[right]:
        return False
    
    
    return checkPalindromeUsingRecursion(S, left+1, right-1)
    
    


if __name__ == "__main__":
    N = 5
    print("\nPrint 1 to N using recursion")
    print1toNRecursion(N)
    print("\nPrint N to 1 using recursion")
    printNto1Recursion(N)

    print("\nPrint 1 to N using backtracking")
    print1toNBacktracking(N, N)

    print("\nPrint N to 1 using Backtracking")
    printNto1Backtracking(1, N)

    print("\nSum of N numbers using recursion")
    print(sumOfN_NaturalNumbersusingRecursion(N))

    print("\nReverse an array using Recursion")
    A = [2,4,4,2,1]
    print(reverseArrayUsingRecursion(A, 0, len(A)-1))

    print("\nCheck Palindrome using Recursion")
    S = "MADAM"
    print("Palindrome" if checkPalindromeUsingRecursion(S, 0, len(S)-1) else "Not a Palindrome")


