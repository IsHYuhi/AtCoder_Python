import re
W = input()
#W = W.replace('a','')
print(re.sub('a|i|u|e|o', '', W))