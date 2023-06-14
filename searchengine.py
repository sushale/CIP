"""
File: searchengine.py
---------------------
You fill in this comment
"""


import os
import sys
import string


def create_index(filenames, index, file_titles):
    for file in filenames:
        with open(file) as f:
            first_line=f.readline().rstrip("\n") # first line title processing 
            clean_line=first_line
            file_titles[file]=clean_line
            
            for line in [first_line] + f.readlines():
                clean_string=line.split()
                for term in clean_string:
                    term=term.strip(string.punctuation) # normalize each term
                    if term !='':
                        term=term.lower()
                        if term in index:
                            if file not in index[term]:
                                index[term].append(file) #add to index dict
                        else:
                            index[term]=[file]

def search(index, query):
    words = query.split()
    results = []

    # create list with file names from the first search term
    if words[0] in index:
        results = list(index[words[0]])

    # Iterate over the remaining terms
    for word in words[1:]:
        if word not in index:
            return []  # Return an empty list if any word is not in the index

        # Keep only the file names that exist in the current search term results
        results = [file for file in results if file in index[word]]

    return results
        
def common_many(*lists):
    pass

    common_list=[]
    
    for element in lists[0]:
        is_common=True
        for lst in lists[1:]:
            if element not in lst:
                is_common=False
                break
        if is_common and element not in common_list:
            common_list.append(element)
    
    return common_list
    
      



##### YOU SHOULD NOT NEED TO MODIFY ANY CODE BELOW THIS LINE (UNLESS YOU'RE ADDING EXTENSIONS) #####


def do_searches(index, file_titles):
    """
    This function is given an inverted index and a dictionary mapping from
    file names to the titles of articles in those files.  It allows the user
    to run searches against the data in that index.
    """
    while True:
        query = input("Query (empty query to stop): ")
        query = query.lower()                   # convert query to lowercase
        if query == '':
            break
        results = search(index, query)

        # display query results
        print("Results for query '" + query + "':")
        if results:                             # check for non-empty results list
            for i in range(len(results)):
                title = file_titles[results[i]]
                print(str(i + 1) + ".  Title: " + title + ",  File: " + results[i])
        else:
            print("No results match that query.")


def textfiles_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a valid directory, returns a list of the .txt
    file names within it.

    Input:
        directory (string): name of directory
    Returns:
        list of (string) names of .txt files in directory
    """
    filenames = []

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filenames.append(os.path.join(directory, filename))

    return filenames


def main():
    """
    Usage: searchengine.py <file directory> -s
    The first argument specified should be the directory of text files that
    will be indexed/searched.  If the parameter -s is provided, then the
    user can interactively search (using the index).  Otherwise (if -s is
    not included), the index and the dictionary mapping file names to article
    titles are just printed on the console.
    """
    # Get command line arguments
    args = sys.argv[1:]

    num_args = len(args)
    if num_args < 1 or num_args > 2:
        print('Please specify directory of files to index as first argument.')
        print('Add -s to also search (otherwise, index and file titles will just be printed).')
    else:
        # args[0] should be the folder containing all the files to index/search.
        directory = args[0]
        if os.path.exists(directory):
            # Build index from files in the given directory
            files = textfiles_in_dir(directory)
            index = {}          # index is empty to start
            file_titles = {}    # mapping of file names to article titles is empty to start
            create_index(files, index, file_titles)

            # Either allow the user to search using the index, or just print the index
            if num_args == 2 and args[1] == '-s':
                do_searches(index, file_titles)
            else:
                print('Index:')
                print(index)
                print('File names -> document titles:')
                print(file_titles)
        else:
            print('Directory "' + directory + '" does not exist.')


if __name__ == '__main__':
    main()
