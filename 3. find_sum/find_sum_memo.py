def find_sum(target_sum, numbers, hash):
  if target_sum in hash: return hash[target_sum]
  if target_sum == 0: return []
  if target_sum < 0: return None

  for num in numbers:
    curr = find_sum(target_sum - num, numbers, hash)
    hash[target_sum] = curr
    if isinstance(curr, list):
      curr.append(num)
      return hash[target_sum]

  return None

print(find_sum(7, [2, 3], {}))
print(find_sum(7, [5, 3, 4, 7], {}))
print(find_sum(7, [2, 4], {}))
print(find_sum(8, [2, 3, 5], {}))
print(find_sum(300, [7, 14], {}))

# n = len(numbers)
# m = target_sum

# TC: O(n*m)
# SC: O(m)
