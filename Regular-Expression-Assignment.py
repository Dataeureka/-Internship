#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re


# In[7]:


# Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
sub = 'Python Exercises, PHP exercises.'
y = re.sub("[\s,\.]", ":", sub)
print(y)


# In[11]:


# Question 2
import pandas as pd
import re

# Create the dictionary
data = {'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']}

# Create the DataFrame
df = pd.DataFrame(data)

# Function to clean the text
def clean_text(text):
    # Remove specific words like 'YYYYY'
    text = re.sub(r'\bXXXXX\b', '', text)
    # Remove everything except words and spaces
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Apply the clean_text function to the 'SUMMARY' column
df['SUMMARY'] = df['SUMMARY'].apply(clean_text)

print(df)


# In[ ]:


# Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.
import re

def find_long_words(input_string):
    # Compile the regular expression pattern
    pattern = re.compile(r'\b\w{4,}\b')
    # Find all words that are at least 4 characters long
    long_words = pattern.findall(input_string)
    return long_words

# Example usage
input_string = "This is  the day that the lord has made and we will rejoice and be glad in it."
print(find_long_words(input_string))


# In[27]:


Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

import re

def find_three_to_five_char_words(input_string):
    # Compile the regular expression pattern
    pattern = re.compile(r'\b\w{3,5}\b')
    # Find all words that are three, four, or five characters long
    words = pattern.findall(input_string)
    return words

# Example usage
input_string = "This is  the day that the lord has made and we will rejoice and be glad in it."
print(find_three_to_five_char_words(input_string))


# In[28]:


# Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
import re

def remove_parentheses(lst):
    # Compile the regular expression pattern
    pattern = re.compile(r'\s*\([^)]*\)\s*')
    
    # Function to clean a single string
    def clean_string(s):
        return pattern.sub('', s).strip()
    
    # Apply the clean_string function to each element in the list
    return [clean_string(item) for item in lst]

# Sample text
sample_text = [" example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

# Remove parentheses
cleaned_list = remove_parentheses(sample_text)
print(cleaned_list)


# In[37]:


#Question 7- Write a regular expression in Python to split a string into uppercase letters

# Sample text
string = "ImportanceOfRegularExpressionsInPython"

# Split the string using the pattern
result = re.split(r'(?=[A-Z])', string)

# Print the result
print(result)


# In[39]:


# Question 8- Create a function in python to insert spaces between words starting with numbers. 
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

import re

# Sample text
sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

# Insert spaces between words starting with numbers using re.sub
output = re.sub(r'(?<=\D)(?=\d)', ' ', sample_text)

# Print the output
print(output)


