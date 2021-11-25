# Japanese test - Dessert, Cube, Ladder, Horse, Flowers, Storm

## Description

This application is is a personality test deriving from japanese culture, and this [link](https://steemit.com/psychology/@breezin/cube-test-japenese-personality-test) provides all relevant information about how this game works. It can also help users to notice how do they see themselves and sparkle some imagination.

## User Stories 

* I want the User to understand and navigate easy through the test
* I want the User to be able to start/restart/quit the app and get information about the game 
* I want the User to be able to write the description of objects
* I want User to have the responses displayed
* I want User to be notified when the characters that he inputs are not supported with an apropriate message
* I want the User to be notified of empty input and given another chance to put information
* I want to possibly use one of Python libraries to create a visual appearance of the results

## Site Owner Goals

* To entertain users by inspiring them to know themselves better
* To offer user a display of answers to the questions
* To be able to guide users and collect their answers, name
* To be able to display a personality test in a fun way to users

## Instructions

This is a personality test, inspired by Japanese culture, where you gain insight of what your perspective is like.
- Welcome and name to start
The welcome page is presenting the test, without too many details, asking for the name. It is part of the mystery, so curiosity is sparkled. After user enters the name, users are greeted back and encouraged to be creative and take time to describe objects. As the name contains a word 'test', I wanted to assure the users mentioning all answers are right, so they feel free to describe in greater details.
- Choosing a to start, b to read about, and q to quit
If chosen to quit, users exit the app with appropriate 'Goodbye' message,
if chosen to see about, users can read a bit more about the details of this Japanese Cube test and then asked to try the test or not, and if not, the user exits with apropriate message displayed. If chosen to try it, user starts with first object, cube.
- Describing the objects
There are 5 different objects, starting from cube, to be describedby the user, than to horse, to the flowers and lastly, the thunderstorm. Users are asked to describe in details what do they imagine,and what kind of setting they imagine, also the relation between objects if there is any.
- After answering and describing every object, user is offered reading about the interpretation of every object and what could it mean for the user, or if not wanting to read this moment, choose n to exit or start the test over.


## Flowchart

![](static/readme-images/cube-flowchart.png)

## Features

### Welcome Page

![](static/readme-images/welcome.png)

### About

![](static/readme-images/about_test.png)

Entered test - First object - cube

![](static/readme-images/started.png)

Second object - Ladder

![](static/readme-images/ladder.png)

Third object - Horse

![](static/readme-images/horse.png)

Fourth object - Flowers

![](static/readme-images/flowers.png)

Fifth object - Thunderstorm

![](static/readme-images/thunder.png)


### Future features

I would like this app to be able to generate the whole document with answers and interpretations for users so they could print and keep a hard copy if they like

## Technologies 
links and explain

* Git
* GitHub -  used for version control
* Gitpod - Cloud-based IDE and the steps for deployment
* Python

### Python Packages 

* Prompt-toolkit if used explain every and links connect
* Tabulate


## Deployment

### GitHub

- In the [GitHub repository](https://github.com/totalnoMartina/cube-discovery),navigate to the Settings tab.
- From the Source section drop-down menu, select the `Main` Branch (alt: `Master`).
- Once the `Main` branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

### Local Deployment

In order to make a local copy of this project, you can clone it using the following command in your IDE terminal of your choice:

- `git clone https://github.com/totalnoMartina/cube-discovery.git`
from slack add here

### Heroku

Explain step by step, creating a heroku account, create an new app, select region, go to 'deploy' tab, sleect github as deployment method, locate your repository on Github, select 'connect reposit' , enable automatic deployments, thwn go settings tab, and packages here below:
When deploying on Heroku, two buildpacks are installed from the _Settings_ tab.

1. `heroku/python`
2. `heroku/nodejs`

A _Config Var_ was added and named `PORT`, and set to `8000` before clicking deploy branch.
go back to deploy tab, click deploy branch, it will take coulpe minutes to install requirements, once it is finished, you can view live deployed site and list the link to your site. screenshots of the steps maybe - optional


## Credits 

The italics code were found in [this link](https://stackoverflow.com/questions/13559276/can-i-write-italics-to-the-python-shell)

The code for prompt asking user for a name is found [here](https://python-prompt-toolkit.readthedocs.io/en/stable/pages/asking_for_input.html)

The code for clearing the screen before moving on to next object is [here]( https://www.geeksforgeeks.org/clear-screen-python/)

The help to find a list of functions is found on this [link](https://www.quora.com/How-can-you-make-a-list-of-functions-in-Python)

# Acknowledgements

Code Institute mentor, Tim Nelson is huge help and guidance, helping me and directing my ideas toward real goal to be accomplished through creating this app. I was unsure on how to start and I had perfect guidance.
My close friends who tested the app a few times, shared insights and concerns that help me make this better for the UX.
