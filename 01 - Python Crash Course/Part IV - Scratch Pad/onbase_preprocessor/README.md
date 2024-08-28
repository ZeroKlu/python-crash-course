# README #

This repository contains a template for an OnBase preprocessor.

### Purpose ###

* This preprocessor does not contain any file modification logic. It is 
intended to demonstrate the necessary code and procedure to use Python to 
develop a program meeting the OnBase preprocessor requirements.
    * Must be a compiled executable
        * We cannot pass a script to python.exe, as we would be unable to 
          capture the integer exit code from the preprocessor.
    * Must accept command-line arguments including:
        * %I (input file path)
        * %O (output file path)
    * Must return an integer exit code to identify success or failure
* Version 1.0.0.0

### How do I get set up? ###

* Install the necessary python library for creating an executable
    * ``` python.exe -m pip install pyinstaller```
    * *Note: Install this to your PC, not in a venv
* Create a JSON Configuration file including (at least) the following 
  values
    * "log_level" (string: accepts one of the following values):
        *  "debug"
        *  "info"
        *  "warn"
        *  "error"
 *  "log_dir" (string: accepts one of the following values):
    *  "A path to a directory where the log files will be generated (e.g.: C:\Temp)"
    *  "root" (log files will be stored in the directory containing the preprocessor)
    *  "logs" (log files will be stored in a subdirectory called "logs")

### Creating the EXE ###

* Deactivate your venv (if using one)
* Navigate your terminal to the directory where your preprocessor code exists, then run the following command
    * ```pyinstaller --onefile sample_preprocessor.py```
