print("learning python again")

num_of_apples = 10
print(num_of_apples)

num_of_apples = 8
print(num_of_apples)

print(type(num_of_apples))



# passing in variables (reminds me of props)
fav_numbers = 27
name_and_fav_numbers = "Rach: {}".format(fav_numbers)
print(name_and_fav_numbers)

# add strings
first_name = "john "
last_name = "doe"
print(first_name + last_name)

# ==
play_position = 1
end_position = 10

is_at_end = play_position ==end_position
print(is_at_end)

# not
not_is_at_end = not is_at_end
print(not_is_at_end)

# and. has to be true on both sides of &&
score = 10
is_game_over = score >= 10 and is_at_end
print(is_game_over)

# ===================
# COLLECTIONS - ways to store multiple values in one variable. lists, tuples,dictionaries
# ===================

# ===================
# LISTS []- can put any type of data in here
# ===================


list = [5, True, "apple"]
enemy_positions = [5, 10, 15]
enemy_positions = [5, 10, 15, 20]
print(enemy_positions[3])

# len checks the length of a list
print(len(enemy_positions))

# change value of list item
enemy_positions[0] = 6

#range
print(enemy_positions[0:2]) 

# append function - adds onto the end
# list_name.append(25)
#there is also .insert and .remove

# ===================
# TUPLES () - cannot change
# ===================
high_score = ("jan", 130)
print(high_score)

# in operator (is used to determine if an element on the left is inside of a collection on the right. is a boolean statement)
print("jan" in high_score)

# ===================
# DICTIONARIES dictionary = {key: value}
# ===================

actions = {"move_right":1, "move_left":-1}
print(actions["move_right"])

# none key/value
print(actions.get("g"))

# update a value
actions["move_right"] = 2

# add a new key value pair
actions["u"] = 1

# fetch solely keys or values
print(actions.keys())
print(actions.values())
print(actions.items())

# delete item at a specific key
del(actions["u"])

# in operatpr, does a key exist inside of this dictionary
print("l" in actions)

# ===================
# CONTROL FLOW - checking if a condition is true, and executing code if it is.if, while, for in loops
# ===================

# ===================
# IF STATEMENTS - 
# ===================
 
key = "r"

if key =="r":
  print("move right")
elif key =="l":
  print("move left")
else:
  print("invalid movement")


