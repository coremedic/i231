## i231 coin flip program ##
import random

num_flips = 0
num_heads = 0
num_tails = 0

while True:
    coin = random.randint(0, 1)
    if coin == 0:
        num_heads += 1
        print("heads: ", int(num_heads / (num_heads + num_tails) * 100),"%")
    else:
        num_tails += 1
        print("tails: ", int(num_tails / (num_heads + num_tails) * 100),"%")
    num_flips += 1
    if (num_heads / num_flips * 100) > 48 and (num_heads / num_flips * 100) < 52 or (num_tails / num_flips * 100) > 48 and (num_tails / num_flips * 100) < 52:
        break

print(f"Total heads: {num_heads}")
print(f"Total tails: {num_tails}")
print(f"Total flips: {num_flips}")