import random


class LearnerWrapper:
    """
    Need to implement methods of aa model.
    Load saved model and wraps the model methods because of different ML model like xgboost, logistic regression
    and etc.
    """
    def __init__(self, algo_path):
        self.learner = None

    def predict_proba(self, vector):
        return random.uniform(0, 1)


class Learner:
    def __init__(self, algo_path):
        self.learner = LearnerWrapper(algo_path)

    def predict_proba(self, vector):
        return self.learner.predict_proba(vector)
