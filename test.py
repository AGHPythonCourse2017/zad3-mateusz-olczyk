from main import count_letters, how_many_words_can_be_built

count_letters_test = count_letters('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
assert count_letters_test['l'] == 3
assert count_letters_test['o'] == 4
assert count_letters_test['r'] == 3
assert count_letters_test['e'] == 5
assert count_letters_test['m'] == 3
assert count_letters_test['i'] == 6
assert count_letters_test['p'] == 2
assert count_letters_test['s'] == 4
assert count_letters_test['u'] == 2
assert count_letters_test['d'] == 2
assert count_letters_test['t'] == 5
assert count_letters_test['a'] == 2
assert count_letters_test['c'] == 3
assert count_letters_test['n'] == 2
assert count_letters_test['g'] == 1

assert 4 == how_many_words_can_be_built('whatever', 'whateverwhateveradbawhateverdefghwhatever')
assert 4 == how_many_words_can_be_built('whatever', 'whateverwhateveradbawhateverdefghwhatver')
assert 3 == how_many_words_can_be_built('whatever', 'whateverwhateveradbawhateverdefghwhateer')
