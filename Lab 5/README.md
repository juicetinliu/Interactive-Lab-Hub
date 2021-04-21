# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.


## Prep

1.  Pull the new Github Repo.
2.  Read about [OpenCV](https://opencv.org/about/).
3.  Read Belloti, et al's [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf)

### For the lab, you will need:

1. Raspberry Pi
1. Raspberry Pi Camera (2.1)
1. Microphone (if you want speech or sound input)
1. Webcam (if you want to be able to locate the camera more flexibly than the Pi Camera)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.


## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

Befor you get started connect the RaspberryPi Camera V2. [The Pi hut has a great explanation on how to do that](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera).  

#### OpenCV
A more traditional to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python.

Additionally, we also included 4 standard OpenCV examples. These examples include contour(blob) detection, face detection with the ``Haarcascade``, flow detection(a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (I.e. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example.

```shell
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```
#### Filtering, FFTs, and Time Series data. (beta, optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the set up from the [Lab 3 demo](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%203/demo) and the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

Include links to your code here, and put the code for these in your repo--they will come in handy later.

Run `part_A.py` and enter either 1, 2, or 3 to run each example!
https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/part_A.py

#### Teachable Machines (beta, optional)
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple.  However, its simplicity is very useful for experimenting with the capabilities of this technology.

You can train a Model on your browser, experiment with its performance, and then port it to the Raspberry Pi to do even its task on the device.

Here is Adafruit's directions on using Raspberry Pi and the Pi camera with Teachable Machines:

1. [Setup](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/raspberry-pi-setup)
2. Install Tensorflow: Like [this](https://learn.adafruit.com/running-tensorflow-lite-on-the-raspberry-pi-4/tensorflow-lite-2-setup), but use this [pre-built binary](https://github.com/bitsy-ai/tensorflow-arm-bin/) [the file](https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl) for Tensorflow, it will speed things up a lot.
3. [Collect data and train models using the PiCam](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/training)
4. [Export and run trained models on the Pi](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/transferring-to-the-pi)

Alternative less steps option is [here](https://github.com/FAR-Lab/TensorflowonThePi).

#### PyTorch  
As a note, the global Python install contains also a PyTorch installation. That can be experimented with as well if you are so inclined.

### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interactions outputs and inputs.
**Describe and detail the interaction, as well as your experimentation.**

A reaction detection system that could be implemented in virtual lectures that could simplify feedback/surveys in class and make classes more engaging. When the teacher asks a question and wants to gather everyone's feedback, students can then simply raise a thumbs up or thumbs down on their video and a system would tally the total number of yes/no's present in the virtual classroom. This could speed up the process of gathering lots of answers but make the experience much more fun for students rather than filling out surveys or pressing buttons. Perhaps this could be extended to detect things like numbers (as represented by number of fingers raised), or even objects and facial expressions.

A google TeachableMachine was trained to detect either a thumbs up or thumbs down or nothing.

![training](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/Screenshot%202021-04-21%20at%2000.49.51.png)

[Try out the trained model with your webcam!](https://teachablemachine.withgoogle.com/models/G2kI-ujkA/)

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note your observations**:
For example:
1. When does it do what it is supposed to do?

The model works well for most cases (with myself in the camera) due to the large number of training images used - (different thumbs up/thumbs down gestures, two/one hands, face/no face, no gestures).

2. When does it fail?

The model has a hard time detecting thumbs up/down when the hand is slighly obstructed; it sometimes detects thumbs up/down even when there is no hand gesture. When I turn my head to the side, it detects it as a thumbs down; when I turn my head upwards, it detects a thumbs up!

![Fail](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/Screenshot%202021-04-21%20at%2001.07.20.png)


3. When it fails, why does it fail?

The failures are likely due to the training data not covering a wide enough variety of scenarios such as different background colors, face types, lighting conditions, etc.

4. Based on the behavior you have seen, what other scenarios could cause problems?

Perhaps it may not detect a thumbs up/down at all if another person were in front of the camera; if the background changes then it may also have trouble detecting gestures or may mistake variances in lighting as a gesture. If someone associates a different gesture with yes/no then it could also pose problems - the model expects only thumbs up/down as yes/no.

**Think about someone using the system. Describe how you think this will work.**
1. Are they aware of the uncertainties in the system?

They would not be; if a system like this were implemented in a product like Zoom, people would likely expect it to work flawlessly.

2. How bad would they be impacted by a miss classification?

For the individual using the system, a miss classification would not impact him/her much unless answering a question had consequences - group forming, graded quiz, etc. For the class as a whole, a lot of miss-classifications could greatly impact the overall yes/no score for the entire class' results.

3. How could change your interactive system to address this?

Have some sort of disclaimer; include buttons in the quiz system so their is always fallback to simpler methods of answer; perhaps even include a calibration sequence to allow students to train their own model before answering to increase accuracy.

4. Are there optimizations you can try to do on your sense-making algorithm.

Use more training data: 
- Record friends making gestures
- Find different backgrounds and lighting conditions
- Include more output classes? Perhaps a 'maybe' option to reduce the confusion of the model

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**Include a short video demonstrating the answers to these questions.**
What can you use X for?

Gesture recognition is great for videos, accesibility, and classifying complex body motions to simpler categories for other applications.

What is a good environment for X?

A controlled environment where the video resolution is great, lighting conditions are fair and the data isn't too noisy (only one person's gesture at a time).

* What is a bad environment for X?

Somewhere with lots of noisy data: a crowd of people making a gesture, bad lighting with lots of variance, or poor video quality in general.

* When will X break?

In any of the bad environments mentioned above; if the gestures made aren't expected by the trained model.

* When it breaks how will X break?

Depending on the input, it would either not detect a gesture (false negatives), or mistakenly detect a gesture when there isn't one (false positives).

* What are other properties/behaviors of X?

It is able to detect things that weren't in the training data - I only trained the model with a single thumbs up/down but the model was able to correctly give a yes/no output when I put two thumbs up/down.

* How does X feel?

It feels awesome when it works, as if the computer can magically understand what your hand is signalling. Using body language is almost something that is completely exclusive to human-human interaction, so seeing a computer able to detect these body motions is quite amazing.

[Model in Action MP4 file](https://github.com/juicetinliu/Interactive-Lab-Hub/blob/Spring2021/Lab%205/Screen%20Recording%202021-04-21%20at%2001.24.50.mov)
[(Google Drive link)](https://drive.google.com/file/d/1U5kffuy9L7WGTMCRxQ9XSa9b7aTx6g0W/view?usp=sharing)

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**Include a short video demonstrating the finished result.**

