import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Creating the dataset
ingredients = ['Chicken', 'Lentils', 'Yogurt', 'Cumin', 'Tomatoes', 'Garlic', 'Onions', 'Butter', 'Cheese', 'Pasta', 'Bread', 'Beef', 'Lettuce', 'Wine', 'Herbs']
person1_indian =   [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
person2_indian =   [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
person3_american = [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
person4_american = [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
person5_french =   [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1]

# Combine all persons into a single dataset
data = np.array([person1_indian, person2_indian, person3_american, person4_american, person5_french])

# Compute cosine similarity
cosine_sim = cosine_similarity(data)

# Display the cosine similarity matrix
cosine_sim



######
import random

indian_fridge_ingredients = ['Chicken','Lentils (Dal)','Yogurt','Cumin','Tomatoes','Garlic','Onions','Ginger','Cilantro (Coriander leaves)','Green chilies','Turmeric','Mustard seeds','Garam masala','Curry leaves','Paneer (Indian cottage cheese)','Ghee (Clarified butter)','Fresh mint','Fenugreek leaves (Kasuri methi)','Spinach','Eggplant (Brinjal)','Okra (Bhindi)','Potatoes','Cauliflower','Green peas','Bell peppers','Carrots','Fresh coconut','Tamarind paste','Rice','Whole wheat flour (Atta)','Chickpeas (Chana)','Black beans (Rajma)','Butter','Milk','Eggs','Mangoes','Lemons','Lime','Jaggery','Cardamom','Cloves','Cinnamon sticks','Bay leaves','Fennel seeds','Red chili powder','Coriander powder','Black mustard oil','Asafoetida (Hing)','Pickles (Achar)','Pomegranate']
american_fridge_ingredients = ['Milk','Eggs','Butter','Cheddar cheese','Mozzarella cheese','Yogurt','Chicken breast','Ground beef','Bacon','Ham','Sausage','Turkey','Lettuce','Spinach','Carrots','Broccoli','Bell peppers','Tomatoes','Cucumbers','Zucchini','Mushrooms','Onions','Garlic','Potatoes','Sweet potatoes','Corn','Peas','Green beans','Apples','Bananas','Grapes','Oranges','Strawberries','Blueberries','Bread','Tortillas','Pasta','Rice','Ketchup','Mustard','Mayonnaise','Ranch dressing','Barbecue sauce','Soy sauce','Hot sauce','Butter','Cream cheese','Orange juice','Apple juice','Jam']
french_fridge_ingredients = ['Butter','Cream','Milk','Eggs','Cheese (Camembert)','Cheese (Brie)','Cheese (Roquefort)','Cheese (Gruyère)','Cheese (Comté)','Cheese (Goat cheese)','Yogurt','Chicken','Duck','Ham','Sausage','Pâté','Smoked salmon','Fresh herbs (Thyme)','Fresh herbs (Rosemary)','Fresh herbs (Tarragon)','Fresh herbs (Parsley)','Garlic','Onions','Shallots','Leeks','Carrots','Celery','Potatoes','Tomatoes','Zucchini','Eggplant','Bell peppers','Green beans','Lettuce','Spinach','Mushrooms','Baguette','Croissants','Wine (Red)','Wine (White)','Champagne','Olive oil','Balsamic vinegar','Dijon mustard','Crème fraîche','Anchovies','Capers','Cornichons','Puff pastry','Pears','Apples']
english_fridge_ingredients = ['Milk','Eggs','Butter','Cheddar cheese','Double cream','Yogurt','Chicken','Bacon','Sausages','Ham','Beef','Lamb','Pork','Potatoes','Carrots','Peas','Green beans','Cabbage','Brussels sprouts','Leeks','Onions','Garlic','Mushrooms','Tomatoes','Lettuce','Cucumber','Bell peppers','Broccoli','Cauliflower','Spinach','Bread','Butter','Marmalade','Jam','English mustard','Mayonnaise','Ketchup','Brown sauce (HP Sauce)','Worcestershire sauce','Pickles','Chutney','Apple juice','Orange juice','Beer','Ale','Wine','Cheddar cheese','Clotted cream','Strawberries','Raspberries']
german_fridge_ingredients = ['Milk','Butter','Cheese (Emmental)','Cheese (Gouda)','Quark','Yogurt','Sausages (Bratwurst)','Sausages (Weißwurst)','Ham','Bacon','Pork','Beef','Chicken','Sauerbraten','Potatoes','Sauerkraut','Red cabbage','Carrots','Onions','Garlic','Leeks','Cabbage','Spinach','Green beans','Peas','Asparagus (white)','Bread (Rye)','Pretzels','Mustard','Mayonnaise','Ketchup','Pickles','Horseradish','Apple juice','Orange juice','Beer','Wine (Riesling)','Butter','Cream','Fresh herbs (Dill)','Fresh herbs (Parsley)','Fresh herbs (Chives)','Eggs','Sour cream','Cream cheese','Radishes','Tomatoes','Cucumbers','Mushrooms','Apples']
russian_fridge_ingredients = ['Milk','Butter','Smetana (Sour cream)','Kefir','Ryazhenka','Cottage cheese (Tvorog)','Cheese (Russian)','Sausages','Ham','Beef','Pork','Chicken','Fish (Herring)','Fish (Salmon)','Potatoes','Cabbage','Beets','Carrots','Onions','Garlic','Dill','Parsley','Chives','Radishes','Cucumbers','Tomatoes','Pickles','Mushrooms','Saurkraut','Bread (Rye)','Black bread','Buckwheat (Kasha)','Rice','Pasta','Eggs','Apples','Berries (Cranberries)','Berries (Lingonberries)','Honey','Jam','Horseradish','Mustard','Mayonnaise','Ketchup','Sunflower oil','Vinegar','Vodka','Kvass','Fruit juice','Tea (Black)']
malaysian_fridge_ingredients = ['Chicken','Beef','Pork','Fish','Shrimp','Squid','Coconut milk','Tofu','Tempeh','Eggs','Milk','Butter','Yogurt','Lemongrass','Galangal','Turmeric','Ginger','Garlic','Onions','Shallots','Chili paste','Dried chilies','Curry leaves','Kaffir lime leaves','Pandan leaves','Coriander leaves','Mint leaves','Cilantro','Bean sprouts','Long beans','Okra','Eggplant','Tomatoes','Cucumbers','Bell peppers','Carrots','Cabbage','Kangkung (Water spinach)','Bitter melon','Potatoes','Sweet potatoes','Rice','Rice noodles','Coconut','Palm sugar','Soy sauce','Fish sauce','Oyster sauce','Shrimp paste (Belacan)','Tamarind paste']
mexican_fridge_ingredients = ['Chicken','Beef','Pork','Chorizo','Fish','Shrimp','Eggs','Milk','Cheese (Queso fresco)','Cheese (Queso Oaxaca)','Cheese (Cotija)','Butter','Crema (Mexican sour cream)','Limes','Cilantro','Jalapeños','Serrano peppers','Poblano peppers','Habanero peppers','Tomatoes','Tomatillos','Avocados','Onions','Garlic','Bell peppers','Cucumbers','Carrots','Radishes','Zucchini','Corn','Black beans','Pinto beans','Lettuce','Cabbage','Spinach','Chayote','Nopales (Cactus)','Tortillas','Tortilla chips','Salsa','Guacamole','Hot sauce','Adobo sauce','Chipotle peppers in adobo','Pickled jalapeños','Mole sauce','Mexican chocolate','Tequila','Beer']
korean_fridge_ingredients = ['Kimchi','Soy sauce','Gochujang (Korean red chili paste)','Doenjang (Fermented soybean paste)','Gochugaru (Korean red chili flakes)','Sesame oil','Sesame seeds','Garlic','Ginger','Green onions (Scallions)','Onions','Korean radish (Mu)','Napa cabbage','Spinach','Carrots','Zucchini','Cucumber','Bean sprouts','Bell peppers','Potatoes','Sweet potatoes','Tofu','Fish sauce','Oyster sauce','Rice vinegar','Mirin','Rice cakes (Tteok)','Rice','Rice noodles','Glass noodles (Dangmyeon)','Seaweed (Gim/Nori)','Dried anchovies','Beef','Pork','Chicken','Eggs','Milk','Cheese','Butter','Mushrooms (Enoki)','Mushrooms (Shiitake)','Korean pears','Apples','Asian pears','Persimmons','Chili peppers','Perilla leaves','Ssamjang (Korean dipping sauce)','Kimchi base (Mak kimchi)']


# Create a list of all ingredients to maintain a common feature space
all_ingredients = list(set(indian_fridge_ingredients + american_fridge_ingredients + french_fridge_ingredients +
                      english_fridge_ingredients + german_fridge_ingredients + russian_fridge_ingredients +
                      malaysian_fridge_ingredients + mexican_fridge_ingredients + korean_fridge_ingredients))



# Function to sample 20 ingredients from a list without replacement, 5 times
def sample_fridge(ingredients, n_samples=5, sample_size=20):
    sampled_fridges = [random.sample(ingredients, sample_size) for _ in range(n_samples)]
    return sampled_fridges

# Sample from each fridge 5 times without replacement
sampled_indian_fridges = sample_fridge(indian_fridge_ingredients)
sampled_american_fridges = sample_fridge(american_fridge_ingredients)
sampled_french_fridges = sample_fridge(french_fridge_ingredients)
sampled_english_fridges = sample_fridge(english_fridge_ingredients)
sampled_german_fridges = sample_fridge(german_fridge_ingredients)
sampled_russian_fridges = sample_fridge(russian_fridge_ingredients)
sampled_malaysian_fridges = sample_fridge(malaysian_fridge_ingredients)
sampled_mexican_fridges = sample_fridge(mexican_fridge_ingredients)
sampled_korean_fridges = sample_fridge(korean_fridge_ingredients)

# Sample fridges
sampled_fridges = {
    'Indian': sampled_indian_fridges,
    'American': sampled_american_fridges,
    'French': sampled_french_fridges,
    'English': sampled_english_fridges,
    'German': sampled_german_fridges,
    'Russian': sampled_russian_fridges,
    'Malaysian': sampled_malaysian_fridges,
    'Mexican': sampled_mexican_fridges,
    'Korean': sampled_korean_fridges
}


def create_binary_vector(sample, ingredients_list):
    return [1 if ingredient in sample else 0 for ingredient in ingredients_list]

# Calculate the average cosine similarity between each country's sample fridges and each other country
average_similarities = {}

for country1, samples1 in sampled_fridges.items():
    average_similarities[country1] = {}
    for country2, samples2 in sampled_fridges.items():
        if country1 == country2:
            continue
        similarities = []
        for sample1 in samples1:
            for sample2 in samples2:
                vec1 = create_binary_vector(sample1, all_ingredients)
                vec2 = create_binary_vector(sample2, all_ingredients)
                sim = cosine_similarity([vec1], [vec2])[0][0]
                similarities.append(sim)
        average_similarities[country1][country2] = np.mean(similarities)

# Print the average similarities
print("Average Cosine Similarities Between Countries' Sampled Fridges:")
for country1, similarities in average_similarities.items():
    for country2, similarity in similarities.items():
        print(f"{country1} vs {country2}: {similarity:.4f}")





import torch
import torch.nn as nn
import torch.optim as optim

# Assuming the previous code has created binary vectors for each refrigerator sample
def create_binary_vector(sample, ingredients_list):
    return [1 if ingredient in sample else 0 for ingredient in ingredients_list]

# Create a list of all ingredients to maintain a common feature space
all_ingredients = list(set(indian_fridge_ingredients + american_fridge_ingredients + french_fridge_ingredients +
                      english_fridge_ingredients + german_fridge_ingredients + russian_fridge_ingredients +
                      malaysian_fridge_ingredients + mexican_fridge_ingredients + korean_fridge_ingredients))

# Convert all samples to binary vectors
def samples_to_vectors(samples, all_ingredients):
    return np.array([create_binary_vector(sample, all_ingredients) for sample in samples])

sample_vectors = {
    'Indian': samples_to_vectors(sampled_indian_fridges, all_ingredients),
    'American': samples_to_vectors(sampled_american_fridges, all_ingredients),
    'French': samples_to_vectors(sampled_french_fridges, all_ingredients),
    'English': samples_to_vectors(sampled_english_fridges, all_ingredients),
    'German': samples_to_vectors(sampled_german_fridges, all_ingredients),
    'Russian': samples_to_vectors(sampled_russian_fridges, all_ingredients),
    'Malaysian': samples_to_vectors(sampled_malaysian_fridges, all_ingredients),
    'Mexican': samples_to_vectors(sampled_mexican_fridges, all_ingredients),
    'Korean': samples_to_vectors(sampled_korean_fridges, all_ingredients)
}

# Combine all samples into one dataset
all_samples = np.vstack(list(sample_vectors.values()))
all_samples_tensor = torch.tensor(all_samples, dtype=torch.float32)

# Define the autoencoder model
class Autoencoder(nn.Module):
    def __init__(self, input_dim, encoding_dim):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, encoding_dim),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Linear(encoding_dim, input_dim),
            nn.Sigmoid()
        )
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return encoded, decoded

input_dim = len(all_ingredients)
encoding_dim = 100  # 10-dimensional space

model = Autoencoder(input_dim, encoding_dim)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the autoencoder
num_epochs = 50
batch_size = 10
num_batches = len(all_samples_tensor) // batch_size

for epoch in range(num_epochs):
    for i in range(num_batches):
        batch = all_samples_tensor[i * batch_size: (i + 1) * batch_size]
        optimizer.zero_grad()
        encoded, decoded = model(batch)
        loss = criterion(decoded, batch)
        loss.backward()
        optimizer.step()
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Get the 10-dimensional embeddings
embeddings = {}
for country, vectors in sample_vectors.items():
    vectors_tensor = torch.tensor(vectors, dtype=torch.float32)
    with torch.no_grad():
        encoded, _ = model(vectors_tensor)
    embeddings[country] = encoded.numpy()

# Example: Print the 10-dimensional embeddings for Indian samples
print("10-dimensional embeddings for Indian samples:")
print(embeddings['Indian'])

cosine_similarity([embeddings['Malaysian'][1],embeddings['Korean'][0]])
