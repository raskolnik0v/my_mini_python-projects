#repeater of number

"""
********************************

num = [1, 4, 4]
tekrar_sayısı = num.count(max(num, key = num.count))
tekrar_sayısı

# 3 rakam için en büyüğünün kaç kez tekrar ettğini buluyor
*******************************
def equal(x,y,z):
  num =[x,y,z]
  sonuc = num.count(max(num, key = num.count))

  if sonuc > 1 :
    return sonuc
  else :
    return 0
*********************************
    #artık  istediğimiz kadar eleman yollaya biliriz içine x,y,z li 3 lü değişkenliyi iterable olan  * arg çevirdik 
def equalll(* arg):
  num = list(arg)
  sonuc = num.count(max(num, key = num.count))

  if sonuc > 1 :
    return sonuc
  else :
    return 0
  **********************************
  #lambda versionu

equallambda = lambda x,y,z : [x,y,z].count(max([x,y,z], key = [x,y,z].count))
**************************

#ifli versiyonu yani tekrar eden yoksa 0 döndürsün
#ternary yani belli sayıda değişken sokma
equalllambda = lambda x,y,z : [x,y,z].count(max([x,y,z], key = [x,y,z].count))\
 if [x,y,z].count(max([x,y,z], key = [x,y,z].count)) > 1 else 0

 *********************************
 #arbitrary istediğimiz kadar değişken sokabilmek için 
equallllambda = lambda * x :list(x).count(max(list(x), key = list(x).count))\
if list(x).count(max(list(x), key = list(x).count)) > 1 else 0 



*********************************
"""

#arbitrary istediğimiz kadar değişken sokabilmek için --- list(x) i sadece x yapınca da oldu

equallllambda = lambda * x :x.count(max(x, key = x.count))\
if x.count(max(x, key = x.count)) > 1 else 0

equallllambda(7,8,8,8,9,11)
