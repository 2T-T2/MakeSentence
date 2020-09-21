import json
import random

from mylib.index_Multi import index_Multi

class marcov:
  def __init__(self):
    self.dic = {}
    
  def loadDic(self,filePath):
    with open(filePath,"r") as f:
      self.dic = json.loads(f.read())

  def makeSentence(self,firstword=""):
    if firstword == "":
      firstword = random.choice(self.dic["firstWord"])
    sentence = firstword
    if firstword in self.dic["firstWord"]:
      word = random.choice(self.dic[firstword])
      while not(word == "。\n"):
        sentence = sentence + word
        word = random.choice(self.dic[word])
    else:
      word = random.choice(self.dic[random.choice(self.dic["firstWord"])])
      while not(word == "。\n"):
        sentence = sentence + word
        word = random.choice(self.dic[word])
    return sentence + "。"

  def loadCsv(self,filePath):
    csv = []
    cnt = 0

    with open(filePath,encoding="shift-jis") as f:
      for line in f:
        csv.append(line.split(","))
      
    firstwords = []
    unique = []
    notunique = []
    for line in csv:
      unique = unique + line
      notunique = notunique + line
      firstwords.append(line[0])

    unique = list(set(unique))
    for uni in unique:
      indexlist = index_Multi(notunique,uni)
      for index in indexlist:
        if not(notunique[index] == "。") and not(notunique[index] == "\n") and not(notunique[index + 1] == "\n"):
          self.dic.setdefault(uni,[]).append(notunique[index + 1])

    for firstword in firstwords:
      if not(firstword == "\n"):
        self.dic.setdefault("firstWord",[]).append(firstword)

  def saveDic(self,filePath):
    with open(filePath, "w") as f:    
      json.dump(self.dic,f,ensure_ascii=False,indent=4)
