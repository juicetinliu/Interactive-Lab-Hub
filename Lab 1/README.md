

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.



For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. _Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

1. Set up [your Github "Lab Hub" repository](../../../) by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Spring/readings/Submitting%20Labs.md).
2. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how](https://guides.github.com/features/mastering-markdown/) to post links to your submissions on your readme.md so we can find them easily.

### For lab, you will need:

1. Paper
1. Markers/ Pen
1. Smart Phone--Main required feature is that the phone needs to have a browser and display a webpage.
1. Computer--we will use your computer to host a webpage which also features controls
1. Found objects and materials--you’ll have to costume your phone so that it looks like some other device. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case. Be creative!
1. Scissors

### Deliverables for this lab are: 
1. Storyboard
1. Sketches/photos of costumed device
1. Any reflections you have on the process.
1. Video sketch of the prototyped interaction.
1. Submit these in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.


## Overview
For this assignment, you are going to 

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 
**Describe your setting, players, activity and goals here.**

- _Setting:_ At a school.

- _Players:_ Students and the device.

- _Activity:_ Students walk in to the classroom through the doorway, and the device acknolwedges their arrival to 'greet' them with colored lights depending on their lateness (Green - early, Red - late).

- _Goals:_ Students going into class will see the lights and reflect on their decision to walk into class late; there would also be a student identification system (with rfid ID cards) as part of this device to feed into an automatic roll call each morning.

**Include a picture of your storyboard here**

![Storyboard](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/Screenshot%202021-02-10%20at%2011.24.48.png)

**Summarize feedback you got here.**

- "If a student knows he/she is late, does he/she need a light to show that he/she is late?"

- "Not so useful now ..(with COVID around)"

- "Might be quite useful for students with tight schedules"

## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

**Are there things that seemed better on paper than acted out?**

- It would be more clear to viewers to have some sort of interaction with the device (Eg. a card scan/temperature check) to signal an event instead of an automatic system with the student just walking through.

**Are there new ideas that occur to you or your collaborators that come up from the acting?**

- The light could be used as a signal in more ways, for example if they shouldn't enter a room because of their high temperature (with the current COVID climate) or if they aren't enrolled in the class (since their RFID ID cards can be cross-checked with the current class roster).

## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

If you run into technical issues with this tool, you can also use a light switch, dimmer, etc. that you can can manually or remotely control.

**Give us feedback on Tinkerbelle.**

- There are connection issues with mobile (not sure what is causing the errors but rerunning the tinker.py script sometimes fixes it).

- Buttons don't fade on mobile when selecting the `Tinkerbelle` button.

- It's a pretty cool tool!

## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

**Include your first attempts at recording the set-up video here.**

[Setup MP4 file](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/Part%20D_1.mp4)
([Google Drive link](https://drive.google.com/file/d/1ZnzopLStq40G4d4xzSdy7EsOKAimWLuZ/view?usp=sharing))

Now, change the goal within the same setting, and update the interaction with the paper prototype. 

**Show the follow-up work here.**

[Follow-up MP4 file](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/Part%20D_2.mp4)
([Google Drive link](https://drive.google.com/file/d/1_y7k5J_EecfELjZqMp8iJ5wFbhV46E_i/view?usp=sharing))

## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

**Include sketches of what your device might look like here.**

![Sketch](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/Part%20E.png)

**What concerns or opportunitities are influencing the way you've designed the device to look?**

The device has to be large enough for people to notice it and see it afar, but fit the style of a rectangular door. The design of the device was inspired by exit signs on top of doors to instill familiarity and was kept simple to reduce clutter. Concerns would have to be made about the maintainability and durability of the device as well as power consumption (probably a cabled connection), since it would be left for long periods of time on top of the doorway. There are no buttons or forms of interaction on the device itself as it operates as more of an indicator.

## Part F. Record

**Take a video of your prototyped interaction.**

[Prototype MP4 file](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/Part%20F.mp4)
([Google Drive link](https://drive.google.com/file/d/1SDP1MoYZn83hy0jhMh3ZugB5IA3T5ok2/view?usp=sharing))

**Please indicate anyone you collaborated with on this Lab.**

Kae-Jer (Mike) Cho, Ting-Yu (Angus) Lin, Ming-Chun (Jeff) Lu

# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.

## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

**Summarize feedback from your partners here.**

- Ming-Chun (Jeff) Lu: My guess for the scene: Covid Indicator ? Best idea ever! Only question is how does indicator determine whether the person got covid or not? Maybe by temperature?

- Kae-Jer (Mike) Cho: My guess for the scene: A covid patient detector! it’s so useful and can help a lot of people! my question is that how do you detect the covid? does it detect by body temperature? maybe you need a temperature sensor or an infrared thermometer!

- Ting-Yu (Angus) Lin: My guess for the scene: A sensor alerts and blocks people if their body temperature are too high. Thoughts: Greattt! I like the design which is totally feasible imho and very useful at the moment. Question: Some people who get COVID don’t show a high body temperature, thus I think for this issue I care more about if others wear reliable masks. Hence, maybe can this sensor detect whether the mask people putting on is surgical or not?

## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors, 
3) We will be grading with an emphasis on creativity. 

**Document everything here.**
## Part A. Plan 
**Describe your setting, players, activity and goals here.**

- _Setting:_ At home, in a room.

- _Players:_ Friends, people staying at home.

- _Activity:_ The device features two players, each with a copy of the device in their homes. Either person can change the color of the lamp, which causes the other lamp to mimic the color wirelessly. If bored, one can push down on the soft lamp to trigger a similar squashing of the lamp in the other person's house through servos mounted inside the lamp.

- _Goals:_ Players will feel less alone at home, with the lamp symbolizing the presence of someone else they can communicate to, while also not being over-intrusive on their daily lives. The physicality of the lamp being compressible from both ends further adds to the sense of companionship and fun.

**Include a picture of your storyboard here**

![Storyboard](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/Screenshot%202021-02-21%20at%2019.54.55.png)

**Summarize feedback you got here.**

- "It's a little useless for friends - since there's messaging XD"

- "More of a gag than a useful device"

- "Maybe you can add more interactivity for couples, especially long-distance relationships"

## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

**Are there things that seemed better on paper than acted out?**

- It seemed that showing the connectivity of the device (sending the signal to another device) would not be easy without some video editing/compositing.

**Are there new ideas that occur to you or your collaborators that come up from the acting?**

- Not really; though it was clear that the video had to be well choreographed to make editing easier.

## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

**Include your first attempts at recording the set-up video here.**

[Setup MP4 file](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/2%20Part%20D_1.mp4)
([Google Drive link](https://drive.google.com/file/d/1W1a-gAwLBgaC_DD04vFmlA2OsXmkCjuh/view?usp=sharing))

Now, change the goal within the same setting, and update the interaction with the paper prototype. 

**Show the follow-up work here.**

[Follow-up MP4 file](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/2%20Part%20D_2.mp4)
([Google Drive link](https://drive.google.com/file/d/1t1CJAj4gdWiXp4yr2DTkEfFi3e0VDFCn/view?usp=sharing))


## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

**Include sketches of what your device might look like here.**

![Sketch](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/Screenshot%202021-02-19%20at%2022.15.52.png)

**What concerns or opportunitities are influencing the way you've designed the device to look?**

The device would have to be made more ergonomic and stylish as to be nice to look at and not ruin the visual setting. The spherical minimalist shape was inspired by a Poké Ball. The lighting would have to be bright enough as to catch the attention of the other person on the receiving end of the communication. The soft body would ideally be made of silicone or some durable yet elastic material while also being translucent to light. The device would probably be wired since it would have to constantly be on to listen for/broadcast signals to other similar devices. Since the device would be placed on a surface, it would not need to be over-engineered in terms of durability as it would ideally not be moved around too much or fall to the ground.

## Part F. Record

**Take a video of your prototyped interaction.**

[Prototype MP4 file](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%201/2%20Part%20F.mp4)
([Google Drive link](https://drive.google.com/file/d/1ecy8bR27Gs-RrATIB3prQ0f_8kLWjjid/view?usp=sharing))

**Please indicate anyone you collaborated with on this Lab.**

Kae-Jer (Mike) Cho, Ting-Yu (Angus) Lin, Ming-Chun (Jeff) Lu, Eric Chen, Cheng-wei Hu
