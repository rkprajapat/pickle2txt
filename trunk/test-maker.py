#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

"""Generates sample pickle files from classes defined here."""

import cPickle as pickle

class BasicTypes:

    def __init__(self):
        self.a_str = "Hello, World!"
        self.a_float = 6.55321
        self.a_bool = False
        self.a_list = [-1, 2.5, "alpha"]
        self.a_tuple = (0, 1.2, "three")
        self.a_dict = {"A Key":"A Value", "Second":2}


if __name__ == "__main__":

    objects_n_names = (
            (BasicTypes().dict(), "basic.pkl")
            )

    for obj, path in objects_n_names:
        output = open(path, 'wb')
        pickle.dump(obj, output)
        output.close()

