from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text


iris = load_iris()
X = iris.data
y = iris.target


clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)


tree_rules = export_text(clf, feature_names=iris.feature_names)
print("Decision Tree Rules:\n", tree_rules)


tree_structure = clf.tree_


used_features = [iris.feature_names[i] for i in tree_structure.feature]

print("\nFeatures used in the tree:", used_features)
