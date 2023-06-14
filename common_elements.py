"""
File: common_elements.py
------------------------
File to implement a function that is passed two lists and returns a new list
containing those elements that appear in both of the lists passed in.
"""


def common(list1, list2):

    common_list=[]
    
    for element1 in list1:
        for element2 in list2:
            if element1 == element2 and element1 not in common_list:
                common_list.append(element1)
    
    return common_list


def main():
    # Same tests as the doctests above, but can be run from the terminal:
    # python3 common_elements.py
   
    
    print(common(['a'], ['a']))                             # should print ['a']
    print(common(['a', 'b', 'c'], ['x', 'a', 'z', 'c']))    # should print ['a', 'c']
    print(common(['a', 'b', 'c'], ['x', 'y', 'z']))         # should print []
    print(common(['a', 'a', 'b'], ['a', 'a', 'x']))         # should print ['a']
    print(common(['a', 'a', 'b','b','f'], ['a', 'a', 'x'])) #should print ['a']
    


if __name__ == '__main__':
    main()
