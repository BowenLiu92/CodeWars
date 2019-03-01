
# coding: utf-8

# In[1]:


def dative(word):
    vowel_list = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű', 'a', 'á', 'o', 'ó', 'u', 'ú']
    fword = [i for i in word if i in vowel_list]
    if fword[-1] in vowel_list[0:9]:
        return word+'nek'
    return word+'nak'

