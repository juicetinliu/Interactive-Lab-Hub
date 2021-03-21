# You're a wizard, Justin

<img src="https://pbs.twimg.com/media/Cen7qkHWIAAdKsB.jpg" height="400">

In this lab, we want you to practice wizarding an interactive device as discussed in class. We will focus on audio as the main modality for interaction but there is no reason these general techniques can't extend to video, haptics or other interactive mechanisms. In fact, you are welcome to add those to your project if they enhance your design.


## Text to Speech and Speech to Text

In the home directory of your Pi there is a folder called `text2speech` containing some shell scripts.

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav

```

you can run these examples by typing 
`./espeakdeom.sh`. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts

```

You can also play audio files directly with `aplay filename`.

After looking through this folder do the same for the `speech2text` folder. In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

## Serving Pages

In Lab 1 we served a webpage with flask. In this lab you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to [http://ixe00.local:5000]()


## Demo

In the [demo directory](./demo), you will find an example wizard of oz project you may use as a template. **You do not have to** feel free to get creative. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. You can control what system says from the controller as well.

## Optional

There is an included [dspeech](./dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. If you're interested in trying it out we suggest you create a seperarate virutalenv. 



# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller.

## Prep for Part 2

A Smart Heating System

![sketch](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%203/Lab3%20Part%202%20Prep.png)

## Share your idea sketches with Zoom Room mates and get feedback

*what was the feedback? Who did it come from?*

Pressing a button for voice activation is a little cumbersome; could be more intuitive with something similar to "hey siri" - Ming-Chun (Jeff) Lu

Will this system be compatible with other temperature sensors? Might be cool to implement it - Kae-Jer (Mike) Cho

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

### System
The system was split into 4 states:
#### Idle (when the system is waiting for voice input or not heating/cooling)
A button press on the knob takes us to the **Voice** state

![Idle](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%203/IMG_9743.png)

#### Voice (when the system is listening for voice input)
Once the user finishes speaking, they are taken either back to the **Idle** state or **Heating**/**Cooling** state.

![Voice](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%203/IMG_9744.png)

#### Cooling (when the system is cooling)
![Ice](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%203/IMG_9738.png)
 
#### Heating (when the system is heating)
![Fire](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%203/IMG_9739.png)

### Controller
The controller was done using the `pygame` library to take in keyboard inputs during runtime to minic voice controls. This was possible because the raspberry pi was connected through VNC Viewer.

*Include videos or screencaptures of both the system and the controller.*

Here's a video of the system tested by a willing volunteer:
[Test MP4 file](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%203/Voice%20Control_s.mov)
([Google Drive link](https://drive.google.com/file/d/1O-MXQU_KxH_AEgc1ZumEHCKSRQkbVon7/view?usp=sharing))

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

I got three people to test the system - Ming-Chun (Jeff) Lu, Kae-Jer (Mike) Cho, Yen-Hao (Eric) Chen!

Answer the following:

### What worked well about the system and what didn't?
It was very intuitive for users (the colored light on the knob helped users a lot by signalling what state the system was in). The animations also made the system much cooler. We didn't have access to a speaker for this lab so audio playback was not available.

### What worked well about the controller and what didn't?
The controller made it very easy to simulate actual voice controls without much latency or issues with recognition (since I was in control of the processing). The only possible drawbacks would be that I had to be in the same room as the user (could have used an audio streaming service). 

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
Latency can be a problem - if user interaction is the main focus then this can siginificantly impact the user's experience. Another issue can be how limiting the controller can be for the operator - only a set of limited actions can be chosen and run.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
Perhaps add a way to control the temperature output continuously instead of having single states for the cooling/heating/off functions. This could make the system seem much more realistic and interactive. Instead of just button/voice input we could also take in video input to see the user's body posture or even temperature sensors to make much better control decisions.
