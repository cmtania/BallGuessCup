# there are three cups on a table, at positions a, b, and c. at the start, 
# there is a ball hidden under the cup at position b. however, 
# I perform several swaps on the cups, which are notated as two letters. 
# for example, if i swap the cups at positions a and b, i could notate this as ab or ba. 
# create a function that returns the letter position that the ball is at, once i finish swapping the cups. 
# the swaps will be given to you as an array.

swaps = ["BA","AC","BA"]

cups = ["A", "B", "C"]
counter = 0

def swapBall(notation):
    replaceLetter(cups.index(notation[0]),cups.index(notation[1]), notation[0], notation[1])
      
def replaceLetter(first_index, second_index, first_letter, second_letter):
    cups[first_index] = second_letter
    cups[second_index] = first_letter
    if(counter == len(swaps)):
      getBall()

def getBall():
    print("The ball is at letter " + ballLocation(cups.index("B")))

def ballLocation(index):
  if index == 0:
    return "A"
  elif index == 1:
    return "B"
  else:
    return "C"

for x in swaps:
  counter = counter + 1
  swapBall(x)
