from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create a decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

# View the decision tree rules
tree_rules = export_text(clf, feature_names=iris.feature_names)
print("Decision Tree Rules:\n", tree_rules)

# Access the decision tree structure
# Decision trees in scikit-learn have a `tree_` attribute containing the underlying Tree data structure
# It can be accessed to explore the tree structure
tree_structure = clf.tree_

# Accessing features used in the tree
used_features = [iris.feature_names[i] for i in tree_structure.feature]

print("\nFeatures used in the tree:", used_features)
