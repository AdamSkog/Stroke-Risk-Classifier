from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder


class MultiColumnLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, columns=None):
        self.columns = columns  # List of column names to encode

    def fit(self, X, y=None):
        return self  # No need to fit, as LabelEncoder is stateless

    def transform(self, X):
        X_copy = X.copy()
        if self.columns is not None:
            for column in self.columns:
                le = LabelEncoder()
                X_copy[column] = le.fit_transform(X_copy[column])
        return X_copy
