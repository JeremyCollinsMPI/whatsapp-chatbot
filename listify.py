def listify(function):
  result = []
  def wrapper_listify(*args):
    for member in args[0]:
      result.append(function(member))
    return result
  return wrapper_listify

def square(x):
  return x ** 2

sl = listify(square)

print(sl([2,3]))