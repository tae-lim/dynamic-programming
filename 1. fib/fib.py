def fib(n):
  if n <= 2: return 1
  return fib(n-1) + fib(n-2)

print(fib(3))
print(fib(8))

# TC: 2^n
# the depth of the tree is n and at every node, we have 2 paths. The depth is the exponent and the branches are the number of decisions

# SC: O(n)
# we traverse through the leftmost depth and as we reach the leaf, we pop out nodes to reach the depth of another leaf and so on.
