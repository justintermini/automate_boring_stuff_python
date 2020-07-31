# Write a function that takes a list value as an argument and returns a string
# with all the items separated by a comma and a space, with and inserted before
# the last item. For example, passing the previous spam list to the function
# would return 'apples, bananas, tofu, and cats'. But your function should be
# able to work with any list value passed to it. Be sure to test the case
# where an empty list [] is passed to your function.

def comma(list):
    y = len(list)
    if y == 1:
        print(str(list[0]))
    elif y == 2:
        print(str(list[0]) + ' and ' + str(list[1]))
    elif y > 2:
        for x in range(y-1):
            print((str(list[x]) + ', '), end='')
        print(('and ' + str(list[-1])))
    
        
    
        



spam = ['cats', 'dogs', 'eggs']
comma(spam)


# Need to add code for error checking
          
