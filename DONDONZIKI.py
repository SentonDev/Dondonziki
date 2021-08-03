import random

while True:
	t=('quduq','qaychi','qopqoq')
	k = random.choice(t)
	p =None

	while p not in t:
		p = input("\n>>>  ").lower()

	if k==p:
		print('AI: ', k)
		print("DURRANG!")
	
	elif p == 'quduq':
		if k=='qaychi':
			print('k: ', k)
			print("YUTDINGIZ!")
		elif k== 'qopqop':
			print('AI: ', k)
			print("YUTQAZDINGIZ!")
		
	elif p=='qaychi':
		if k == 'quduq':
			print('AI: ', k)
			print("YUTQAZDINGIZ!")
		elif k =='qopqoq':
			print('AI: ', k)
			print("YUTDINGIZ!")
		
	elif p=='qopqoq':
		if k=='qaychi':
			print('AI: ', k)
			print("YUTQAZDINGIZ!")
		elif k=='quduq':
			print('AI: ', k)
			print("YUTQAZDINGIZ!")
			
	yana = input("\nyanami? (ha/yoq) >>>   ").lower()
	if yana != "ha":
		break