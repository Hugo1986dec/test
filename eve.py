driving = input('請問你有開過車嗎？')
if driving != '有' and driving != '沒有':
   print('來亂的') 
   raise SystemExit

age = input('請輸入你的年齡')
age = int(age)
if driving == '有':
   if age >= 18:
      print('你可以合法上路')
   else:
      print('你違法了')   
elif driving == '沒有':
   if age >= 18:
      print('嫩逼')
   else:
      print('乖') 

   