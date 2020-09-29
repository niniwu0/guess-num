import random

start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)

r = random.randint(start,end)
count = 0
while True:
	count += 1 #count = count + 1
	ans = input('請猜數字,你的答案是: ')
	ans = int(ans)
	if ans == r:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif ans > r:
			print('答案比你猜的還小，再加油')
	elif ans < r:
			print('答案比你猜的還大，再加油')
	print('這是你猜的第', count, '次')