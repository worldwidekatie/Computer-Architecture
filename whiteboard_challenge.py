# Given the following array of values, 
# print out all the elements in reverse order, 
# with each element on a new line.
# For example, given the list
ls = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# Your output should be
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before 
# writing any code. Run through the UPER problem solving 
# framework while going through your thought process.

# could use ls.reverse()

#ls.reverse()
# for i in ls:
#     print(i)

for i in ls[::-1]:
    print(i)

"""Stretch Goal"""
# Given a hashmap where the keys are integers, 
# print out all of the values of the hashmap in 
# reverse order, ordered by the keys.
# For example, given the following hashmap:
data = {
  14: "vs code",
  3: "window",
  9: "alloc",
  26: "views",
  4: "bottle",
  15: "inbox",
  79: "widescreen",
  16: "coffee",
  19: "tissue",
}
# The expected output is:
# widescreen
# views
# tissue
# coffee
# inbox
# vs code
# alloc
# bottle
# window
# since "widescreen" has the largest integer key, 
# "views" has the second largest, etc.
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible 
# before writing any code. Run through the UPER problem 
# solving framework while going through your thought process.
# keys = []
# for i in data:
#     keys.append(i)

keys = sorted(data)
keys.reverse()

for i in keys:
    print(data[i])


