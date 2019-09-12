# Welcome to 3rd CI&T Japan Hackathon
## SAVE THE WORLD! Subculture x IoT

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

A hackathon (also known as a hack day, hackfest or codefest) is a design sprint-like event in which computer programmers and others involved in software development collaborate intensively on software projects. Hackathons usually are about specific subjects and today the subject is "SAVE THE WORLD! Subculture x IoT".
	
## Rules and Regulations
Although the main target for today's event is to have fun, there are a few rules and regulations that you need to know in order to be eligible to be today's winner. 

### General Rules
All the participants will be splited in 4 different groups. Each team member will be decided in a draw, however the event organization might split some people based on professional profiles.
The group members need to organize themselves and work as a team. However only one computer will be allowed for each team.
The event organization will provide a set for each group composed by the following:

(1) A Raspberry Pi
(2) A sensor kit

The Raspberry Pi is already connected to Firebase's Firestore database and saving the data that is been read from the sensors each 30 seconds and displayed in a Web interface.

### Minimum Requirements
The proposed idea must be related to "SAVE THE WORLD" theme. In other words, the group need to come up with ideas related to things that may help on world causes such as saving natural resources, saving the environment, sustainability, edutation or anything related to the theme.
It is mandatory to use at least (1) Raspberry Pi and (2) Firebase, however it is allowed to include any other technologies if wanted.

### Judging Criteria

## Challenge
This project is simple Lorem ipsum dolor generator.

### Overall Architecture
The following diagram illustrates the overall architecture for today's Hackathon:

![Overall Architecture](https://drive.google.com/uc?export=view&id=15Ef0CSe3NhDkXl4YrWqAMAsPTKn9_C4j)


### Technologies
This section introduces the technologies used on this Hackathon.

#### Firebase
Firebase is a product powered by Google which allows to build apps fast, without managing infrastructure.
On this challange, we will use Firebase for host our web application and our database.
https://firebase.google.com/

#### Raspberry Pi
The Raspberry Pi is a series of small single-board computers. The sensors will be plugged in Raspberry Pi which will send the information to Firebase's database.
https://www.raspberrypi.org/

## Folder and Files Structure
The officil github repository (https://github.com/geovanneb/ciandt-hackathon) for the Hackathon is using the following folder structure:
```
ciandt-hackathon
  ├── iot #contains the python code shiped on Raspberry Pi
  ├── web-ui #contains the Firebase project (Web user interface).
```

## Environment setup
Make sure that all team members has a github account, then go to the official repository and fork it:
https://github.com/geovanneb/ciandt-hackathon

### Local Environment
Clone the repository on your computer:
```
$ git clone git@github.com:geovanneb/ciandt-hackathon.git
```

Install Firebase CLI:
```
npm install -g firebase-tools
```

Login with your Google Account and select your project
```
firebase login
```

### Deploy Web UI to Firebase hosting

```
firebase deploy --only hosting
```

### Deploy python code to Raspberry Pi
```
Instructions here
```