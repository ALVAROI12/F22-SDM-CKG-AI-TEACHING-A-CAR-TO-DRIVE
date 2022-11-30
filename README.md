# How_to_simulate_a_self_driving_car UIW FALL 2022
This is the code for "How to Simulate a Self-Driving Car" by Siraj Raval on Youtube

# We used this video from youtube to help us deploy the simulator but we made adjustments.

## Overview

This is the code for [this](https://youtu.be/EaY5QiZwSP4) video on Youtube by Siraj Raval. We used the use Udacity's [self driving car simulator](https://github.com/udacity/self-driving-car-sim) as a testbed for training an autonomous car. But we found a problem due to the lack of libraries for the version 3.5 of Python.

## Dependencies

You can install all dependencies by running one of the following commands

You need a [anaconda](https://www.continuum.io/downloads) or [miniconda](https://conda.io/miniconda.html) to use the environment setting.

```python
# Use TensorFlow without GPU
conda env create -f environments.yml 

# Use TensorFlow with GPU
conda env create -f environment-gpu.yml
```

Or you can manually install the required libraries (see the contents of the environemnt*.yml files) using pip.

----------------------------------------------------------------------------------------------------------------------------------------------------------
You can use both codes but i highly recomend use the googlecolab one if you do not want to deal with more issues. Do not need to install libraries.


## Gathering Data

The Udacity provided dataset works well but it is not enough to get the car running in difficult terrain (like the second track in Udacity simulator). To gather the data from track 2, we would first need to create a folder in our project directory. Let’s call this folder- data. Now, fire up our simulator. Select the second track from the menu and go to the training mode option.
Once you enter the training mode, you shall see a record option on the top right corner of the screen. Click on the icon and browse to the data folder. Press select.
You can start recording your ride once you press the record icon again! Now, if you are a novice gamer like me, I would suggest to take things slow and try to make sure your car stays at the center of the road as much possible, even during the turns. This would help to get better training data that will eventually make a good model. We will record 2 laps driving in one direction of the track and also 2 more laps driving in the opposite direction to make sure the turns are reversed. This would make sure our model does not overfit and make better left and right turns.

# Download the model.h5 file in the same directory if you had been using Google Colab to write your code. Fire up the terminal, cd to your directory and run the script with our model:

python drive.py model.h5 


