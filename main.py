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