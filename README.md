# Assignment 1 - Designing Models and Analyzing Data 

> * Participant name: Allison Gadd
> * Project Title: Entrance and Holding Area of a Subway Station

# General Introduction

The first part of this assignment explores designing models (and basic Python/Git features). 

We will look at **subway model in a city** system. A **subway system** is an underground, tube, or metro, underground railway system used to transport large numbers of passengers within urban and suburban areas - modern subways use different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently. 

The second part of the assignment explores data analysis. Data analysis and visualization is key to both the input and output of simulations. This assignment explores different random number generators, distributions, visualizations, and statistics. Additionally, it will look at getting you accustomed to specifying input and output variables to a system. We will also practice working with real data.


# Part 1: Designing a Model - Subway System

The problem is to look at the entrance of a subway station. It is important to make sure that there are enough automated ticket kiosks and automated turnstiles that no build up of people occurs at the entrance. Next is to look at the holding area to make sure it can accommodate the number of people through the turnstiles but are still waiting for the needed train. To make the wait bearable there would need to be benches and restrooms for those in transit. It is important to make sure that the trains come in a timely manner so that the holding area does not become over crowded. 

In the real world this issue of pedestrian conjestion actually led to Boston deciding that they needed a subway station. The engineers decided to model the system as a mix of London's underground tubes, and Paris' open-exacuation method of design.In the end it was determined that the subway didn't really help with the foot traffic, but it did help eleviate the congestion due to car traffic.

Brooks, R.B. 'History of the Boston Subway: The First Subway in America.' History of Massachusett.org. March 16, 2017.

![Image of Subway City System](https://github.com/IDS6145-Fall2019/assignment1-agadd881/blob/master/images/subway_turnstiles.png)

![Image of Subway City System](https://github.com/IDS6145-Fall2019/assignment1-agadd881/blob/master/images/busy_subway.png)

## (Part 1.1): Requirements (Experimental Design) **(10%)**

Requirements for an entrance to a subway station where there are ticket kiosks, turnstiles, and a holding area before travelers get on their train.

* There needs to be enough turnstiles to be able to get 100 people per minute through the entrance.

* There needs to be at least one turnstile that is handicap accessible.

* The holding area must be large enough to accommodate 2000 people at a time.

* There must be restrooms for various users: wheelchair users, parents, and companion stalls.

* On average a train should be through every 10 minutes in order to pick up new passengers to help clear out the holding area.

* If the ticket kiosks are automated, there must be at least one with braille access.

## (Part 1.2) Subway (My Problem) Model **(10%)**

* [**Object Diagram**](model/object_diagram.md) 
The Enterance includes the people, ticket kiosks, turnstiles, and a holding area.

* [**Class Diagram**](model/class_diagram.md) 
The people, turnstiles, ticket kiosks, and restrooms can be viewed in a break down of their accessibility.

* [**Behavior Diagram**](model/behavior_diagram.md) 
The activity diagram steps through how a traveler would go to the correct ticket kiosk to check or buy ticketts, and then would proceed to the correct turnstile based on the accessibilities that they require.

* [**Agent / User case**](model/agent_usecase_diagram.md) 
The use case diagram looks at how the travelers uses the entance system around them.

## (Part 1.3) Subway (My Problem) Simulation **(10%)**

The simulation type for getting the travelers through the ticket kiosks and turnstiles would be a discrete simulation. The system is a basic queuing type system where the traveler goes through the line/entrance and then waits in the holding area until their train arrives. This wait time would be a function of how early the traveler got to the station, and if their were any delays to the train route. If we look at needed number of turnstiles we could make the hypothesis that we would need 5 turnstiles with at least one being wheelchair accessible in order to meet the requirement of through put. This would be easy to note by changing the amount of These numbers would vary based on the popularity of the subway station and how many people each would have to accommodate.


## (Part 1.4) Subway City (My Problem) Model **(10%)**
[**Code template**](code/README.md) - 

Code in file ENTER.py It includes 4 classes for the subway entrance problem: people, ticket kiosk, turnstile, and restrooms. Within each class the variables are defined as True for the moment. Each class also has at least one function that was called in the main part of the program.


## (Part 1.5) Specifying the Inputs to a System **(10%)**

(remove the below points once ideas are satisfied)
* Specify the independent and dependent input variables of your subway esclator model
* Specify where the data will come from measured subset of real data (empirical) or synthetic data
* What kind of statistics are important to capture this input data
* How do you plan to analyze the output of your model?
* What ways will you visualize your data - charts, and graphs you will create?
* What clever way will you visualize your output with a useful infographic?



# Part 2: Creating a Model from Code

## (Part 2.1) **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model **(10%)**
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template for the code found in  [**the following folder**](code/POTS_system/). Please create a **class** diagram of this model (replace the placeholder diagram). (you can use paper and pencil or a digital tool).



# Part 3: Data Analysis

## (Part 3.1) - Real Data **(10%)**

Find a datasource that looks at part of this model - subway stations locations / escalator number, heights, widths / volume of passangers - ridership numbers   (*fits* - we are pretty loose here, it can be anything.)

* Write up a paragraph that describes the data and how it fits into your system.
* Load the data into Python
* Calculate a few useful statistic on the data - keep it simple- STD, means, etc..., this is just designed * to get used to working with real data. Explain the insights you derive from these statistics.
* Visualize the raw data - visualize a few critical aspects of the data to better describe what it is, what it is showing, and why its useful to your system.
* Calculate and plot some summary statistics that better describe the data.

(Add your plots and visualization here)
(Put your data into the data directory)


## (Part 3.2) -  Plotting 2D Random Number Generators **(15%)**

Based on the figure below it can be seen that as N increased, the area is covered more fully. Another thing to note in the figure is that the pseudo-random numbers have more blank spaces as the numbers are more 'random', while the quasi-random figures show that it tries to fill in the blank space more.

![Image of 2d template City](https://github.com/IDS6145-Fall2019/assignment1-agadd881/blob/master/images/Random_Num.png)


## (Part 3.3) -  Plotting 1D Random Distributions **(15%)**

Now, choose three different distributions to plot in 1D, or as a histogram. Choose a pseudo-random generator and generate three different distributions. Example distributions are Uniform (part 8), Normal, Exponential, Poisson, and Chi-Squared, but feel free to use any three distributions of your choice. Again, plot each distribution for five different Ns. This will result in 15 different subplots, formatted similar to the image in Part 8. Include your properly formmated 1D plots below and breifly describe what we are looking at and how things change as N is changed.

Repeat the above using a quasi-random generator. Discuss the similarities and differences.
