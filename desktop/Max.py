#determines the largest number among the four inputs of the user.

prompts = ["first", "second", "third", "fourth",]
numbers = [float(input("Enter " + prompt + " number: ")) for prompt in prompts]
print("The largerst number is", max(numbers))


# create a list called prompts that contains a part of the string that will serve as the custom message in the input query. This also where the for loop inside the comprehension loops through.
# use a comprehension to create a list that will store the numbers from the user input.
# Since the comprehension uses the function 'input' to obtain the user input, it needs to be typecasted to float, as the return value of input is a string.
# use max function to determine the element with the highest value and print the return value

