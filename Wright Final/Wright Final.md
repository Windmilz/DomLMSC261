# what you did
I attempted to create a text based RPG
## how you did it
I retrieved a framework for me to code off of and created a small story that I thought was pretty basic but also a little interesting, it has a nice twist at the end. Then had to have an html file load the game (which was coded in Java script) and load both of those things onto a website.
###    the problems you faced & how you overcame them
So the first problem was the big problem. Originally I had planned to use this repository: https://www.npmjs.com/package/text-rpg-engine/v/1.0.5 for my engine. It seemed simple enough to use and create the json file. Of course it didnt dawn on me that I was using a json file until it was time to export this to html and actually put on the web. Which was a problem in itself. The process made no sense to me so I deliberated with my brother over this, to which he said it would make more sense if I just used another engine that was simplified. Then he went silent for about 2 hours and then sent me back a custom RPG engine that already had a basic html and css file attached to it (although the css file doesn't exist anymore, rest in peace).

if anyone wants to check out the repository I have it right here

https://github.com/captainsalt/rpg-framework

Huge thank you to my brother for giving me a better engine so I could actually complete this assignment.

There was one really weird issue with the way he coded it. because the class arguments (which is how he contained all the information) the boolean that allows the program to find out wether or not the progress in the story doesn't check for the right answers. It checks for the wrong answer. So a couple of times I found myself passing through the wrong boolean because i didn't understand that until testing my game.

#### what code you used from others/elsewhere where to find that code
Aside from the framework repository listed above, I also imported a css file from mini css : <link rel="stylesheet" href="https://cdn.rawgit.com/Chalarangelo/mini.css/v3.0.1/dist/mini-default.min.css">
 which you can find on https://minicss.org/docs
