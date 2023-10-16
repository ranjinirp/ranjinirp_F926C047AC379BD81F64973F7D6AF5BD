def                              linearSearchProduct(productlist,target Product):
  indices=[]

  for index, product in             enumerate(Productlist):
      if product == targetProduct:
          indices.append(index)

  return indices


products=                    ["shoes","boot","loafer","shoes","sandal","shoes"]
target=" shoes"
result=linearSearchProduct(products,target)
print(result) 