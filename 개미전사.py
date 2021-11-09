def ant(n, food):
	food_max = 0
	for i in range(2, n):
		food[i] = food[i]+food[i-2]
	print(max(food))
n = int(input())
food = list(map(int, input().split()))
ant(n, food)
