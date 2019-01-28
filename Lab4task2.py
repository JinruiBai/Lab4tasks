def word_count(book):
  book = open("text")
  line = book.readline()
  word = line.split()
  my_dict = {}
  total = 0
  for item in book:
    total += 1
    my_dict[item] = item.count(item)
  print(my_dict)
  print(total)

def most_common(my_dict):
  t = []
  for key, value in my_dict.item():
    t.append((value,key))
    t.sort(revese = True)
print(t)
