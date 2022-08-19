# Write a function `can_construct(target, word_bank)` that accepts a target
# string and an array of strings.

# The function should return a 2D array containing all of the ways that the
# `target` can be constructed by concatenating elements of the `word_bank`
# array. Each element of the 2D array should represent one combination that
# constructs the `target`.

# You may reuse elements of `word_bank` as many times as needed

def all_construct(target, word_bank, curr, res):
  if target == '':
    res.append(curr)



  for sub_str in word_bank:
    if sub_str in target and target.index(sub_str) == 0:
      clone = list(curr)
      clone.append(sub_str)
      suffix = target[len(sub_str):]
      all_construct(suffix, word_bank, clone, res)

  return res






print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], [], [])) # 2
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], [], [])) # 1
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], [], [])) # 0
print(all_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], [], [])) # 4
# print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], [], [])) # 0
