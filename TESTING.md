
# Testing

Testing user input for many different characters or empty space
![](documentation/readme-images/welcome-validation-test.png)

Testing entering empty space when starting with the first object
![](documentation/readme-images/cube-empty-input-test.png)

Testing second object for empty input by user
![](documentation/readme-images/ladder-empty-test.png)

Testing third object for empty space input by user
![](documentation/readme-images/horse-empty-test.png)

Testing fourth object for empty space input by user
![](documentation/readme-images/flowers-empty-test.png)

Testing user for the input on choosing to see interpretation
![](documentation/readme-images/interpretation-validation-test.png)

Empty input validation tested while starting the test
![](documentation/readme-images/empty-input-starting-test.png)

Start test, choose quit if user changed mind and get apropriate message
![](documentation/readme-images/quitting-starting-valid-test.png)

Validating input for characters not accepted and present apropriate message
![](documentation/readme-images/about-symbols-test.png)

Testing at the object thunderstorm for empty space, user gets apropriate message
![](documentation/readme-images/empty-input-thunderstorm-test.png)





User is able to start again at the end of this test
![](documentation/readme-images/end-trying-again-test.png)

## Bugs

### Validation testing Notes

Please Note!
During testing the function cube() for validation of the user input being symbols/characters as '#;08=-' or space character, a method .isalpha() was tested, which is also spacebar-sensitive, and will not take user input if entered space in between. The method is taken out of the function for the reason of user possibly wanting to describe in long sentences with a comma or space and possibly exclamation marks or similar. Therefore, the function prints out exact input of user with the symbols included, if any. 
By putting this method I might have had limited user to describe everything in one go and made it more complicated. So this was my reason to not use validation for isalpha() and accept symbols as user input.
Another option considered was using creating a list from user input, adding inputs into a list, separating by a comma or space (again, something that complicates function further), and then later using for loop to place them back as user wrote them or a common method in Python called tostring(). In my perspective, this validation is only relevant if user slips a finger without writing anything in, so we bring user back to the beginning to write description again, with apropriate prompt. And if user wants to put commas, I wanted that to be allowed.

For user to input the name, I tried using Python [prompt_toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/) and heroku did not seem to recognize, so I removed that.
Some infinite loops are caused and that was handled with exiting function.

For iterating from one object to another, I had an idea to use separate function called next_or_restart() which was used before the functions were ready to connect to each other. As the app evolved, the function is no longer needed and therefore, deleted.

Original validation was discovered through these bugs.

## Test User Stories

* I want the User to understand and navigate easy through the test
* I want the User to be able to start/restart/quit the app and get information about the game 
* I want the User to be able to write the description of objects
* I want User to have the responses displayed
* I want User to be notified when the characters that he inputs are not supported with an apropriate message
* I want the User to be notified of empty input and given another chance to put information
* I want to possibly use one of Python libraries to create a visual appearance of the results

## Features
### Welcome Page

![](documentation/readme-images/welcome.png)

### About

![](documentation/readme-images/about_test.png)

Entered test - First object - Cube

![](documentation/readme-images/cube-start.png)

Second object - Ladder

![](documentation/readme-images/ladder.png)

Third object - Horse

![](documentation/readme-images/horse.png)

Fourth object - Flowers

![](documentation/readme-images/flowers.png)

Fifth object - Thunderstorm

![](documentation/readme-images/thunder.png)

Interpretation - Cube
![](documentation/readme-images/cube-interpret.png)

Interpretation - Horse
![](documentation/readme-images/horse-interpret.png)

Interpretation - Ladder
![](documentation/readme-images/ladder-interpret.png)

Interpretation - Flowers
![](documentation/readme-images/flowers-interpret.png)

Interpretation - Thunderstorm
![](documentation/readme-images/thunder-interpret.png)


## Further Testing

### Browser Compatibility maybe eleave it
