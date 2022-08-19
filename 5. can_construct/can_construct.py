# Write a function `can_construct(target, word_bank)` that accepts a target
# string and an array of strings.

# The function should return a boolean indicating whether or not the `target`
# can be constructed by concatenating elements of the `word_bank` array.

# You may reuse elements of `word_bank` as many times as needed

def can_construct(target, word_bank, s):
  if s == target: return True
  if len(s) > len(target): return False

  for sub_str in word_bank:
    if can_construct(target, word_bank, s+sub_str): return True

  return False


#



# print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], '')) # true
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], '')) # false
# print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], '')) # true
# print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], '')) # false

# TC: O(n^m * m)
# SC: O(m^2)
