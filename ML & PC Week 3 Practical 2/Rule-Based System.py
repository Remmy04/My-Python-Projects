# Initial set of known facts
facts = {'sunny', 'weekend'}

# List to preserve the order in which facts are added/inferred
ordered_facts = ['sunny', 'weekend']

# Rule base: Each rule says "if condition is true, then result is also true"
rules = {
    'sunny': 'go_outside',
    'weekend': 'have_free_time',
    'have_free_time': 'go_outside',
    'go_outside': 'wear_sunglasses',
    'wear_sunglasses': 'look_cool',
    'look_cool': 'take_selfie',
    'take_selfie': 'post_on_instagram'
}

# Function to perform forward chaining inference
def forward_chaining(facts, rules, ordered_facts):
    # Loop until no new facts can be inferred
    while True:
        found_new_facts = False  # Flag to track whether we found new inferences in this round

        # Go through all rules
        for condition, result in rules.items():
            # If the condition is known and result is not already a fact
            if condition in facts and result not in facts:
                print(f"Inferred: {result}")  # Print the new fact for learning/debugging
                facts.add(result)            # Add new fact to the known facts set
                ordered_facts.append(result) # Keep track of order of inference
                found_new_facts = True       # Mark that we found something new this round

        # If we didn’t infer anything new, we can stop
        if not found_new_facts:
            break

    return ordered_facts  # Return the list of all facts in order they were inferred

# --- Execution starts here ---
print("Initial fact:", facts)
print()
# Run the inference engine
final_order = forward_chaining(facts, rules, ordered_facts)

# Print all facts in the order they were inferred
print("\nFacts in logical order of inference:")
for fact in final_order:
    print("-", fact)

# Facts (set): Unordered collection of known truths (starting knowledge).
# Rules (dictionary): Conditional logic saying if one fact is true, then another becomes true.
# Forward Chaining: Starts from facts, applies rules, and keeps inferring new facts until no more rules apply.
# Ordered Facts (list): Used to track the order in which facts are added, which sets do not do.

# Output:
# Initial fact: {'sunny', 'weekend'}
# Inferred: go_outside
# Inferred: have_free_time
# Inferred: wear_sunglasses
# Inferred: look_cool
# Inferred: take_selfie
# Inferred: post_on_instagram
#
# Facts in logical order of inference:
# - sunny
# - weekend
# - go_outside
# - have_free_time
# - wear_sunglasses
# - look_cool
# - take_selfie
# - post_on_instagram