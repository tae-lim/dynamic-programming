def fib(n, memo={}):
  if n in memo: return memo[n]
  if n <= 2:
    memo[n] = 1
    return memo[n]

  memo[n] = fib(n-1, memo) + fib(n-2, memo)
  return memo[n]


print(fib(60))


# TC: O(n)
# Items weve memoized are stored in cache so we dont need to go through individual subtrees weve already processed

# SC: O(n)
# Goes from root to leaf nodes and nodes are popped from the call stack to reach other leaf nodes which maintains linear space
