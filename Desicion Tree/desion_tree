import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        # indeks cechy, wedlug ktorej nastepuje podzial danych
        self.feature = feature
        # prog podzialu dla danej cechy
        self.threshold = threshold
        # lewy wezel potomny (poddrzewo)
        self.left = left
        # prawy wezel potomny (poddrzewo)
        self.right = right
        # wartosc w wezle, jesli jest to lisc (dla lisci, gdy wezel nie ma potomkow)
        self.value = value

    def is_leaf_node(self):
        # funkcja sprawdza, czy wezel jest lisciem (nie ma potomkow)
        return self.value is not None

class DecisionTree:
    def __init__(self, max_depth=10):
        # maksymalna glebokosc drzewa
        self.max_depth = max_depth
        # korzen drzewa
        self.root = None

    def fit(self, X, y):
        # rozpoczynamy budowe drzewa od korzenia
        self.root = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        # liczba probek i cech w danych
        num_samples, num_features = X.shape
        # jesli osiagnieto maksymalna glebokosc lub wszystkie etykiety sa takie same, zwracamy lisc
        if depth == self.max_depth or len(np.unique(y)) == 1:
            common = Counter(y).most_common(1)[0][0]
            return Node(value=common)

        # wybor najlepszej cechy i progu dla podzialu
        best_feat, best_thresh = self._best_criteria(X, y, num_features)
        left_idxs, right_idxs = self._split(X[:, best_feat], best_thresh)
        left = self._grow_tree(X[left_idxs], y[left_idxs], depth+1)
        right = self._grow_tree(X[right_idxs], y[right_idxs], depth+1)
        return Node(best_feat, best_thresh, left, right)

    def _best_criteria(self, X, y, num_features):
        # inicjalizacja najlepszego przyrostu informacji i indeksow
        best_gain = -1
        split_idx, split_thresh = None, None
        for feature_idx in range(num_features):
            # unikalne progi dla danej cechy
            thresholds = np.unique(X[:, feature_idx])
            for threshold in thresholds:
                gain = self._information_gain(y, X[:, feature_idx], threshold)
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feature_idx
                    split_thresh = threshold
        return split_idx, split_thresh

    def _information_gain(self, y, X_column, split_thresh):
        # obliczenie entropii rodzica
        parent_entropy = self._entropy(y)
        left_idxs, right_idxs = self._split(X_column, split_thresh)
        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0
        n = len(y)
        n_left, n_right = len(left_idxs), len(right_idxs)
        e_left, e_right = self._entropy(y[left_idxs]), self._entropy(y[right_idxs])
        child_entropy = (n_left / n) * e_left + (n_right / n) * e_right
        ig = parent_entropy - child_entropy
        return ig

    def _entropy(self, y):
        # obliczenie entropii dla zestawu etykiet
        hist = np.bincount(y)
        ps = hist / np.sum(hist)
        return -np.sum([p * np.log2(p) for p in ps if p > 0])

    def _split(self, feature, thresh):
        # podzial danych na podstawie progu
        left_idxs = np.argwhere(feature <= thresh).flatten()
        right_idxs = np.argwhere(feature > thresh).flatten()
        return left_idxs, right_idxs

    def predict(self, X):
        # predykcja dla kazdej probki w zbiorze danych
        return np.array([self._predict(inputs, self.root) for inputs in X])

    def _predict(self, inputs, node):
        # przechodzenie drzewa do momentu znalezienia liscia
        if node.is_leaf_node():
            return node.value
        if inputs[node.feature] <= node.threshold:
            return self._predict(inputs, node.left)
        else:
            return self._predict(inputs, node.right)
