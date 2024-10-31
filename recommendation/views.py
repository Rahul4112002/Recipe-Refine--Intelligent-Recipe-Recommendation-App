from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
import os


# Load the dataset (make sure this path is correct)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = pd.read_csv(os.path.join(BASE_DIR, 'recommendation', 'Notebook', 'recipe_final (1).csv'))


# Preprocess Ingredients
vectorizer = TfidfVectorizer()
X_ingredients = vectorizer.fit_transform(data['ingredients_list'])

# Normalize Numerical Features
scaler = StandardScaler()
X_numerical = scaler.fit_transform(data[['calories', 'fat', 'carbohydrates', 'protein', 'cholesterol', 'sodium', 'fiber']])

# Combine Features
X_combined = np.hstack([X_numerical, X_ingredients.toarray()])

# Train KNN Model
knn = NearestNeighbors(n_neighbors=3, metric='euclidean')
knn.fit(X_combined)

# Recommendation Function
def recommend_recipes(input_features):
    input_features_scaled = scaler.transform([input_features[:7]])
    input_ingredients_transformed = vectorizer.transform([input_features[7]])
    input_combined = np.hstack([input_features_scaled, input_ingredients_transformed.toarray()])
    distances, indices = knn.kneighbors(input_combined)
    recommendations = data.iloc[indices[0]]
    return recommendations[['recipe_name', 'ingredients_list', 'image_url']].head(5)

# Function to truncate product name
def truncate(text, length):
    return text[:length] + "..." if len(text) > length else text

def home(request):
    recommendations = []
    form_data = {}  # Dictionary to store form data

    if request.method == 'POST':
        try:
            # Extract form data and store it in form_data
            form_data = {
                'calories': request.POST.get('calories', ''),
                'fat': request.POST.get('fat', ''),
                'carbohydrates': request.POST.get('carbohydrates', ''),
                'protein': request.POST.get('protein', ''),
                'cholesterol': request.POST.get('cholesterol', ''),
                'sodium': request.POST.get('sodium', ''),
                'fiber': request.POST.get('fiber', ''),
                'ingredients': request.POST.get('ingredients', ''),
            }

            # Convert to appropriate types for recommendation function
            input_features = [
                float(form_data['calories']),
                float(form_data['fat']),
                float(form_data['carbohydrates']),
                float(form_data['protein']),
                float(form_data['cholesterol']),
                float(form_data['sodium']),
                float(form_data['fiber']),
                form_data['ingredients']
            ]

            # Generate recommendations
            recommendations = recommend_recipes(input_features).to_dict(orient='records')
        except ValueError:
            recommendations = []

    # Return form_data to the template
    return render(request, 'index.html', {
        'recommendations': recommendations,
        'truncate': truncate,
        'form_data': form_data
    })
