# ------------------------------
# Knowledge base
# ------------------------------
# This dictionary represents a simple ontology.
# Each entity (animal or category) may contain:
# - 'is_a': defines its parent category
# - 'has': properties or physical traits
# - 'lives_in': habitat information

knowledge = {
    'Bat': {'is_a': 'Mammal', 'has': ['Wings'], 'lives_in': ['Caves']},
    'Cat': {'is_a': 'Mammal', 'lives_in': ['House']},
    'Dog': {'is_a': 'Mammal', 'lives_in': ['House']},
    'Penguin': {'is_a': 'Bird', 'has': ['Flippers'], 'lives_in': ['Antarctica']},
    'Parrot': {'is_a': 'Bird', 'has': ['Can Talk'], 'lives_in': ['Rainforest']},
    'Whale': {'is_a': 'Mammal', 'has': ['Blubber', 'Flippers'], 'lives_in': ['Ocean']},
    'Bird': {'is_a': 'Animal', 'has': ['Feathers', 'Beak']},
    'Mammal': {'is_a': 'Animal', 'has': ['Fur', 'Warm Blood']},
    'Animal': {'has': ['Heart', 'Legs']}
}

# ------------------------------
# Function: get_properties
# ------------------------------
# This function collects all inherited 'has' properties for an entity.
# It follows the 'is_a' chain upward until there are no more parents.

def get_properties(entity):
    props = []  # Create an empty list to store all properties
    while entity in knowledge:
        if 'has' in knowledge[entity]:  # If entity has 'has' properties, add them
            props += knowledge[entity]['has']
        if 'is_a' in knowledge[entity]:  # Move up the inheritance chain
            entity = knowledge[entity]['is_a']
        else:  # Stop if there is no parent
            break
    return props # Example: ['Wings', 'Fur', 'Warm Blood', 'Feathers', 'Beak', 'Heart', 'Legs']

# ------------------------------
# Function: get_habitats
# ------------------------------
# This function works similarly to get_properties,
# but it collects all 'lives_in' habitat info from the entity and its ancestors.

def get_habitats(entity):
    habitats = []  # Empty list for habitats
    while entity in knowledge:
        if 'lives_in' in knowledge[entity]:  # Add habitats if available
            habitats += knowledge[entity]['lives_in']
        if 'is_a' in knowledge[entity]:  # Move to parent entity
            entity = knowledge[entity]['is_a']
        else:  # End loop if no parent
            break
    return habitats

# ------------------------------
# Function: get_inheritance_chain
# ------------------------------
# This function builds a chain of (child, parent) pairs
# to explain the inheritance path of the given entity.

def get_inheritance_chain(entity):
    chain = []  # List to store inheritance chain
    while entity in knowledge and 'is_a' in knowledge[entity]:
        parent = knowledge[entity]['is_a']  # Example: 'Mammal' = knowledge['Whale']['is_a'], so the parent of whale is 'Mammal'
        chain.append((entity, parent))      # Add (child, parent) to the chain list, Example: ('Whale', 'Mammal')
        entity = parent                     # The previous parent becomes entity, 'entity' becomes 'Mammal' , then go back to the loop  
    return chain                            # Loop ends when there are no more parents

# Second Loop:
# entity = 'Mammal'
# knowledge['Mammal']['is_a'] → 'Animal'
# Append ('Mammal', 'Animal') to the chain.
# Now entity = 'Animal', which has no is_a, so the loop stops.
# The chain is now [('Whale', 'Mammal'), ('Mammal', 'Animal')].

# ------------------------------
# Main Program Loop
# ------------------------------
# This loop runs continuously, allowing the user to query different animals.

while True:
    entity = input("Enter an animal : ")  # Ask user for input

    if entity in knowledge:
        # Retrieve and display inheritance relationships
        chain = get_inheritance_chain(entity) # The chain is now [('Whale', 'Mammal'), ('Mammal', 'Animal')].
        for child, parent in chain:
            print(f"\n{child} is a {parent}.")

        # Retrieve and display properties
        result = get_properties(entity)
        print(f"\n{entity} has: {', '.join(result)}")

        # Retrieve and display habitats
        habitats = get_habitats(entity)
        print(f"\n{entity} lives in: {', '.join(habitats)}")
        print()

    else:
        print("Not found in knowledge base.")


# Output:
# Enter an animal : Whale
# Whale is a Mammal.
# Mammal is a Animal.
# Whale has: Blubber, Flippers, Fur, Warm Blood, Heart, Legs
# Whale lives in: Ocean 