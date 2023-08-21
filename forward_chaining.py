#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import itertools
from fact import Fact
from unify import unify
from util import Substitution

# Generalized Modus Ponens
def substitution(facts_1, facts_2):          
    if len(facts_1) != len(facts_2):
        return False

    for f1, f2 in zip(facts_1, facts_2):
        if f1.get_op() != f2.get_op():
            return False

    return unify(facts_1, facts_2, Substitution())

def forward_chaining(kb, alpha):
    results = set()
    
    # Precheck if current facts are enough to answer, potentially optimize the reasoning process by 
    # avoiding unnecessary forward chaining when the answer is already available in the existing facts.
    for fact in kb.facts:
        unification = unify(fact, alpha, Substitution())
        if unification:
            if unification.empty():
                results.add('true')
                return results
            results.add(unification)
            
    last_generated_facts = kb.facts.copy()

    while True:
        new_facts = set()
        # Checking Rule Trigger
        for rule in kb.rules:
            if not rule.may_trigger(last_generated_facts):
                continue
            
            num_premises = rule.get_premise_count()
            potential_facts = kb.get_potential_facts(rule)
            # Generating Premises Combinations
            if not rule.duplicate_predicate:        
                potential_premises = itertools.combinations(sorted(potential_facts), num_premises)
            else:
                potential_premises = itertools.permutations(potential_facts, num_premises)
            # Checking Substitutions and Applying Rule
            for premise_tuple in potential_premises:
                premises = list(premise_tuple)
                theta = substitution(rule.premises, premises)
                if not theta:
                    continue
                # Creating a New Fact and Substituting            
                new_fact = rule.conclusion.copy()
                theta.apply_substitution(new_fact)
                # Checking and Adding New Fact
                if new_fact not in new_facts and new_fact not in kb.facts:
                    new_facts.add(new_fact)
                    unification = unify(new_fact, alpha, Substitution())
                    if unification:
                        if unification.empty():
                            kb.facts.update(new_facts)
                            results.add('true')
                            return results
                        # Adding Substitution to Results
                        results.add(unification)

        last_generated_facts = new_facts
        if not new_facts:
            if not results:
                results.add('false')
            return results
        kb.facts.update(new_facts)

