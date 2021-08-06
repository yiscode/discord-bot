
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
def dice_level(message):
  level_list = ['EX','S','A','B','C','D','E']
  return level_list[randint(0,6)]