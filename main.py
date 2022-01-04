# Name:   <Gurpreet Singh>
# Student Number: <20313393>
# Email:  <21gsgs@queensu.ca>

# I confirm that this assignment solution is my own work and conforms to
# Queen's standards of Academic Integrity


import tkinter as tk
import glob
from tkinter.filedialog import askdirectory

window = tk.Tk()  # create a window that can be displayed
window.title("Assignment3")  # give it a title
window.geometry("600x800")  # width x height in pixels


def letter_only(w):
    """
    Parameter: A string.
    Returns: A filtered string with only characters in it.
    Description: This function remove any non character from the string w.
    For instance if the input is "hell2o", then it would return "Hello".
    """
    new_word = ''
    for c in w:
        if c.isalpha():
            new_word += c
    return new_word


stop_words_set = set()  # A set to store stop words

stop_words_file = open('StopWords.txt', 'r')

for line in stop_words_file:
    """This for loop open the stopWord file, filter all the words in it
    and then put them in the stop_words_set set.
    """

    # putting every word of the line in a list.
    line_words_list = line.split()
    for stop_word in line_words_list:
        stop_word = letter_only(stop_word)  # filtering the word
        stop_words_set.add(stop_word)  # adding the word in the set

""" Asking the user for the directory of where all the files are stored
and also setting a default directory just in case user does not choose
any directory.
"""
data_directory = askdirectory(initialdir="./books")
if data_directory == "":
    data_directory = "./books"

# Storing all the files name in the text_file_name_list list.
text_file_name_list = glob.glob(data_directory + "/" + "*.txt")

"""A Dictionaries to store all word counts of all the files.
Files name is the key and other dictionary which contain the word
and their respective count is the value in this dictionary.
"""
wordcount_name_dict = {}

for files_names in text_file_name_list:
    """
    This for loop iterate through all the elements of the
    text_file_name_list and open the file for reading in the variable
    named "r".
    """
    wordcount_dict = {}
    file = open(files_names, 'r')

    for line in file:
        """
        This for loop access all the lines in the file  and split them
        in a list of with each words as an element of type string.
        """
        line_word_list = line.split()
        for words in line_word_list:
            """ This For loop access all the words from the list,
            convert them into filtered lower case words.
            """
            words = words.lower()
            words = letter_only(words)
            if words not in stop_words_set and words != "":
                """
                This For loop put the words in the dictionary
                word_count_dict if they are not in the stopWords file
                or if the words are not just some empty space.
                """
                if words not in wordcount_dict:  # if not in list, add them
                    wordcount_dict[words] = 1
                else:  # If in list, increment their count.
                    wordcount_dict[words] += 1

    # Deleting values from the dictionary if there frequency < 5 times.
    # List(type(Dictionary)), create a copy of the dictionary
    for number in list(wordcount_dict):
        if wordcount_dict[number] < 5:
            del wordcount_dict[number]
    # Renaming the file name from absolute path to just file name.
    files_names = (files_names.split("/"))[-1]
    files_names = (files_names.split("."))[0]

    """Adding the wordcount_dict dictionary, as a value to the
    wordcount_name_dict dictionary where the key is the name of that
    particular file.
    """
    wordcount_name_dict[files_names] = wordcount_dict

set_A = set()
# Iterating in the bigger wordcount_name_dict dictionary
for iter_var in wordcount_name_dict:
    """Iterating through the inner Dictionary to extract just the words
    which represent the file and then put them in the set_A set.
    """
    for iter_var2 in wordcount_name_dict[iter_var]:
        set_A.add(iter_var2)

    """Now changing the value of the Key in the wordcount_name_dict
    to a set, which contain the words that represent the Key(File).
    """
    wordcount_name_dict[iter_var] = set_A.copy()
    set_A.clear()  # Clearing the set after storing it in the dictionary

"""To store book name as key and list of matching files as value.
"""
jaccard_dict = {}
jaccard_list = []  # To store the matching files

for var in wordcount_name_dict:
    """This for loop will compare each files with other files.
    Variable "var" taking the dictionary key as its value, which
    is the name of the files.
    """
    maximum = 0  # To store the maximum Jaccard Ratio.
    # var2 taking the file's name as it value
    for var2 in wordcount_name_dict:
        """
        Variable "var2" taking the dictionary key as its value, which
        is the name of the files.
        """
        # if statement to ensure that same files are not being compared.
        if var != var2:
            intersection = wordcount_name_dict[var].intersection \
                (wordcount_name_dict[var2])
            union = wordcount_name_dict[var].union(wordcount_name_dict[var2])
            jaccard_ratio = len(intersection) / len(union)

            if jaccard_ratio > maximum:
                """Storing the name of the file in the list with the
                highest ratio"""
                maximum = jaccard_ratio
                jaccard_list.clear()
                jaccard_list.append(var2)
                jaccard_dict[var] = jaccard_list.copy()
            elif jaccard_ratio == maximum:
                """If two files have the same ratio, then store both.
                """
                jaccard_dict[var].append(var2)

"""
Using Tkinter to display the output in the GUI rather than the
compiler.
"""
col_0_head = tk.Label(window, text="Book Name", pady=20,
                      font='Helvetica 20 underline')
col_0_head.grid(row=0, column=0)
col_1_head = tk.Label(window, text="Best Match", font='Helvetica 20 underline')
col_1_head.grid(row=0, column=1)

row = len(jaccard_dict)
for i in jaccard_dict:
    x = tk.Label(window, text=i)
    x.grid(row=row, column=0)

    y = tk.Label(window, text=jaccard_dict[i])
    y.grid(row=row, column=1)
    row += 1

window.mainloop()
