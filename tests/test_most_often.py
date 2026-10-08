from lib.most_often import *
import pytest
'''
expected behaviours
'''
'''
test to make sure it initialises an empty list
'''
def test_empty_list_initialised():
    most_often = MostOften()
    assert most_often.starting_list == []

'''
add new method adds a new item to list
'''
def test_add_new_method():
    most_often = MostOften()
    most_often.add_new("Overwatch")
    assert most_often.starting_list == ["Overwatch"]

'''
get most often gets the most often item and returns 
winner if there is a clear winner
'''
def test_returns_winner():
    most_often = MostOften()
    most_often.add_new("Overwatch")
    most_often.add_new("Overwatch")
    most_often.add_new("Overwatch")
    most_often.add_new("Overwatch")
    assert most_often.get_most_often() == "Overwatch"

'''
in get most often - returns no clear winner if there is no clear winner
'''
def test_return_no_winner():
    most_often = MostOften()
    most_often.add_new("Overwatch")
    most_often.add_new("Minecraft")
    most_often.add_new("Days Gone")
    assert most_often.get_most_often() == "no clear winner"

'''
errors
'''

'''
add new - if no new items you get an error
add new - if there is no string get an error
'''

'''
if no empty list is initialised get an error
'''
