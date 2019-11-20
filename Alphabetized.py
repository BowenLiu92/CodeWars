#!/usr/bin/env python
# coding: utf-8

# In[1]:


def alphabetized(s):
    ins = [letter for letter in s if letter.isalpha()]
    return (''.join(sorted(ins, key=str.casefold))).strip(' ')

