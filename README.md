# Simulation of the operation of a smart home system

## A project written in the Django framework, implementing the functionality of a smart home system, with software simulation of the operation of sensors.

In this project, the program simulates the operation of sensors: after a certain period of time, sensors are randomly selected whose readings change. The system registers changes in sensor readings and, according to the initially specified rules, checks whether the state of the devices needs to be changed; if necessary, the states are changed in accordance with the specified rules.
The project includes:

* the core application, which is responsible for displaying the states of devices and sensor readings, as well as for executing specified rules when reading changes in sensor readings
* the sensors application, which is responsible for the logic of the sensors, including the generation of random indicators in a certain range
* automation application that contains the logic for checking the given rules and their execution

# How to install this Python Project

1. clone this repository
2. make sure you have Python 3.10 or higher
3. go to the project repository on your device, open a terminal and enter the command 'pip install -r requirements.txt' to install the required libraries
4. enter the command 'cd smart_home_project' into the terminal
5. enter the command 'python manage.py runserver' into the terminal
6. go to the website at the address indicated in the terminal
7. to run the sensors, open a second terminal, enter the command 'cd smart_home_project' in the terminal again, and then enter this command in the terminal 'python manage.py run_sensors'
8. to add new devices, sensors and rules go to the Django admin panel, to do this in the address bar of the site you need to add /admin and enter the administrator data: username - admin and password - 19248ukasjndf

