
# coding: utf-8

# In[8]:


def maxSequence(arr):
    if arr:
        max_c = max_g = arr[0]
        for i in range(1, len(arr)):
            max_c = max(max_c + arr[i], arr[i])
            max_g = max(max_c, max_g)
            print(i)
        if max_g < 0: return 0
        else:
            return max_g
    else:
        return 0

