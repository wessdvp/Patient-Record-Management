# Patient Record Management Application

## Overview

The PatientManager application is a user-friendly tool for managing patient records. Developed with Python's `tkinter` library, this application allows you to easily add, retrieve, and view patient information through a graphical user interface (GUI).

## Features

- **Add Patient**: Input and save patient details including name, age, gender, and medical history.
- **Retrieve Patient**: Search for a patient by name and view their details.
- **View Patient List**: Display a list of all registered patients and view their information.

## Notice

Please be aware that all data entered into the application will be lost when the application is closed. This application does not persist data beyond the current session. If you need to keep patient records, please consider modifying the application to save data to a file or database.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. This script uses the Tkinter library, which is included with Python.

### Installation

- Clone this repository or download the script file.
- Run the script using Python.


### Interact with the Application

   - **Add Patient**:
     1. Click on the "Add Patient" button on the main menu.
     2. A new screen will appear asking for patient information.
     3. You will be prompted to enter the patient’s name, age, gender (M/F), and medical history one by one.
     4. After entering each field, click the "Next" button to proceed to the next field.
     5. Once all fields are filled out, the patient’s details will be saved, and you will be returned to the main menu.

   - **Retrieve Patient**:
     1. Click on the "Retrieve Patient" button on the main menu.
     2. A search screen will appear asking you to enter the patient's name.
     3. Type the name of the patient you wish to search for and click the "Search" button.
     4. If the patient is found, their details will be displayed. If not, an error message will appear indicating that the patient does not exist.
     5. To return to the main menu, click the "← Return to Main Menu" button.

   - **View Patient List**:
     1. Click on the "View Patient List" button on the main menu.
     2. A new window will open displaying a list of all registered patients.
     3. Scroll through the list to view patient names.
     4. Double-click on a patient’s name to see detailed information about that patient.
     5. To return to the main menu, click the "← Return to Main Menu" button.

## Dependencies

- Python 3.x (includes `tkinter`)

No additional libraries are required as `tkinter` is included with Python's standard library.

## License

This project is licensed under the MIT License. See the LICENSE.txt file for details.
