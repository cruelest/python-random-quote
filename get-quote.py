import random


def mainnn():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)
  rnd = random.randint(0, last)

  print(quotes[rnd].strip())

if __name__== "__main__":
  mainnn()
