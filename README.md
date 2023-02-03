# Feedback-Simulator
Developed by Dominik I. Braun.

## What is it?
This simulator is based on Python/PyQT and uses UDP to stream the feedback recorded from a Brain-Computer-Interface during an experiment. 

## Run the application
1. Download the repository
2. Go to ..\bin\dist\ 
3. Run the feedback_simulator.exe

## Add/remove receiving clients
Click on the "+" or "-" buttons to add or remove clients from the receiving list. When adding a new client, make sure that you enter a valid integer value in the input field.

## Start/Stop stream
Click on "Start Stream" to start streaming the data and on "Stop Streaming" to stop it.

## Format of the data
The application is written to stream a string with 9 comma separated values in the shape of an array. The values represent:

- value 0: thumb flexion
- value 1: thumb abduction
- value 2: index flexion
- value 3: middle flexion
- value 4: ring flexion
- value 5: pinky flexion
- value 6: wrist flexion/extension # Not working atm
- value 7: Empty
- value 8: wrist supination/pronation # Not working atm

Example String: "[value 0, value 1, value 2, value 3, value 4, value 5, value 6, value 7, value 8]". The string is encoded in utf-8 bytes.

## Let it stream to our Virtual Hand Interface
1. Download the Virtual Hand Interface from https://github.com/NsquaredLab/Virtual-Hand-Interface
2. Follow the instructions and connect the Virtual Hand Interface
3. Add the port of the Virtual Hand Interface to the feedback simulator
4. Start the stream!


Find us on our website: https://www.nsquared.tf.fau.de/ 

