"""
Rule:

    i before e, except after c

    this rule breaks down to:
        usually ie
        usually cei
        never cie
        no information about ei

    The datum we are after is whether 'cie' is common.
    With the data below, we need to use (ie - cie) for
    the prevalence of ie without c.

"""
import pickle
import re

matches = ['cei', 'cie', 'ei', 'ie']
counts = [0,0,0,0]

with open('ngsl.pickle') as f:
    ngsl = pickle.load(f)

print("Total words in ngsl: {}".format(len(ngsl),))

expressions = [re.compile(x, re.IGNORECASE) for x in matches]

for expression_index, expression in enumerate(expressions):
    for word in ngsl:
        if expression.search(word):
            counts[expression_index] += 1

print(zip(matches, counts))

print("(ie - cie) yields: {}".format((counts[3]-counts[1])))
