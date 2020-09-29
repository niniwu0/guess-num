import random

r = random.randint(1,100)
while True:
	ans = input('請猜數字,1~100,你的答案是: ')
	ans = int(ans)
	if ans == r:
		print('終於猜對了!')
		break
	elif ans > r:
			print('答案比你猜的還小，再加油')
	elif ans < r:
			print('答案比你猜的還大，再加油')
