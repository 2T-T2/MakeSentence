def index_Multi(List,liter):
  #Listはリスト本体・literは検索したい文字
  index_L = []
  for val in range(0,len(List)):
    if liter == List[val]:
      index_L.append(val)
  return index_L