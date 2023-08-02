user_input = input("Enter a number to nest: ")      # Accept user input first
nested = []         # Create an empty list to store the output

i = len(user_input)-1       # Set the index to the last character of the user input so that we can start looping from the end

while i >= 0:       # Loop through the user input (used a while loop because a for loop would have looked more complicated)
    if i == len(user_input)-1:      # If the index is the last character of the user input, then we can just add it to the list  (no need to nest) 
        nested = list(user_input[i]) # Convert the character to a list and store it in the nested variable
    else:       # If the index is not the last character of the user input, then we need to nest it
        nested = [list(user_input[i]), nested]         # This is the main part of the code. We are nesting the previous list inside the current list [] accepts two arguments and stores them in a list similar to using list.append(list())
    i -= 1

print(nested)

# OR YOU CAN TRY WITH A FOR LOOP

for i in range(len(user_input)-1,-1,-1):
    if i == len(user_input)-1:
        nested = list(user_input[i])
    else:
        nested = [list(user_input[i]), nested]

print(nested)