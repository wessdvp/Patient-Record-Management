# BMI Calculator

This is a simple BMI (Body Mass Index) calculator built using Python's Tkinter library. The application allows users to input their weight and height, then calculates and displays their BMI. Additionally, it features a color-coded bar that visually represents the BMI range.

## Features

- **User Input**: Allows users to input their weight (in kilograms) and height (in meters).
- **BMI Calculation**: Calculates BMI upon entering details and clicking the "Calculate BMI" button.
- **BMI Result Display**: Displays the calculated BMI on the screen with the associated BMI category.
- **BMI Range Bar**: A visual bar that changes color based on the calculated BMI, indicating the BMI category (e.g., normal weight, overweight, obesity).

## BMI Ranges and Colors

- **Under 18.5**: Blue (Underweight)
- **18.5 - 24.9**: Green (Normal weight)
- **25 - 29.9**: Yellow (Overweight)
- **30 - 34.9**: Orange (Moderately obese)
- **35 - 39.9**: Red (Severely obese)
- **40+**: Brown (Morbidly obese)

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. This script uses the Tkinter library, which is included with Python.

### Installation

1. Clone this repository or download the script file.
2. Run the script using Python.

### Usage

1. Enter your weight in kilograms in the "Weight (kg)" field.
2. Enter your height in meters in the "Height (m)" field.
3. Click the "Calculate BMI" button.
4. Your BMI will be displayed, along with a color-coded bar indicating your BMI range.

## Code Overview

- **`calculate_bmi()`**: Retrieves the weight and height inputs, calculates the BMI, and updates the result label and the BMI range bar.
- **`update_bar(bmi)`**: Updates the color and width of the BMI range bar based on the calculated BMI value.
- **Tkinter GUI Elements**: The GUI is built using Tkinter, with labels, entry fields, and a canvas for the visual BMI bar.

## Example

If the user inputs a weight of 70 kg and a height of 1.75 m:

- The calculated BMI will be 22.86.
- The result will be displayed as `BMI: 22.86`.
- The obesity class will be displayed as `Normal weight`.
- The BMI range bar will be green, indicating normal weight.

## Dependencies

- **tkinter** (for the GUI)

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Version History

- **v1.0**: Initial release of the code.
- **v1.1**:
  - Fixed BMI classification to align with medical guidelines.
  - Added the underweight category.
  - Added text labels for obesity classes:
    - Underweight: BMI < 18.5
    - Normal weight: BMI 18.5 to 24.9
    - Overweight: BMI 25 to 29.9
    - Moderately obese: BMI 30 to 34.9
    - Severely obese: BMI 35 to 39.9
    - Morbidly obese: BMI ≥ 40
