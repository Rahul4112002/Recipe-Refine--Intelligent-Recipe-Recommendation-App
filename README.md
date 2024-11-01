# Recipe Refine 🍲

Recipe Refine is an intelligent recipe recommendation app designed to provide personalized meal suggestions based on nutritional preferences and ingredient input. By using machine learning techniques, Recipe Refine refines your search to match recipes with your dietary requirements, helping you easily discover delicious and tailored meal options.

# Demo Video 
https://github.com/user-attachments/assets/8f4196f2-796a-4873-9ec8-28ab36749989


# Features🚀

    Personalized Recipe Suggestions: Get meal recommendations based on calorie, fat, carbohydrates, protein, cholesterol, sodium, fiber, and ingredient input.
    
    Intelligent Ingredient Matching: Uses NLP techniques to match recipes with ingredients you have on hand.
    
    Intuitive User Interface: Easy-to-use form for inputting dietary preferences and nutritional goals.
    
    Responsive Design: Works seamlessly across desktop and mobile devices.

# Getting Started🛠️

Follow these steps to set up and run Recipe Refine on your local machine.
Prerequisites

    Python 3.8 or higher
    Django 5.1.2
    Required packages in requirements.txt

# Installation
    Clone the Repository:
   
    git clone https://github.com/Rahul4112002/Recipe-Refine--Intelligent-Recipe-Recommendation-App.git
    
    cd Recipe-Refine

# Create and Activate a Virtual Environment:

    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`

# Install Dependencies:

    pip install -r requirements.txt

# Run the Server:

    python manage.py runserver

    Access the App: Open your web browser and go to http://127.0.0.1:8000.

#  Usage Guide📋

    Enter Nutritional Preferences: Fill in your desired values for calories, fat, carbohydrates, protein, cholesterol, sodium, and fiber.

    Add Ingredients: List the ingredients you have, separated by commas.

    Click "Get Recipes": Receive up to 5 recipe suggestions tailored to your preferences!

# Project Structure🔧

    Recipe-Refine/
    ├── recommendation/
    │   ├── Notebook/
    │   │   └── recipe_final.csv  # Recipe dataset
    │   ├── migrations/
    │   ├── templates/
    │   │   └── index.html
    │   ├── views.py
    │   └── models.py
    ├── manage.py
    ├── README.md
    └── requirements.txt

# Technology Stack🧠

    Backend: Django, Scikit-Learn, Pandas, Numpy
    Frontend: HTML5, CSS3, JavaScript
    Machine Learning: K-Nearest Neighbors (KNN) for similarity-based recipe recommendation
    NLP: TF-IDF vectorization for ingredient processing

# Future Improvements✨

    User Authentication for saving favorite recipes.
    Enhanced Recommendation Algorithm using a hybrid model for even better personalization.
    Meal Plan Generator to suggest a weekly meal plan based on user preferences.

# Contributing🤝

    Fork the repository.
    Create a new branch with a descriptive name.
    Make your changes and test thoroughly.
    Submit a pull request for review.

# License📜

This project is licensed under the @rahul4112 License.
