# Bluesoxx Halloween Game


import time        # module we can use to make game pause

###########
# DISPLAY #
###########
#
# This is a function we can use to write messages to the screen, for the player to see.
# We could just use print() and sleep() all over our code, but this way is less
# repetitive in terms of typing, and if we want to change the way the game talks then
# this way we can do it all in one place.
#
# I can just call this function with a string, like: display("Hello"), and in this case
# the game will write "Hello" to the screen and then pause for two seconds before
# continuing.  The pause is for 2 seconds becaus eof the part of the function definition
# that says, 'pause=2'.  But if I choose to use the function in an different way, by
# supplying both a string and an integer, the game will pause for a different amount of
# time.  Like, writing display("Hello", 5") will make the game print "Hello" to the screen
# and then pause for a very dramatic five seconds.  This kind of setup is called "default
# arguments"; 2 is the default value for the variable 'pause'.
#
# You should alter this function to change the way the game talks!  For instance, maybe,
# even though it is Halloween the game does not have to say everything is spooky.  Or,
# use google to figure out how to use the pyttsx library, and make the game say everything
# out loud.  (For pyttsx you will have to install the package in PyCharm under the "project
# interpreter menu" and in the code you will import the package at the top and then set up
# an engine.  Might sound harder than it really is!  Here is an example of how to use the
# (but the installation is different from in PyCharm):
# https://pythonprogramminglanguage.com/text-to-speech/
#
def display(msg, pause=2):
    msg = msg + "  Spooky!"
    print(msg)
    time.sleep(pause)


#######
# ASK #
#######
#
# Similarly to the display() function above, we use this function instead of writing
# raw_input() and upper() all over our code.  We provide a question that we want the
# user to ask, and then record the answer.  To make it easier to check their answer,
# we convert it to all upper case, so that it won't matter if they type, for instance,
# "yes" or "Yes" or "YES" or even "YEs"--we can just convert all of these to upper
# and check whether the result is "YES".
#
# Above, the display() function doesn't return anything, it just writes something to
# the screen and then quits.  But here, our function returns the player's response.
# So, in our main program we want to make sure to store the result of calling this
# function in a variable.
def ask(question):
    print(question)
    response = raw_input()
    response = response.upper()
    return response

###################
# THE GAME ITSELF #
###################
#
# Now we use the helper functions ask() and display(), which we defined above, to create
# a game.  The game uses if-statements to determine what will happen to the player based
# on the responses they give to the ask() questions.


# Greet the player and introduce the scenario.
name = ask("What is your name?")
display("Welcome to the game, " + name + ".")
display("You are at home late at night shopping for shoes on the internet.  You have one thousand dollars.")
display("On Site 1 you find shoes that won't be delivered for months, from a company that has never made shoes before.")
display("These shoes cost one thousand dollars.", 5)
display("On Site 2 you find shoes that are available immediately, from an established company, costing forty dollars.")

# Ask whether the player wants to buy from the first site and respond appropriately.
response = ask("Do you want to buy a pair of shoes from the first site?")
if (response == "YES" or response == "Y"):
    display("A dragon appears and proclaims you a visionary.")
elif (response == "NO" or response == "N"):
    display("You go on to live the rest of your life, which turns out comfortable, but incomplete.")
else:
    display("Sorry, your response was unintelligible.")

# Ask whether the player wants to buy from the second site and respond appropriately.
response = ask("Do you want to buy 25 pairs of shoes from the second site?")
if (response == "YES" or response == "Y"):
    display(name + ": really?  What are you going to do with 25 pairs of shoes?")
elif (response == "NO" or response == "N"):
    display("A skeleton appears and whispers that " + name + " is sensible and boring.")
else:
    display("Sorry, your response was unintelligible.")

# End the game.
print("The game is over.")
