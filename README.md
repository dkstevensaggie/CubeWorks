# CubeWorks
Flight software for the GASPACS mission written in Python, with some compents in c.

## Introduction
The Get Away Special Passive Attitude Control Satellite (GASPACS) is an experimental 1U cubesat in development by Utah State University's Get Away Special team.  The purpose of the experiment is to test the viability of an inflatable aero-stabilization boom deployable component in Low Earth Orbit (LEO).  This repository contains CubeWorks, the flight software for the satellite.

## Objectives
CubeWorks is intended to be a robust, modular, and fault tolerant software framework for small satellites, with minimal barrier to entry.  The experienced developer may be asking, "Why write the entire framework in python and not a more performant language with closer hardware interaction?"  The answer is because the framework is designed to be accessible to newer developers who want to get into space research.  The software isn't as performant as an equivalent solution written in, say, c++ but it isn't designed to be.   

Framework components are designed to be modular, and easy to add to and remove from a given system.  All that is needed is to define a driver that interacts with your hardware components and inherits from the built in `Component` class, and include it in the main file.  

## Installation
The CubeWorks software module is designed to run on a Raspberry Pi Zero W running Raspbian as its operating system.  For production, Raspbian without the desktop environment will be used, but during development the DE is fine to use.  For development, using a Raspberry Pi 3 B+ is fine.  The framework has not been tested on a Pi 4, but since it's all in python, it should run just fine.  

### Installation Process
4. Image a Raspberry Pi with Raspbian and boot the Pi
5. Once booted, install the following dependencies:
	- Python3, `sudo apt install python3`
	- python3-pip, `sudo apt install python3-pip`
6. Clone this repository onto the pi, `git clone https://github.com/SmallSatGasTeam/CubeWorks.git`
6. Move into the root directory of the project, `$ cd CubeWorks` 
6. Install dependencies with `$ pip3 install -r requirements.txt`
7. To run the project, `cd` into the CubeWorks directory and run: `python3 main.py`

## Documentation

This project is documented using Doxygen.  Instructions for building the docs are located in `CubeWorks/docs/README.md`.  

### File Structure
This file structure comprises the major compoments of CubeWorks.  

```
CubeWorks
├── Components
│   ├── Component.py
│   ├── ContextPrinter.py
│   ├── Database.py
│   └── __init__.py
├── Drivers
│   ├── driver0
│   │   ├── driver0.py
│   │   └── __init__.py
│   └── driver1
│       ├── driver1.py
│       └── __init__.py
├── main.py
├── mission_modes.py
├── README.md
├── tests
│   └── unit_testing_example.py
├── unit_tests.py
└── watchdog
```

### Class Structure

![CubeWorks_UML](https://github.com/SmallSatGasTeam/GASPACS/blob/master/docs/CubeWorks_UML.png)
