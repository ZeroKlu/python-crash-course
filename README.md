# README #

### What is this repository for? ###

* This repository contains all the code samples (as well as my comments and 
  some additional lessons) for a planned 8-week Python training course.
* For this training course, we use the following textbook:
    * Title: Python Crash Course
    * Author: Eric Matthes
    * ISBN:
        * 2nd edition: 978-1593279288<br>[Amazon Link](https://www.amazon.com/Python-Crash-Course-Eric-Matthes/dp/1718502702)
        * 3rd edition: 978-1718502703<br>[Amazon Link](https://www.amazon.com/Python-Crash-Course-2nd-Edition/dp/1593279280)
    * Textbook Resources:
        * [2nd Edition Downloads](https://github.com/ehmatthes/pcc_2e/zipball/master/)
        * [3rd Edition Downloads](https://github.com/ehmatthes/pcc_3e/archive/refs/heads/main.zip)

### How do I get set up? ###

* Follow setup steps in:
    * [Setting Up Your Workstation for Development Training.pdf](./00%20-%20Resources/Setup%20Documents/01%20Setting%20Up%20Your%20Workstation%20for%20Development%20Training.pdf)
    * [Setting Up Your Workstation for Python Training.pdf](./00%20-%20Resources/Setup%20Documents/02%20Setting%20Up%20Your%20Workstation%20for%20Python%20Training.pdf)

* Create a virtual environment
    * ```python.exe -m venv .venv``` 
* Activate your virtual environment
    * ```.venv\Scripts\activate```
* Update PIP in the virtual environment
    * ```python.exe -m pip install --upgrade pip```
* Install my utility functions
    * ```python.exe -m pip install sm_utils```
* Install the libraries used by the textbook.<br>Note: You can wait until the specified chapter to install if you prefer.
    * (Chapter 11 - Testing)
        * Pytest: ```python.exe -m pip install pytest```
    * (Chapter 12-14 - Alien Invasion)
        * PyGame: ```python.exe -m pip install pygame```
    * (Chapter 15-17 - Data Visualization)
        * Matplotlib: ```python.exe -m pip install matplotlib```
        * Requests: ```python.exe -m pip install requests```
        * Plotly (2nd ed): ```python.exe -m pip install plotly```
        * Plotly Express (3rd ed): ```python.exe -m pip install plotly.express```
    * (Chapter 18-20 - Web Portal)
        * Django: ```python.exe -m pip install django```
* Some of the examples I provide include languages other than Python.  
  For these, you may need to install this extension in VS Code:
    * [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)

### Documentation ###

* All documentation located in the [Setup Documents](./00%20-%20Resources/Setup%20Documents/) folder.

### Who do I talk to? ###

* Any questions can be addressed to [zeroklu@protonmail.com](mailto:zeroklu@protonmail.com?subject=Python%20Training%20Repository%20Feedback)
