# Write a function `can_sum(target_sum, numbers)` that takes in a target sum and an array of numbers as arguments.

# The function should return a boolean indicating whether or not it is possible to generate the target sum using numbers from the array.

# You may use an element of the array as many times as needed.

# You may assume that all input numbers are non-negative.

def can_sum(target_sum, numbers):
  if target_sum == 0: return True
  if target_sum < 0: return False

  for num in numbers:
    if can_sum(target_sum - num, numbers): return True

  return False

print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
# print(can_sum(300, [7, 14]))

# TC: O(n^m) where n is length of numbers and m is the value of target_sum (height of tree)
# if we could only subtract 1 from target_sum every step, we would go down linearly
# at every step, we have length of numbers branching decisions

# SC: O(m) where m is the value of target_sum (height of tree)
# we traverse one path from root to leaf node each time until all leaves are seen which means we go no more than the height of the tree
