from search import title_to_info, keyword_to_titles, search, article_info, article_length, title_timestamp, favorite_author, multiple_keywords, display_result
from search_tests_helper import print_basic, print_advanced, print_advanced_option, get_print
from wiki import article_metadata, title_to_info_map, keyword_to_titles_map
from unittest.mock import patch
from copy import deepcopy

# List of all available article titles for this search engine
# The benefit of using this is faster code - these functions will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
METADATA = article_metadata()
TITLE_TO_INFO = title_to_info_map()
KEYWORD_TO_TITLES = keyword_to_titles_map()

# Storing into a variable so don't need to copy and paste long list every time
DOG = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']

TRAVEL = ['Time travel']

MUSIC = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']

PROGRAMMING = ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)']

SOCCER = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']

PHOTO = ['Digital photography']

SCHOOL = ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)']

PLACE = ['2009 in music', 'List of dystopian music, TV programs, and games', '2006 in music', '2007 in music', '2008 in music']

DANCE = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music']

def test_example_title_to_info_tests():
    ''' Tests for title_to_info(), function #1. '''
    # Example tests, these do not count as your tests
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'an article title': {'author': 'andrea', 'timestamp': 1234567890, 'length': 103}, 
                'another article title': {'author': 'helloworld', 'timestamp': 987123456, 'length': 8029}}
    assert title_to_info(deepcopy(fake_metadata)) == expected

def test_example_keyword_to_titles_tests():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES
    

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of keyword_to_titles with fake_metadata
    expected = {'some': ['an article title'], 'words': ['an article title', 'another article title'], 'that': ['an article title'], 'make': ['an article title', 'another article title'], 'up': ['an article title'], 'sentence': ['an article title'], 'more': ['another article title'], 'could': ['another article title'], 'sentences': ['another article title']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected

def test_example_unit_tests():
    # Example tests, these do not count as your tests

    # Basic search, function #3
    assert search('dog') == DOG

    # Advanced search option 1, function #4
    expected = {'Black dog (ghost)': {'author': 'SmackBot', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'AnomieBOT', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'J. Spencer', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Sarranduin', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Hellbus', 'timestamp': 1208969289, 'length': 18050}}
    assert article_info(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Mexican dog-faced bat', 'Guide dog']
    assert article_length(8000, deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Black dog (ghost)': 1220471117, 'Mexican dog-faced bat': 1255316429, 'Dalmatian (dog)': 1207793294, 'Guide dog': 1165601603, 'Sun dog': 1208969289}
    assert title_timestamp(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('J. Spencer', deepcopy(DOG), TITLE_TO_INFO) == True
    assert favorite_author('Andrea', deepcopy(DOG), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
    assert multiple_keywords('soccer', deepcopy(DOG)) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 2
    advanced_response = 8000

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat', 'Guide dog']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.
def test_example_title_to_info_tests1():
    ''' Tests for title_to_info(), function #1. '''
    # Example tests, these do not count as your tests
    assert title_to_info(METADATA) == TITLE_TO_INFO
    
     # Create fake metadata to test
    fake_metadata = [['arun', 'ram', 123, 144, ['Tiger', 'is', 'a', 'animal']], ['diwakar', 'pravakar', 0, 8, ['cat', 'is', 'also', 'an', 'animal']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'arun': {'author': 'ram', 'timestamp': 123, 'length': 144}, 'diwakar': {'author': 'pravakar', 'timestamp': 0, 'length': 8}}
    assert title_to_info(deepcopy(fake_metadata)) == expected
    
     # Create fake metadata to test
    fake_metadata = [['albin', 'rosna', 999, 333, ['i', 'is', 'a', 'pray']], ['alina', 'sonu', 000, 888, ['let', 'is', 'understand', 'an', 'festival']]]
    expected = {'albin': {'author': 'rosna', 'timestamp': 999, 'length': 333}, 'alina': {'author': 'sonu', 'timestamp': 000, 'length': 888}}
    assert title_to_info(deepcopy(fake_metadata)) == expected
    
     # Create fake metadata to test
    fake_metadata = [['darsan', 'asis', 5, 25, ['tiger', 'is', 'a', 'danger']], ['prayas', 'solta', 36, 49, ['let', 'us', 'enjoy', 'this', 'moment']]]
    
    expected = {'darsan': {'author': 'asis', 'timestamp': 5, 'length':25}, 'prayas': {'author': 'solta', 'timestamp': 36, 'length': 49}}
    assert title_to_info(deepcopy(fake_metadata)) == expected
    
def test_example_keyword_to_titles_tests2():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
   

    # Create fake metadata to test
    fake_metadata = [['an article title', 'arun', 222, 333, ['i', 'love', 'computer', 'science', 'a', 'lot']], ['another article title', 'giri', 444, 555, ['ram', 'loves', 'computer', 'science', 'really']]]
    
    # Expected value of keyword_to_titles with fake_metadata
    expected = {'i': ['an article title'], 'love': ['an article title'], 'computer': ['an article title', 'another article title'], 'science': ['an article title', 'another article title'], 'a': ['an article title'], 'lot': ['an article title'], 'ram': ['another article title'], 'loves': ['another article title'], 'really': ['another article title']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected
    
    fake_metadata = [['an article title', 'arun', 5, 25, ['learning', 'is', 'a', 'gradually', 'improving', 'process']], ['another article title', 'giri', 16, 49, ['arun', 'is', 'a', 'improving', 'person']]]
        
    # Expected value of keyword_to_titles with fake_metadata
    expected = {'learning': ['an article title'], 'is': ['an article title', 'another article title'], 'a': ['an article title', 'another article title'], 'gradually': ['an article title'], 'improving': ['an article title', 'another article title'], 'process': ['an article title'], 'arun': ['another article title'], 'person': ['another article title']}
    assert keyword_to_titles(deepcopy(fake_metadata)) == expected
    
    fake_metadata = [['an article title', 'arun', 5, 25, ['cow', 'is', 'a', 'national', 'animal', 'nepal']], ['another article title', 'giri', 16, 49, ['we', 'should', 'learn', 'to', 'work']]]
    
     # Expected value of keyword_to_titles with fake_metadata
    expected = {'cow': ['an article title'], 'is': ['an article title'], 'a': ['an article title'], 'national': ['an article title'], 'animal': ['an article title'], 'nepal': ['an article title'], 'we': ['another article title'], 'should': ['another article title'], 'learn': ['another article title'], 'to': ['another article title'], 'work': ['another article title']}
    assert keyword_to_titles(deepcopy(fake_metadata)) == expected
    
def test_example_unit_tests1():
    

    # Basic search, function #3
    assert search('photo') == PHOTO
    assert search('travel') == TRAVEL
    assert search('programming') == PROGRAMMING
    
    
    # Advanced search option 1, function #4
    expected = {'Digital photography': {'author': 'Mintleaf', 'timestamp': 1095727840, 'length': 18093}}
    assert article_info(deepcopy(PHOTO), TITLE_TO_INFO) == expected
    
    expected = {'Time travel': {'author': 'Thug outlaw69', 'timestamp': 1140826049, 'length': 35170}}
    assert article_info(deepcopy(TRAVEL), TITLE_TO_INFO) == expected
    
    expected = {'C Sharp (programming language)': {'author': 'Eaglizard', 'timestamp': 1232492672, 'length': 52364}, 'Python (programming language)': {'author': 'Lulu of the Lotus-Eaters', 'timestamp': 1137530195, 'length': 41571}, 'Lua (programming language)': {'author': 'Makkuro', 'timestamp': 1113957128, 'length': 0}, 'Covariance and contravariance (computer science)': {'author': 'Wakapop', 'timestamp': 1167547364, 'length': 7453}, 'Personal computer': {'author': 'Darklock', 'timestamp': 1220391790, 'length': 45663}, 'Ruby (programming language)': {'author': 'Hervegirod', 'timestamp': 1193928035, 'length': 30284}}
    assert article_info(deepcopy(PROGRAMMING), TITLE_TO_INFO) == expected
    
    
    
    
    # Advanced search option 2, function #5
    expected = ['Mexican dog-faced bat']
    assert article_length(1200, deepcopy(DOG), TITLE_TO_INFO) == expected
    
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Guide dog']
    assert article_length(15000, deepcopy(DOG), TITLE_TO_INFO) == expected
    
    
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Guide dog', 'Sun dog']
    assert article_length(20000, deepcopy(DOG), TITLE_TO_INFO) == expected
    
    
     # Advanced search option 3, function #6
    expected = {'Time travel': 1140826049}
    assert title_timestamp(deepcopy(TRAVEL), TITLE_TO_INFO) == expected
    
    expected = {'Digital photography': 1095727840}
    assert title_timestamp(deepcopy(PHOTO), TITLE_TO_INFO) == expected
    
    expected = {'C Sharp (programming language)': 1232492672, 'Python (programming language)': 1137530195, 'Lua (programming language)': 1113957128, 'Covariance and contravariance (computer science)': 1167547364, 'Personal computer': 1220391790, 'Ruby (programming language)': 1193928035}
    assert title_timestamp(deepcopy(PROGRAMMING), TITLE_TO_INFO) == expected
    
    
    
    
    
     # Advanced search option 4, function #7
    assert favorite_author('J. Spencer', deepcopy(DOG), TITLE_TO_INFO) == True
    assert favorite_author('arun', deepcopy(DOG), TITLE_TO_INFO) == False
    assert favorite_author('giri', deepcopy(DOG), TITLE_TO_INFO) == False
    assert favorite_author('SmackBot', deepcopy(DOG), TITLE_TO_INFO) == True
    
    # Advanced search option 5, function #8
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Digital photography']
    assert multiple_keywords('photo', deepcopy(DOG)) == expected
    
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Time travel']
    assert multiple_keywords('travel', deepcopy(DOG)) == expected
    
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)']
    assert multiple_keywords('programming', deepcopy(DOG)) == expected
    

    
@patch('builtins.input')
def test_example_integration_test1(input_mock):
    keyword = 'programming'
    advanced_option = 5
    advanced_response = 'soccer'

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    
    
    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected
    
    
@patch('builtins.input')
def test_example_integration_test2(input_mock):
    keyword = 'dog'
    advanced_option = 2
    advanced_response = 1200

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    
    
    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected
    
# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To make all tests run, call all test functions inside the if statement.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    # As you're done with each function, uncomment the example test functions
    # and make sure they pass
     test_example_title_to_info_tests()
     test_example_keyword_to_titles_tests()
     test_example_unit_tests()
     test_example_integration_test()
     test_example_title_to_info_tests1()
     test_example_keyword_to_titles_tests2()
     test_example_unit_tests1()
     test_example_integration_test1()
     test_example_integration_test2()
