def user_width():
  return int(raw_input("Width? "))
def user_height():
  return int(raw_input("Height? "))
# print ("*" * w)
# for i in range(h-2):
#  print ("*" + ' '* (w-2) + "*")
# print ("*" * w)

def make_box():
  w = user_width()
  h = user_height()
  i = 1
  print ("*" * w)
  while i <= (h - 2):
    print ("*" + " " * (h - 2) + "*")
    i = i + 1
  print ("*" * w) 

make_box()