# Write a function `can_sum(target_sum, numbers)` that takes in a target sum and an array of numbers as arguments.

# The function should return a boolean indicating whether or not it is possible to generate the target sum using numbers from the array.

# You may use an element of the array as many times as needed.

# You may assume that all input numbers are non-negative.


def can_sum(target_sum, numbers, memo):
  if target_sum in memo: return memo[target_sum]
  if target_sum == 0: return True
  if target_sum < 0: return False

  for num in numbers:
    if can_sum(target_sum - num, numbers, memo):
      memo[target_sum] = True
      return True

  memo[target_sum] = False
  return False

print(can_sum(7, [2, 3], {}))
print(can_sum(7, [5, 3, 4, 7], {}))
print(can_sum(7, [2, 4], {}))
print(can_sum(8, [2, 3, 5], {}))
print(can_sum(300, [7, 14], {}))


# TC: O(m*n), where m = target_sum and n = len(numbers)
# for every level in m, we have a for loop that iterates through length of n

# SC: O(m), where m is height of the tree
