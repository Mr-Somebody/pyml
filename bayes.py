#!/usr/bin/python
#-*- coding: utf-8 -*-
#Author: liujian
#Date: 2015/09/06 17:13:13
#Dec: 


class BayesModel:
    """
    """
    def __init__(self):
        """
        """
        self.prior_y = None
        self.prior_x = None

    def predict(self, x):
        """
        """
        result = (0, None)
        for y in self.prior_y:
            val = 1.0
            for v in x:
                val *= self.prior_x[y].get(v, 1.0)
            if val > result[0]:
                result = (val, y)
        return result
        pass


def fit(X, Y):
    """create a bayes model
    Args:
    X: feature list
    Y: label list

    Returns:
    Bayes model
    """
    model = BayesModel()
    model.prior_y = {}
    model.prior_x = {}
    if not X or not Y or len(X) != len(Y):
        return model
    for y in Y:
        if y not in model.prior_y:
            model.prior_y[y] = 1.0
            model.prior_x[y] = {}
        else:
            model.prior_y[y] += 1
    for i in xrange(len(Y)):
        x = X[i]
        y = Y[i]
        for v in x:
            if v not in model.prior_x[y]:
                model.prior_x[y][v] = 1
            else:
                model.prior_x[y][v] += 1
    for y in model.prior_y:
        for v in model.prior_x[y]:
            model.prior_x[y][v] /= model.prior_y[y]
        model.prior_y[y] /= len(Y)
    return model


X = [
    [1, -1],
    [2, -2],
    [1, -2]
]
Y = [0, 1, 0]
model = fit(X, Y)
print model.prior_y
print model.prior_x
print model.predict([2, -1])
