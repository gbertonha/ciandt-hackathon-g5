# Welcome to 3rd CI&T Japan Hackathon
## SAVE THE WORLD! IoT

## Table of contents
* [Introduction](#introduction)
* [Rules and Regulations](#rules-and-regulations)
	* [General Rules](#general-rules)
	* [Minimum Requirements](#minimum-requirements)
	* [Judging Criteria](#judging-criteria)
* [Challenge](#challenge)
	* [Overall Architecture](#overall-architecture)
	* [Technologies](#technologies)
		* [Firebase](#firebase)
		* [Raspberry Pi](#raspberry-pi)
	* [Folder and Files Structure](#folder-and-files-structure)
	* [Environment setup](#environment-setup)

## Introduction
We are CI&T Japan, part of the global digital technology agency CI&T. Our team of experts perfectly mix Lean Principles, Design Thinking and Agile Development techniques to provide Global, Regional and Japanese enterprises what it takes to digitally transform themselves in the Japanese market.
We are really glad to have you here today and we hope you have fun with us!

A hackathon (also known as a hack day, hackfest or codefest) is a design sprint-like event in which computer programmers and others involved in software development collaborate intensively on software projects. Hackathons usually are about specific subjects and today the subject is "SAVE THE WORLD! IoT".
	
## Rules and Regulations
Although the main target for today's event is to have fun, there are a few rules and regulations that you need to be aware about in order to be eligible to became today's winner. 

### General Rules
All the participants will be splited in 4 different groups. Each team member will be decided in a draw, however in order to balance the groups the event organization might split some people based on their professional profiles.
The group members need to organize themselves and work as a team. However only 2 computers will be allowed for each team.
The event organization will provide a set for each group composed by the following:

(1) A Raspberry Pi 3 Model b+
(2) A humidity and temperature sensor (DHT11)
(3) An air pressure sensor (BMP180) 

The Raspberry Pi is already connected to Firebase's Firestore database and saving the data that is been read from the sensors each 30 seconds and displayed in a Web interface.

### Minimum Requirements
The proposed idea must be related to "SAVE THE WORLD" theme. In other words, the group need to come up with ideas related to things that may help on world causes such as saving natural resources, saving the environment, sustainability, education or anything that may be helpful for the humanity as a whole.
It is mandatory to use at least (1) Raspberry Pi, (2) One of the sensors provided by the organization and (3) Firebase, however you can modify the project or include any other technologies as wanted.

### Judging Criteria
The winner group will be decided acording the following table:

| Criteria | Points |
| :---: | :---: |
| Code quality & Technical Difficulty | 300 |
| Teamwork | 300 |
| Impressiveness | 200 |
| Usefulness/Practicality | 100 |
| Business Potential | 50 |

#### Code quality & Technical Difficulty
#### Teamwork
#### Impressiveness
#### Usefulness/Practicality
#### Business Potential

## Challenge
Our CI&T's skilled Engineers have prepared a codebase at github. The solution is already up and running, end to end.
Your mission is to envolve this code to something really cool that will make your group to be today's winner. But be careful! The time is short and it is necessary to come up with an idea that you will be able to finish by 19:00.  
There is a Raspberry Pi with 2 sensors connected on it. The first sensor (DHT11) is reading information about both temperature and humidity. The second one (BMP180) is measuring the atmosphere pressure.
This Raspberry Pi will save the information to Firebase's Firestore database each 2 minutes.
There is a dashboard hosted by Firebase that is reading the information and displaying on the screen. You can acccess the dashboard from the following URLs:

https://ciandt-hackathon-g1.firebaseapp.com  
https://ciandt-hackathon-g2.firebaseapp.com  
https://ciandt-hackathon-g3.firebaseapp.com  
https://ciandt-hackathon-g4.firebaseapp.com  

Your URL depends on which group you belong to (g1, g2, g3 or g4).

### Overall Architecture
The following diagram illustrates the overall architecture of the solution that was explained in the previous section:

![Overall Architecture](https://drive.google.com/uc?export=view&id=1hO1idz7HfCsL2GmfB3AhCtyb5ngqYYpJ)


### Technologies
This section introduces the technologies used on this Hackathon.

#### Firebase
Firebase is a product powered by Google which allows to build apps fast, without managing infrastructure.
On this challange, we will use Firebase for host our web application and our database.  
https://firebase.google.com/  
Please be informed that there is a limit of free API calls that can be done to Firebase. Please check the details in here:  
https://firebase.google.com/pricing

#### Raspberry Pi
The Raspberry Pi is a series of small single-board computers. The sensors will be plugged in Raspberry Pi which will send the information to Firebase's database.  
https://www.raspberrypi.org/

## Folder and Files Structure
The official github repository (https://github.com/geovanneb/ciandt-hackathon) for the Hackathon is using the following folder structure:
```
ciandt-hackathon
  ├── iot #contains the python code shipped on Raspberry Pi
    ├── main.py #main python file 
    ├── vendor #contains third party libraries
  ├── web-ui #contains the Firebase project (Web UI).
    ├── firebase.json #Firebase's configuration file
    ├── public #contains Web UI HTML / CSS / JS files
```

## Environment setup
Make sure that all team members has a github account, then go to the official repository and fork it:
https://github.com/geovanneb/ciandt-hackathon
It is very important during the Hackathon to keep pushing your progress to github, so the organization can check the code being produced by your team.  
Refrain from pushing all code at once just at the end of the event!

### Local Environment
Clone the repository on your computer:
```
$ git clone git@github.com:geovanneb/ciandt-hackathon.git
```

Install Firebase CLI:
```
npm install -g firebase-tools
```

Make sure that you have a google account and that someone from the event organization has granted you admin permissions to your goup's Firebase account.  
Login with your Google Account and select your project
```
firebase login
```

### Run Web UI on your local machine
You can validate your Web UI at any time by running it on your local computer before deploying to Firebase hosting.

```
firebase serve
```

### Deploy Web UI to Firebase hosting
After checking on your local computer, you can deploy your application to Firebase hosting and make it available online:

```
firebase deploy --only hosting
```
After deploying, it should be available from the following URL address (depending on your group number):  
https://ciandt-hackathon-g1.firebaseapp.com  
https://ciandt-hackathon-g2.firebaseapp.com  
https://ciandt-hackathon-g3.firebaseapp.com  
https://ciandt-hackathon-g4.firebaseapp.com 

Your URL depends on which group you belong to (g1, g2, g3 or g4).


### Develop python code on Raspberry Pi

There is a monitor, a keyboard and a mouse that is plugged to your Raspberry Pi. Look to your monitor. You should see the operation system interface that is running on your Raspberry Pi. There is an IDE called Thonny that can be accessed under Menu > Programming. Thonny is a new IDE (integrated development environment) bundled with the latest version of the Raspbian with PIXEL operating system. Using Thonny, it’s now much easier to learn to code. Thonny comes with Python 3.6 built in, so you don’t need to install anything.  
When you start Thonny, you’ll see a new script editor and a shell. As with Python 2/3 IDLE, you enter a program in the script editor and run it in the shell. You can then use the shell to interact directly with the program; accessing variables, objects, and other program features.

```
Instructions here
```