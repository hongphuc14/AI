#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from fact import Fact
class Substitution:
    def __init__(self):
        self.bindings = dict()

    def __repr__(self):
        return ', '.join('{} = {}'.format(var, value) for var, value in self.bindings.items())

    def __eq__(self, other):
        return self.bindings == other.bindings

    def __hash__(self):
        return hash(frozenset(self.bindings.items()))

    def bind(self, var, value):
        self.bindings[var] = value
        
    def empty(self):
        return len(self.bindings) == 0

    def contains(self, var):
        return var in self.bindings

    def get_substitute(self, var):
        return self.bindings[var]

    def apply_substitution(self, fact):
        for idx, arg in enumerate(fact.args):
            if self.contains(arg):
                fact.args[idx] = self.get_substitute(arg)

def is_variable(x):
    return isinstance(x, str) and x[0].isupper()

# Checks if an object is a compound logical expression
def is_compound(x):
    return isinstance(x, Fact)

def is_list(x):
    return isinstance(x, list)
