
import re
from random import randint
def dice(message):
  if re.match('\dD\d\d\d',message.content):
    result=re.match('\dD\d\d\d',message.content).group()
  elif re.match('\dD\d\d',message.content):
    result=re.match('\dD\d\d',message.content).group()
  elif re.match('\dD\d',message.content):
    result=re.match('\dD\d',message.content).group()
  rstring=[]
  for a in range(int(result[0])):
    rstring.append(randint(1,int(result[2:])))
  tostring1=[str(i) for i in rstring]
  return ','.join(tostring1)
