
# Testing

screenshot of testing inputs, valid and invalid

## Bugs

For user to input the name, I tried using Python [prompt_toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/) and heroku did not seem to recognize, so I removed that.
Some infinite loops are caused and that was handled with exiting function.

Original validation was discovered through these bugs.

While trying to store input from user in a string value, or space separated values, I am trying method isspace() whic so far does not show use in every consistent case. Found a bug and resolved, turned out the order of functions was not checking so the validations kept failing and looping like abstract values are in input. Finally, solution is that condition with most requirements should be placed first.

## Test User Stories
 copy from readme

 add screenshots from feature section

## Further Testing

### Browser Compatibility maybe eleave it
