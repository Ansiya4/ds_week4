# Define a simple classification function
def simple_decision_tree_classifier(features):
    # Define a simple decision rule
    if features[0] < 5.0 and features[1] < 3.0:
        return 0  # Classify as Class 0
    else:
        return 1  # Classify as Class 1

# Sample dataset (features)
data = [
    [4.8, 2.5],
    [5.2, 3.0],
    [3.5, 1.5],
    [6.0, 3.5],
    [5.5, 2.5]
]

# Classify each data point
predictions = [simple_decision_tree_classifier(features) for features in data]

# Print the predictions
for i, prediction in enumerate(predictions):
    print(f"Data point {i+1}: Class {prediction}")
