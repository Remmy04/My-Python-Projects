# Initial facts
facts = {
    'John_taller_Kim',
    'John_is_boy',
    'Kim_is_girl',
    'John_and_Kim_same_class',
    'Everyone_else_shorter_than_Kim_except_John',
    'Tom_in_same_class',
    'Tom_is_boy'
}

# Ordered list to track the order of inference
ordered_facts = list(facts)

# Rule base using forward chaining
def forward_chaining(facts, ordered_facts):
    # Rule 1: Infer Tom is shorter than Kim
    if 'Tom_in_same_class' in facts and 'Everyone_else_shorter_than_Kim_except_John' in facts:
        if 'Tom_shorter_Kim' not in facts:
            print("Inferred: Tom is shorter than Kim")
            facts.add('Tom_shorter_Kim')
            ordered_facts.append('Tom_shorter_Kim')
    
    # Rule 2: If John is taller than Kim, and Tom is shorter than Kim → John is tallest
    if 'John_taller_Kim' in facts and 'Tom_shorter_Kim' in facts:
        if 'John_is_tallest' not in facts:
            print("Inferred: John is the tallest in class")
            facts.add('John_is_tallest')
            ordered_facts.append('John_is_tallest')
    
    # Rule 3: If Kim is between John and Tom → Kim is taller than Tom
    if 'John_taller_Kim' in facts and 'Tom_shorter_Kim' in facts:
        if 'Kim_taller_Tom' not in facts:
            print("Inferred: Kim is taller than Tom")
            facts.add('Kim_taller_Tom')
            ordered_facts.append('Kim_taller_Tom')
    return ordered_facts

# Run inference
final_order = forward_chaining(facts, ordered_facts)

# Output : 
# Inferred: Tom is shorter than Kim
# Inferred: John is the tallest in class
# Inferred: Kim is taller than Tom 