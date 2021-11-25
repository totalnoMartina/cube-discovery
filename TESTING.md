
# Testing

screenshot of testing inputs, valid and invalid

## Bugs

### Validation testing Notes

Please Note!
During testing the function cube() for validation of the user input being symbols/characters as '#;08=-' or space character, I tried with a method .isalpha() which is also spacebar-sensitive, and will not take user input if entered space in between. The method is taken out of the function for the reason of user possibly wanting to describe in long sentence with a comma or space and posibly exclamation marks or similar. Therefore, the function prints out exact input of user with the symbols included, if any. 
By putting this method I might have had limited user to describe everything in one go and made it more complicated. So this was my reason to not use validation for isalpha() and accept symbols as user input.
Another option considered was using creating a list from user input, adding inputs into a list, separating by a comma or space (again, something that complicates function further), and then later using for loop to place them back as user wrote them or a common method in Python called tostring(). In my perspective, this validation is only relevant if user slips a finger without writing anything in, so we bring user back to the beginning to write description again, with apropriate prompt. And if user wants to put commas, I wanted that to be allowed.

For user to input the name, I tried using Python [prompt_toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/) and heroku did not seem to recognize, so I removed that.
Some infinite loops are caused and that was handled with exiting function.

For iterating from one object to another, I had an idea to use separate function called next_or_restart() which was used before the functions were ready to connect to each other. As the app evolved, the function is no longer needed and therefore, deleted.

Original validation was discovered through these bugs.


## Test User Stories
 copy from readme

 add screenshots from feature section

## Further Testing

### Browser Compatibility maybe eleave it
