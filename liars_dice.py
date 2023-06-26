#Need:
#20 dice randomly assigned value 1-6 - CHECK
#be able to see 5 dice to start - CHECK
#input to be able to make a guess - CHECK
#AI opponents (3 of them, each making their own guesses)
#Constraints that ensure each bet increases from the previous bet
#At the end of a round, player who lost their bet loses 1 die, and total dice decreases by 1
#Game ends when only human players has dice remaining or when human player loses all 5 dice



#Next Steps:
#start writing the function to allow the AI opponents to make their bets (including parameters on what they're able to bet on based on the rules of Liar's Dice)
#substep: apply the counting function to all opponents and then go back and add weighted probabilities to each to allow them to make their own bets

#if they call the previous person a liar, write the code to make the person who's wrong lose a die and the overall pot lose a die
#then, make sure that if the opponent bets, the x_responses update based on what the previous person bet on



from random import randint
import random
from numpy.random import choice

pot_of_dice = []

def generate_dice(pot_of_dice):
  for die in range(20):
    die = randint(1, 6)
    pot_of_dice.append(die)

generate_dice(pot_of_dice)

print (pot_of_dice)


dice_per_player = {"me": 5, "opp_1": 5, "opp_2": 5, "opp_3": 5}


index = 0
die_number = dice_per_player["me"]
def assign_my_hand(i):
  i = index
  while i < die_number:
    my_hand.append(pot_of_dice[i])
    i += 1

my_hand = []

assign_my_hand(my_hand)

my_hand.sort()
print (my_hand)

#my turn:
bet_number = int(input("What number would you like to bet on? "))

one_response = len(pot_of_dice)
two_response = len(pot_of_dice)
three_response = len(pot_of_dice)
four_response = len(pot_of_dice)
five_response = len(pot_of_dice)
six_response = len(pot_of_dice)


if bet_number == 1:
  one_response = input("How many %d's do you think there are? " % (bet_number))
elif bet_number == 2:
  two_response = input("How many %d's do you think there are? " % (bet_number))
elif bet_number == 3:
  three_response = input("How many %d's do you think there are? " % (bet_number))
elif bet_number == 4:
  four_response = input("How many %d's do you think there are? " % (bet_number))
elif bet_number == 5:
  five_response = input("How many %d's do you think there are? " % (bet_number))
elif bet_number == 6:
  six_response = input("How many %d's do you think there are? " % (bet_number))
else:
  print ("That's not a number on a die! Try again...")
  input("What number would you like to bet on? ")


liar_or_bet = ": will you call them a liar, or bet?"


opp_1_hand = []

index = dice_per_player["me"]
die_number = die_number + dice_per_player["opp_1"]
def assign_opp_1_hand(i):
  i = index
  while i < die_number:
    opp_1_hand.append(pot_of_dice[i])
    i += 1

assign_opp_1_hand(opp_1_hand)

print (opp_1_hand)

#this function counts how many of a given value appear in a list and then add those counts to the nums dictionary:
def count_num_1(hand):
  i = 1
  while i < 7:
    nums_1[i].append(opp_1_hand.count(i))
    i += 1

hand = opp_1_hand
nums_1 = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

count_num_1(nums_1)
print (nums_1)

#simpler but bulkier way to count and has nowhere to store the counted values:
#print (opp_1_hand.count(1))
#print (opp_1_hand.count(2))
#print (opp_1_hand.count(3))
#print (opp_1_hand.count(4))
#print (opp_1_hand.count(5))
#print (opp_1_hand.count(6))


print ("Opponent 1" + liar_or_bet)

always_bet = 0.3333
sometimes_bet = 0.45
sometimes_liar = 0.6

#Works alongside my attempt to write this more efficiently:
#responses = [int(one_response), int(two_response), int(three_response), int(four_response), int(five_response), int(six_response)]

#this is the long way around. This super long if-then statement will print the correct response based on the values bet from the human player and what percentage of the total dice that bet represents
if always_bet > int(one_response) / len(pot_of_dice) or always_bet > int(two_response) / len(pot_of_dice) or always_bet > int(three_response) / len(pot_of_dice) or always_bet > int(four_response) / len(pot_of_dice) or always_bet > int(five_response) / len(pot_of_dice) or always_bet > int(six_response) / len(pot_of_dice):
  print ("I will bet.")
elif always_bet < int(one_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(two_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(three_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(four_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(five_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(six_response) / len(pot_of_dice) < sometimes_bet:
  print ("I might bet.")
elif sometimes_bet < int(one_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(two_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(three_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(four_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(five_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(six_response) / len(pot_of_dice) < sometimes_liar:
  print ("I might call you a liar.")
else:
  print ("I will most certainly call you a liar.")


weights = [4/12, 3/12, 2/12, 2/12, 1/24, 1/24]

first = max(nums_1, key=nums_1.get)
nums_1.pop(first)
second = max(nums_1, key=nums_1.get)
nums_1.pop(second)
third = max(nums_1, key=nums_1.get)
nums_1.pop(third)
fourth = max(nums_1, key=nums_1.get)
nums_1.pop(fourth)
fifth = max(nums_1, key=nums_1.get)
nums_1.pop(fifth)
sixth = max(nums_1, key=nums_1.get)
nums_1.pop(sixth)

opp_1_dice_sorted = [first, second, third, fourth, fifth, sixth]

#this is the key right here to making this all work. This one simple line of code determines which die the AI opponent will bet on when they bet
print(choice(opp_1_dice_sorted, p=weights))

weighted_dice = {first: weights[0], second: weights[1], third: weights[2], fourth: weights[3], fifth: weights[4], sixth: weights[5]}

#i = 0
#while i < 6:
  #weighted_num = opp_1_dice_sorted[i] * weights[i]
  #weighted_dice[i + 1].append(weighted_num)
  #i += 1

print(weighted_dice)


opp_2_hand = []

index = index + dice_per_player["opp_1"]
die_number = die_number + dice_per_player["opp_2"]
def assign_opp_2_hand(i):
  i = index
  while i < die_number:
    opp_2_hand.append(pot_of_dice[i])
    i += 1

assign_opp_2_hand(opp_2_hand)

print (opp_2_hand)


def count_num_2(hand):
  i = 1
  while i < 7:
    nums_2[i].append(opp_2_hand.count(i))
    i += 1

hand = opp_2_hand
nums_2 = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

count_num_2(nums_2)
print (nums_2)


print ("Opponent 2" + liar_or_bet)


#need to fix this so I can use a loop but only print for the correct "x_response" rather than printing for all 6. It also isn't printing based off the correct values right now
#Update: I'd like to find a more efficient way to write this, but this for loop isn't working like I wanted it to

#for response in responses:
  #if always_bet > (response / len(pot_of_dice)):
    #print ("I will bet.")
  #elif always_bet < (response / len(pot_of_dice)) < sometimes_bet:
    #print ("I might bet.")
  #elif sometimes_bet < (response / len(pot_of_dice)) < sometimes_liar:
    #print ("I might call you a liar.")
  #else:
    #print ("I will most certainly call you a liar.")


if always_bet > int(one_response) / len(pot_of_dice) or always_bet > int(two_response) / len(pot_of_dice) or always_bet > int(three_response) / len(pot_of_dice) or always_bet > int(four_response) / len(pot_of_dice) or always_bet > int(five_response) / len(pot_of_dice) or always_bet > int(six_response) / len(pot_of_dice):
  print ("I will bet.")
elif always_bet < int(one_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(two_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(three_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(four_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(five_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(six_response) / len(pot_of_dice) < sometimes_bet:
  print ("I might bet.")
elif sometimes_bet < int(one_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(two_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(three_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(four_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(five_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(six_response) / len(pot_of_dice) < sometimes_liar:
  print ("I might call you a liar.")
else:
  print ("I will most certainly call you a liar.")


opp_3_hand = []

index = index + dice_per_player["opp_2"]
die_number = die_number + dice_per_player["opp_3"]
def assign_opp_3_hand(i):
  i = index
  while i < die_number:
    opp_3_hand.append(pot_of_dice[i])
    i+=1
  
assign_opp_3_hand(opp_3_hand)

print (opp_3_hand)


def count_num_3(hand):
  i = 1
  while i < 7:
    nums_3[i].append(opp_3_hand.count(i))
    i += 1

hand = opp_3_hand
nums_3 = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

count_num_3(nums_3)
print (nums_3)


print ("Opponent 3" + liar_or_bet)


if always_bet > int(one_response) / len(pot_of_dice) or always_bet > int(two_response) / len(pot_of_dice) or always_bet > int(three_response) / len(pot_of_dice) or always_bet > int(four_response) / len(pot_of_dice) or always_bet > int(five_response) / len(pot_of_dice) or always_bet > int(six_response) / len(pot_of_dice):
  print ("I will bet.")
elif always_bet < int(one_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(two_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(three_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(four_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(five_response) / len(pot_of_dice) < sometimes_bet or always_bet < int(six_response) / len(pot_of_dice) < sometimes_bet:
  print ("I might bet.")
elif sometimes_bet < int(one_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(two_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(three_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(four_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(five_response) / len(pot_of_dice) < sometimes_liar or sometimes_bet < int(six_response) / len(pot_of_dice) < sometimes_liar:
  print ("I might call you a liar.")
else:
  print ("I will most certainly call you a liar.")


#print (opp_3_hand.count(1))










