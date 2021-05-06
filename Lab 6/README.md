# m[Q](https://en.wikipedia.org/wiki/QAnon)tt[Anon](https://en.wikipedia.org/wiki/QAnon): Where We Go One, We Go All

## Prep

1. Pull the new changes
2. Install [MQTT Explorer](http://mqtt-explorer.com/)
3. Readings 
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Introduction

The point of this lab is to introduce you to distributed interaction. We've included a some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects. However we want to emphasize the grading will focus on your ability to develop interesting uses for messaging across distributed devices. 

## MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of Internet of Things (IoT) devices. 

### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`
* **Client** - A device that subscribes or publishes information on the network
* **Topic** - The location data gets published to. These are hierarchical with subtopics. If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. Subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on that topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe
* **Publish** - This is a way of sending messages to a topic. You can publish to topics you don't subscribe to. Just remember on our broker you are limited to subtopics of `IDD`

Setting up a broker isn't much work but for the purposes of this class you should all use the broker we've set up for you. 

### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.



![input settings](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/mqtt_explorer.png?raw=true)



Once connected you should be able to see all the messaged on the IDD topic. From the interface you can send and plot messages as well.



## Send and Receive 

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python.  Lets spend a few minutes running these and seeing how messages are transferred and show up. 

**Running Examples**

* Install the packages from `requirements.txt`, ideally in a python environment. We've been using the circuitpython environment we setup earlier this semester. To install them do `pip install -r requirements.txt`
* to run `sender.py` type `python sender.py` and fill in a topic name, then start sending messages. You should see them on MQTT Explorer
* to run `reader.py` type `python reader.py` and you should see any messages being published to `IDD/` subtopics.

## Streaming a Sensor

We've included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%204) that streams sensor inputs over MQTT. Feel free to poke around with it!

## The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB we too can find unity in our heart, minds and souls. With the help of machines can  overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [Pi Display](https://www.adafruit.com/product/4393).

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="300">

You are almost there!

The second step to achieving our great enlightenment is to run `python color.py`

You will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one. 

I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also I have't load tested it so things might just immediately break when every pushes the button at once.

You may ask "but what if I missed class?"

Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can got to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs.

Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 



## Make it your own

Find at least one class (more are okay) partner, and design a distributed application together. 

**1. Explain your design** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.

![Labyrinth maze puzzle](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%206/adsf.png)

Inspired by wooden labyrinth puzzle games where a single player has to tilt the board to maneuver a marble around a maze, we decided to make a co-op version of the game. With two players, each player would be responsible for one axis of tilt (either x or y), requiring both to work together to complete the challenge given to them.

**2. Diagram the architecture of the system.** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

![Architecture Diagram](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%206/Diagram.png)

The two players each use their own raspberry pi connected accelerometer, with the objective of rotating the virtual board and getting the magenta ball into the grey hole - after which the hole randomly generates in another location and the game is reset. By default, player 1 is responsible for the X-axis rotation of the labyrinth board while player 2 is responsible for the Y-axis. The corresponding accelerometer values are sent over MQTT under a specific topic (`IDD/juicey/labyrinth/`) before a UI program - run separately on a third machine - parses the X, Y values over MQTT and displays the resulting ball location and labyrinth board. This setup requires both players to see the screen at the same time, but it could be extended as a communication game by allowing only a third person to see the screen and relay information about the ball's location and state of the game to the other two players. Two scripts were written - one for the raspberry pi controllers `game-controller.py`, and one for the game interface `game-ui.py` (run on the computer) written using the pygame library.

**3. Build a working prototype of the system.** Do think about the user interface: if someone encountered these bananas, would they know how to interact with them? Should they know what to expect?

[Prototype Test MP4 file](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%206/test.mov)
([Google Drive link](https://drive.google.com/file/d/1FgrFotuAti5W3BIbbT7XcCAbAIDY43n_/view?usp=sharing))

The first test of the prototype was done with a single player controlling both the X and Y rotational axes for the labyrinth over MQTT. With minimal delay from communicating over MQTT, the experience was quite flawless and moving the accelerometer would almost instantaneously affect the ball's position. The user interface was done quite simply by having the user input the number of players they had (1 or 2 players). If there were two players, the controller script with continue by asking which player would be player 1 and which would be player 2. Problems could easily arise if both players played as the same player (there are no checks to see which 'role' is currently taken; perhaps this could be solved by having another sub-topic containting the leftover roles allowed. The controls with the accelerometer easily mapped to the labyrinth and ball movement, making this interaction much more intuitive and natural. Perhaps this interaction could be enhanced much further with a cardbaord prototype or some rigging to simulate an actual labyrinth maze puzzle.

**4. Document the working prototype in use.** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

[Prototype Test MP4 file](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%206/IDD%206.mp4)
([Google Drive link](https://drive.google.com/file/d/1w_kHtzh66yJB0itf2lIojsVnqoip2H_-/view?usp=sharing))

In this demo, **player 1** was the video feed on top (responsible for the ball's up-down motion) while **player 2** was the video feed on the bottom (responsible for the ball's left-right motion). Upon closer inspection, it can be seen that player 2's accelerometer was oriented sideways, resulting in him moving the sensor forward-backwards instead of the expected side-to-side motion. There was surprisingly not much latency and the whole experience was pretty fun, especially after we were able to coordinate ourselves after a few attempts.

**5. BONUS (Wendy didn't approve this so you should probably ignore it)** get the whole class to run your code and make your distributed system BIGGER.
