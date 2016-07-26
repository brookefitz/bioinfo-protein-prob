import re

f = open('/tmp/assemble', 'r')
m = f.readlines()
max = 0
test = ["BANANA", "APPLE", "ORANGE"]

#ignore this function
def MCSeq(num, seq):
  if (num > max):
    max = num
    topSeq = seq
  elif (num == max):
    topSeq += seq
  
#important stuff starts here :)
#counts the number of occurences
def seqCount(seq, list):
  sum = 0
  for i in range(0, len(list)):
    s = list[i].rstrip()
    new = len(re.findall(seq, s))
    sum = sum + new
  print seq, " = ", sum

#first for loop splits list into separate strings
#second for loop splits strings into substrings
def printSeq(list):
  for j in range(0, len(list)):
    substr = list[j]
    for k in range(0, len(substr)-1):
      k2 = k + 2
      temp = substr[k:k2]
      seqCount(temp, list)

#runs whole program
printSeq(test)
