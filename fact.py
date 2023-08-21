#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Lớp "Fact" đại diện cho một vị từ logic với các thuộc tính khác nhau như phép toán, đối số và phủ định. 
class Fact:
    def __init__(self, op='', args=[], negated=False):
        self.op = op              
        self.args = args           
        self.negated = negated

    def __repr__(self):
        return '{}({})'.format(self.op, ', '.join(self.args))

    def __lt__(self, rhs):
        if self.op != rhs.op:
            return self.op < rhs.op
        if self.negated != rhs.negated:
            return self.negated < rhs.negated
        return self.args < rhs.args

    def __eq__(self, rhs):
        if self.op != rhs.op:
            return False
        if self.negated != rhs.negated:
            return False
        return self.args == rhs.args

    def __hash__(self):
        return hash(str(self))
   
    def copy(self):
        return Fact(self.op, self.args.copy(), self.negated)

    def negate(self):
        self.negated = not self.negated

    def get_args(self):
        return self.args

    def get_op(self):
        return self.op

    @staticmethod
    def parse_fact(fact):
        if '\\=' in fact:
            parts = fact.split('\\=')
            op = parts[0]
            args = [arg.strip() for arg in parts[1].split(',')]
        else:
            op_start = 0
            op_end = fact.index('(')
            op = fact[op_start:op_end]
            args_start = op_end + 1
            args_end = fact.index(')')
            args = fact[args_start:args_end].split(',')
        return Fact(op, args)

