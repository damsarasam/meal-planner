import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from collections import defaultdict
import random

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[tuple(u)].append(tuple(v))
        self.graph[tuple(v)].append(tuple(u))

class MealPlannerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Meal Planner")
        self.geometry("800x600")
        
        # Background Image
        self.background_image = self.get_background_image()
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Home Page
        self.home_label = ttk.Label(self, text="Welcome to our Meal Planner!", font=("Arial", 24, "bold"))
        self.home_label.pack(pady=100)

        self.start_button = ttk.Button(self, text="Get Started", command=self.show_weekly_plan)
        self.start_button.pack(pady=10)

        # Weekly Plan Page
        self.weekly_plan_frame = ttk.Frame(self)

        self.calorie_label = ttk.Label(self.weekly_plan_frame, text="Target Calories:", font=("Arial", 12))
        self.calorie_label.grid(row=0, column=0, padx=10, pady=10)

        self.calorie_entry = ttk.Entry(self.weekly_plan_frame)
        self.calorie_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = ttk.Button(self.weekly_plan_frame, text="Generate Plan", command=self.generate_weekly_plan)
        self.generate_button.grid(row=0, column=2, padx=10, pady=10)

        self.result_text = tk.Text(self.weekly_plan_frame, width=60, height=20, font=("Arial", 12))
        self.result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def show_weekly_plan(self):
        self.home_label.pack_forget()
        self.start_button.pack_forget()
        self.weekly_plan_frame.pack(pady=50)

    def generate_weekly_plan(self):
        target_calories = int(self.calorie_entry.get())

        meal_graph = Graph()
        breakfast_options = []
        lunch_options = []
        dinner_options = []

        for i in range(len(meal_options)):
            for j in range(i + 1, len(meal_options)):
                calorie_diff = abs(meal_options[i]["calories"] - meal_options[j]["calories"])
                cost_diff = abs(meal_options[i]["cost"] - meal_options[j]["cost"])
                if calorie_diff <= target_calories:
                    meal_graph.add_edge(meal_options[i], meal_options[j])
                    meal_graph.add_edge(meal_options[j], meal_options[i])
                    if meal_options[i]["meal_type"] == "Breakfast" and meal_options[j]["meal_type"] == "Breakfast":
                        breakfast_options.append((meal_options[i], meal_options[j], cost_diff))
                    elif meal_options[i]["meal_type"] == "Lunch" and meal_options[j]["meal_type"] == "Lunch":
                        lunch_options.append((meal_options[i], meal_options[j], cost_diff))
                    elif meal_options[i]["meal_type"] == "Dinner" and meal_options[j]["meal_type"] == "Dinner":
                        dinner_options.append((meal_options[i], meal_options[j], cost_diff))

        weekly_plan = {}
        for day in days:
            breakfast_meal = random.choice(breakfast_options)
            lunch_meal = random.choice(lunch_options)
            dinner_meal = random.choice(dinner_options)
            weekly_plan[day] = {"Breakfast": breakfast_meal, "Lunch": lunch_meal, "Dinner": dinner_meal}

        self.result_text.delete("1.0", tk.END)
        for day, meals in weekly_plan.items():
            self.result_text.insert(tk.END, day + ":\n")
            self.result_text.insert(tk.END, "- Breakfast: {} ({} calories, ${})\n".format(meals["Breakfast"][0]["name"],
                                                                                          meals["Breakfast"][0][
                                                                                              "calories"],
                                                                                          meals["Breakfast"][0]["cost"]))
            self.result_text.insert(tk.END, "              {} ({} calories, ${})\n".format(meals["Breakfast"][1]["name"],
                                                                                            meals["Breakfast"][1][
                                                                                                "calories"],
                                                                                            meals["Breakfast"][1][
                                                                                                "cost"]))
            self.result_text.insert(tk.END, "- Lunch: {} ({} calories, ${})\n".format(meals["Lunch"][0]["name"],
                                                                                        meals["Lunch"][0]["calories"],
                                                                                        meals["Lunch"][0]["cost"]))
            self.result_text.insert(tk.END, "          {} ({} calories, ${})\n".format(meals["Lunch"][1]["name"],
                                                                                        meals["Lunch"][1]["calories"],
                                                                                        meals["Lunch"][1]["cost"]))
            self.result_text.insert(tk.END, "- Dinner: {} ({} calories, ${})\n".format(meals["Dinner"][0]["name"],
                                                                                         meals["Dinner"][0][
                                                                                             "calories"],
                                                                                         meals["Dinner"][0]["cost"]))
            self.result_text.insert(tk.END, "           {} ({} calories, ${})\n".format(meals["Dinner"][1]["name"],
                                                                                         meals["Dinner"][1][
                                                                                             "calories"],
                                                                                         meals["Dinner"][1]["cost"]))
            self.result_text.insert(tk.END, "\n")

    def get_background_image(self):
        image = Image.open(r"/Users/damsara/Downloads/Meal planner/jason-briscoe-GliaHAJ3_5A-unsplash.png")
        image = image.resize((self.winfo_screenwidth(), self.winfo_screenheight()))
        background_image = ImageTk.PhotoImage(image)
        return background_image

    def start_resizing(self):
        self.bind("<Configure>", self.resize_background_image)

    def resize_background_image(self, event):
        resized_image = self.get_background_image().resize((event.width, event.height))
        self.background_image = ImageTk.PhotoImage(resized_image)
        self.background_label.configure(image=self.background_image)

# Define the meal options with calorie, cost, and meal type values
meal_options = [
    {"name": "Chicken Breast", "calories": 165, "cost": 2, "meal_type": "Breakfast"},
    {"name": "Oatmeal", "calories": 150, "cost": 1, "meal_type": "Breakfast"},
    {"name": "Eggs", "calories": 78, "cost": 2, "meal_type": "Breakfast"},
    {"name": "Yogurt", "calories": 120, "cost": 1.5, "meal_type": "Breakfast"},
    {"name": "Salad", "calories": 200, "cost": 4, "meal_type": "Lunch"},
    {"name": "Grilled Chicken", "calories": 250, "cost": 6, "meal_type": "Lunch"},
    {"name": "Salmon", "calories": 350, "cost": 8, "meal_type": "Lunch"},
    {"name": "Steak", "calories": 400, "cost": 10, "meal_type": "Lunch"},
    {"name": "Fish", "calories": 300, "cost": 7, "meal_type": "Dinner"},
    {"name": "Tofu", "calories": 200, "cost": 5, "meal_type": "Dinner"},
    {"name": "Shrimp", "calories": 250, "cost": 7, "meal_type": "Dinner"},
    {"name": "Pasta", "calories": 300, "cost": 6, "meal_type": "Dinner"},
    {"name": "Fruit Salad", "calories": 120, "cost": 3, "meal_type": "Breakfast"},
    {"name": "Avocado Toast", "calories": 200, "cost": 4, "meal_type": "Breakfast"},
    {"name": "Smoothie Bowl", "calories": 250, "cost": 5, "meal_type": "Breakfast"},
    {"name": "Waffles", "calories": 300, "cost": 3.5, "meal_type": "Breakfast"},
    {"name": "Quinoa Salad", "calories": 220, "cost": 5, "meal_type": "Lunch"},
    {"name": "Veggie Wrap", "calories": 280, "cost": 4.5, "meal_type": "Lunch"},
    {"name": "Stir-Fry", "calories": 320, "cost": 7, "meal_type": "Lunch"},
    {"name": "Burger", "calories": 400, "cost": 8, "meal_type": "Lunch"},
    {"name": "Sushi", "calories": 350, "cost": 12, "meal_type": "Dinner"},
    {"name": "Burrito", "calories": 450, "cost": 9, "meal_type": "Dinner"},
    {"name": "Pizza", "calories": 400, "cost": 10, "meal_type": "Dinner"},
    {"name": "Lasagna", "calories": 380, "cost": 8.5, "meal_type": "Dinner"},
    {"name": "Pancakes", "calories": 250, "cost": 3.5, "meal_type": "Breakfast"},
    {"name": "Granola", "calories": 180, "cost": 2.5, "meal_type": "Breakfast"},
    {"name": "Egg Sandwich", "calories": 300, "cost": 4.5, "meal_type": "Breakfast"},
    {"name": "Frittata", "calories": 280, "cost": 4, "meal_type": "Breakfast"},
    {"name": "Caesar Salad", "calories": 220, "cost": 4.5, "meal_type": "Lunch"},
    {"name": "Wrap", "calories": 240, "cost": 3.5, "meal_type": "Lunch"},
    {"name": "Bowl", "calories": 280, "cost": 5, "meal_type": "Lunch"},
    {"name": "Sandwich", "calories": 320, "cost": 6, "meal_type": "Lunch"},
    {"name": "Sushi Roll", "calories": 280, "cost": 10, "meal_type": "Dinner"},
    {"name": "Taco", "calories": 320, "cost": 6.5, "meal_type": "Dinner"},
    {"name": "Pasta Salad", "calories": 250, "cost": 5.5, "meal_type": "Dinner"},
    {"name": "Baked Chicken", "calories": 300, "cost": 7.5, "meal_type": "Dinner"}
]


# Define the days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if __name__ == "__main__":
    app = MealPlannerApp()
    app.start_resizing()
    app.mainloop()
