import random
r = random.randint(1, 100)
while True:
	a = input('請輸入隨機數字')
	a = int(a)
	if a == r:
		print('恭喜猜對！')
		break
	elif a > r:
		print('小一點')
	elif a < r:
		print('大一點')