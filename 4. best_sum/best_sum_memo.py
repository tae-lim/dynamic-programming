# Write a function that returns an array containing the shortest combination of numbers that add up to target sum.

# If there is a tie for the shortest combination, you may return one of the shortest



def best_sum(target_sum, numbers, hash):
  if target_sum in hash: return hash[target_sum]
  if target_sum == 0: return []
  if target_sum < 0: return None

  best = None

  for num in numbers:
    curr = best_sum(target_sum - num, numbers, hash)
    if isinstance(curr, list):
      copy = list(curr)
      copy.append(num)
      if not best or len(curr) < len(best): best = copy

  hash[target_sum] = best
  return best




# print(best_sum(7, [5, 3, 4, 7], {}))
# print(best_sum(8, [2, 3, 5], {}))
print(best_sum(8, [1, 4, 5], {}))
# print(best_sum(100, [1, 2, 5, 25], {}))

# TC: O(n*m*m)
# SC: O(m^2)
