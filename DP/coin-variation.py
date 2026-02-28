coins = [1, 2, 5]
target = 11

N = len(coins)

def RecursiveApproach(coins, N, target) -> int:
    # Base Condition
    if target == 0:
        return 0
    
    if N == 0:
        return float('inf')
    
    if coins[N-1] <= target:
        return min(
                    1 + RecursiveApproach(coins, N, target-coins[N-1]),
                    RecursiveApproach(coins, N-1, target)
                   )
    else:
        return RecursiveApproach(coins, N-1, target)
    

dp = [[float('inf') for _ in range(target+1)] for _ in range(N+1)]

def RecursiveApproachwithMemoize(coins, N, target):
    #Base condition
    if N == 0:
        return float('inf')

    if target == 0:
        return 0
    
    if dp[N][target] != -1:
        return dp[N][target]
    
    if coins[N-1]<=target:
        dp[N][target] = min(
                        1+RecursiveApproachwithMemoize(coins, N, target-coins[N-1]),
                        RecursiveApproachwithMemoize(coins, N-1, target)
                        )
        
    else:
        dp[N][target] = RecursiveApproachwithMemoize(coins, N-1, target)

    return dp[N][target]

def TopDownApproach(coins, N, target):
    # Initialization
    for i in range(N+1):
        for j in range(target+1):
            dp[0][j] = float('inf')
            dp[i][0] = 0

    for i in range(1, N+1):
        for j in range(1, target+1):
            if coins[i-1] <= j:
                dp[i][j] = min(
                    1+dp[i][j-coins[i-1]],
                    dp[i-1][j]
                )
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[N][target]
            

if __name__ == "__main__":
    print(RecursiveApproach(coins, N, target))
    #print(RecursiveApproachwithMemoize(coins, N, target))
    print(TopDownApproach(coins, N, target))
    print(dp)
