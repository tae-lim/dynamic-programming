# Write a function `can_construct(target, word_bank)` that accepts a target
# string and an array of strings.

# The function should return the number of ways that the `target`
# can be constructed by concatenating elements of the `word_bank` array.

# You may reuse elements of `word_bank` as many times as needed

def count_construct(target, word_bank):
  if target == '': return 1

  count = 0

  for sub_str in word_bank:
    if sub_str in target and target.index(sub_str) == 0:
      suffix = target[len(sub_str):]
      count += count_construct(suffix, word_bank)

  return count

print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) # 2
print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # 1
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # 0
# print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # 4
# print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) # 0

# TC: O(n^m * m)
# SC: O(m^2)
