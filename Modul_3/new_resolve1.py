calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    my_tuple = (len(string), string.upper(), string.lower())
    count_calls()
    return my_tuple


def is_contains(string, list_to_search):
    perem = False
    for i in list_to_search:
        if string.lower() in i.lower():
            perem = True
            break
    count_calls()
    return perem


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(is_contains('cycle', ['cyclical ', 'encyclic']))
print(calls)
