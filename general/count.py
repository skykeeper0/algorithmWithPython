fruits = ['apple','orange','apple','banana']

def count(l):
  count = {}
  for item in l:
    if item in count:
      count[item] = count[item] + 1
    else:
      count[item] = 1

  return count

print(count(fruits))