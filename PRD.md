# The project requirements:

## Technical:
You need to use streamlit library to build the UI. Use children friendly font and UI design.  you can reference to PBR Wow in the world theme
You can use aws strands agent to develope agents https://strandsagents.com/latest/.  https://github.com/strands-agents/samples/tree/main/02-samples/09-finance-assistant-swarm-agent
You use anthropic model , haiku 4.5
You can use flask , gunicorn to run the server
You can use python only
API keys for anthropic model is accessible from environment variable. [AKEY]

## development environment
* you use uv
* you need to use aws strands api to build agent
* you use python

## User stories
You are playing with children in grade 5-6.  
You play a game called twenty questions games.  This game is different to the classic twenty question games.

You must play the game in this rule:
1. ask player to have an object in mind.  don't share with any one. 
2. you need to try to guess the item. 
3. the player can only response 'yes' or 'no'. 
4. your max attempts are 20.  


## Operation
* this project needs to be hosted on render.com
* source code must be stored in github


## user experience
### when launch the webpage 
* you will ask for player to input the name. 
* you show a note on the screen:  we are going to play a guessing game.  ask the player to think about one thing and keep that in mind. I will guess it out.  when you are ready click 'start'.
* then prompt a 'start' button to show they are ready to start 

### after click 'start' button
* you make a guess, and print it on the screen in a cute font.
* you ask the player if they are correct. 
* player can click  "yes" or "no" button
* then you follow the clue and start guess. 
* You repeat to ask question above until you guess out the item. util 20 qquestions. 
* you ask question with previous answer as context.

for example: 
is it something you can see?  yes
is it something on the earth?  no
is it something far away ? yes
is it the moon? no
is it the Naptune? yes. <at ths point you win the games>

### when you win the game
* You create a summary and give positive feedback. if you could give a short story or history about the item . e.g. if the player item is a cryaon.  did you know that crayon was invented by ...
You need to restart the question counter and start asking question again. 

### When you lose the game
* you ask what the item is.  
* you act surprised and you will give a short story about the item. 



[How to use dependcies]
strandsagent library.  sample script: https://github.com/strands-agents/samples/blob/main/01-tutorials/01-fundamentals/01-first-agent/01-first-agent.ipynb
anthorpic model : https://strandsagents.com/0.1.x/documentation/docs/user-guide/concepts/model-providers/anthropic/ 



