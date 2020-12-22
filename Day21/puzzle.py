from itertools import chain
import networkx as nx

def read_ingredients(input):
    ingredients = []
    allergies = []
    for line in input:
        ingredient, allergy = line.strip().split(' (contains ')
        allergies.append(allergy[:-1].split(', '))
        ingredients.append(ingredient.split())
    return ingredients, allergies

def find_possible_ingredient_for_allergy(ingredients, allergies):
    all_allergies = set(chain(*allergies))
    all_ingredients = set(chain(*ingredients)) 
    possible_ingredients = {allergy: all_ingredients for allergy in all_allergies}
    for allergy in all_allergies:
        for i, ing in enumerate(ingredients):
            if allergy in allergies[i]:
                possible_ingredients[allergy] = possible_ingredients[allergy].intersection(ing)
    return possible_ingredients
    
def count_non_allergy_ingredients(ingredient_lists, possible_ingredients):
    all_possible_ingredients = set(chain(*possible_ingredients.values()))
    count = 0
    for ingredients in ingredient_lists:
        for ingredient in ingredients:
            if not ingredient in all_possible_ingredients:
                count += 1
    return count
         
def match_ingredients_to_allergies(allergies, possible_ingredients):
    all_allergies = set(chain(*allergies))
    possible_ings = set(chain(*possible_ingredients.values()))
    bg = nx.Graph()
    bg.add_nodes_from(all_allergies, bipartite=0)
    bg.add_nodes_from(possible_ings, bipartite=1)
    bg.add_edges_from((al, ing) for al in all_allergies for ing in possible_ingredients[al])
    match = nx.bipartite.maximum_matching(bg)
    return {al: match[al] for al in all_allergies}

def canonical_list(match):
    sorted_ings = [match[al] for al in sorted(match.keys())]
    return ''.join(ing+',' for ing in sorted_ings[:-1])+sorted_ings[-1]

file_names = ['small_input', 'large_input']
folder_name = './Day21/'
for file_name in file_names:
    with open(folder_name+file_name) as input_file:
        input = input_file.readlines()
        ingredients, allergies = read_ingredients(input)
        possible_ingredients = find_possible_ingredient_for_allergy(ingredients, allergies)
        puzzle1 = count_non_allergy_ingredients(ingredients, possible_ingredients)
        print(F'Puzzle 1 - {file_name}: ', puzzle1)
        match = match_ingredients_to_allergies(allergies, possible_ingredients)
        puzzle2 = canonical_list(match)
        print(F'Puzzle 2 - {file_name}: ', puzzle2)
