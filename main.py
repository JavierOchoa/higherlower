from art import logo, vs
from game_data import data
import random

print(logo)

score = 0
isFinished = False

alreadyUsed = []

itemOne = random.choice(range(0, len(data)))

while not isFinished:
  itemTwo = random.choice(range(0, len(data)))
  if itemTwo in alreadyUsed:
    itemTwo = random.choice(range(0, len(data)))
  else:
    alreadyUsed.append(itemTwo)

  print(f"\n{data[itemOne]['name']}, {data[itemOne]['description']}, from {data[itemOne]['country']} has {data[itemOne]['follower_count']}M followers")
  print(vs)
  print(f"{data[itemTwo]['name']}, {data[itemTwo]['description']}, from {data[itemTwo]['country']}\n")

  guess = input(f"Do you think that {data[itemTwo]['name']} has more followers? (y/n)").lower()

  if guess == "y":
    if data[itemTwo]["follower_count"] > data[itemOne]["follower_count"]:
      score += 1
      itemOne = itemTwo
    elif data[itemTwo]["follower_count"] < data[itemOne]["follower_count"]:
      print(f"\nYou lose, your score is {score}")
      isFinished = True
  elif guess == "n":
    if data[itemTwo]["follower_count"] < data[itemOne]["follower_count"]:
      score += 1
      itemOne = itemTwo
    elif data[itemTwo]["follower_count"] > data[itemOne]["follower_count"]:
      print(f"\nYou lose, your score is {score}")
      isFinished = True