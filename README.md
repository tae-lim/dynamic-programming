# dynamic-programming

## Brute Force

Time Complexity: Branching Decisions ^ Height of the tree

## Memoization Recipe

1. Make it work
  - visualize the problem as a tree
  - implement the tree using recursion
  - test it (can be slow at first)

2. Make it efficient
  - add a memo object
  - add a base case to return memo values
  - store return values into the memo

## Tabulation Recipe
  - visualize the problem as a table
  - size the table based on the inputs
  - intialize the table with default values (0 / 1 / True / False)
  - seed the trivial answer into the table
  - iterate through the table
  - fill further positions based on the current position
