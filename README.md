# Meal Planner Application

This Python program is a Meal Planner application built using the Tkinter library for the GUI and PIL (Python Imaging Library) for image processing. It offers users a convenient way to plan their meals for the week based on their desired calorie intake. Below is an overview of its functionality:

## Features:

1. **Graph Class**:
   - Defines a `Graph` class representing a graph data structure using a dictionary of lists.
   - Provides methods to add edges between nodes.

2. **MealPlannerApp Class**:
   - Subclass of `tk.Tk`, serving as the main application window.
   - Initializes GUI elements like labels, buttons, and frames.
   - Allows users to input a target calorie value for their meals.
   - Generates a random weekly meal plan based on the target calorie range and meal options.
   - Displays the generated meal plan in a text area.

3. **GUI Elements**:
   - Utilizes Tkinter's widgets such as `Label`, `Button`, `Entry`, and `Text` for user interaction.
   - Incorporates images using PIL and Tkinter's `Label` widget to enhance the visual appeal.

4. **Functionality**:
   - Enables users to set a target calorie value for their meals.
   - Randomly selects breakfast, lunch, and dinner options that match the target calorie range to create a weekly meal plan.
   - Presents the generated meal plan in a readable format within the application.

5. **Meal Options and Days**:
   - Defines a list of meal options with attributes such as name, calories, cost, and meal type (e.g., breakfast, lunch, dinner).
   - Specifies the days of the week for scheduling meals.

6. **Main Application Execution**:
   - Instantiates the `MealPlannerApp` class.
   - Initializes and starts the Tkinter event loop to execute the application.

## Requirements:
- Python 3.x
- Tkinter
- PIL (Python Imaging Library)

## Usage:
1. Clone the repository:
   ```
   git clone https://github.com/your_username/meal-planner.git
   ```
2. Navigate to the repository directory:
   ```
   cd meal-planner
   ```
3. Run the Python script:
   ```
   python meal_planner.py
   ```
4. Follow the on-screen instructions to input your desired calorie target and view the generated meal plan.

## Notes:
- Ensure you have Python and the required libraries installed on your system before running the application.
- Customize the meal options and days of the week according to your preferences by modifying the provided data.
- Experiment with different calorie targets and meal options to plan diverse and balanced weekly meals.

## License:
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments:
Special thanks to the developers of Tkinter and PIL for their valuable contributions to the Python ecosystem.
