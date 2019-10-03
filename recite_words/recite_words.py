# This is file help me reciting words, you can input help to see
# all commands and their meaning. I know there are some way to
# optimize the code, but now it's enough for me. By the way, who
# need to reciting thousands words?

# author:   carl
# email:    bearcarl@qq.com
# version:  1.0
# time:     2019.10.2


import datetime
import platform
import os
import pickle
import random
from prettytable import PrettyTable as pt


today_g = datetime.date.today().strftime('%y%m%d')
words_table = dict()
date_info = dict()

last_cmd = ''       # save the last command
cls_switch = 'off'  # auto clear screen switch


# base functions

def check_date_info():
    ''''check if today in date_info or not'''

    if today_g not in date_info:
        date_info[today_g] = {
            'recite_counts':    0,
            'add_counts':       0,
            'del_counts':       0,
            'mod_counts':       0
        }
    else:
        return


def recite_counts():
    '''record reciting a word in someday(date)'''

    check_date_info()
    date_info[today_g]['recite_counts'] += 1


def add_counts():
    '''record adding a word into words table in someday(date)'''

    check_date_info()
    date_info[today_g]['add_counts'] += 1


def del_counts():
    '''record deleting a word from words table in someday(date)'''

    check_date_info()
    date_info[today_g]['del_counts'] += 1


def mod_counts():
    '''record modify a word in words table in someday(date)'''

    check_date_info()
    date_info[today_g]['mod_counts'] += 1


def print_words(table):
    '''print words table using pretty table'''

    x = pt(['word', 'translation'])
    for line in table:
        x.add_row(line)
    print(x)


def print_info():
    '''print date_info table'''

    new_info = list(date_info.keys())
    new_info.sort()
    x = pt(['Date', 'Recite words', 'Add words', 'Del words', 'Mod words'])
    for key in new_info:
        x.add_row([key, date_info[key]['recite_counts'],
                   date_info[key]['add_counts'],
                   date_info[key]['del_counts'],
                   date_info[key]['mod_counts']])
    print(x)


def load_data():
    '''load date_info and words_table object from pickled file'''

    try:
        with open('words_table.pk', 'rb') as f:
            global words_table
            words_table = pickle.load(f)
        with open('date_info.pk', 'rb') as f:
            global date_info
            date_info = pickle.load(f)
    except Exception as e:
        print(e)


def pickle_data():
    '''pickle date_info and words_table object into file'''

    try:
        with open('words_table.pk', 'wb') as f:
            pickle.dump(words_table, f)
        with open('date_info.pk', 'wb') as f:
            pickle.dump(date_info, f)
    except Exception as e:
        print(e)


def auto_cls(arg):
    try:
        assert arg in ('on', 'off')
        global cls_switch
        cls_switch = arg
    except AssertionError:
        print("auto_cls's argument must be 'on' or 'off'")


def quits():
    '''quit'''

    pickle_data()
    exit()


def clear_screen():
    '''clear the screen'''

    if cls_switch == 'on':
        return

    sysstr = platform.system()
    if sysstr == 'Windows':
        os.system('cls')
    elif sysstr == 'Linux':
        os.system('clear')
    else:
        print('Unkonw system, can not clear screen')


def help_info():
    '''print help information'''

    print(
        """
            '<>' express you need to add a argument here. such as 
                    command:add apple 苹果


            help:                       print help info
            all:                        show all words 
            info:                       show statistics
            next:                       show next word   
            quit:                       quit
            import:                     import words from file
            export:                     export words into file 
            add <word> <translation>:   add a word and it's translation
            del <word> <translation>:   delete a word
            mod <word> <translation>:   modify word's translation
            auto_cls <on/off>:          open/close auto clear screen
            search <word>:              search word in word table
        """)


# modify words table functions

def add_word(word, translation='no translation'):
    '''add a words and it's translation into words table'''

    words_table[word] = dict()
    words_table[word]['translation'] = translation
    add_counts()


def del_word(word):
    '''delete a words from words table'''

    if word in words_table:
        words_table.pop(word)
        del_counts()
    else:
        print('Try to del a word not in words table')


def mod_translation(word, translation):
    '''modify a words's translation'''

    if word in words_table:
        words_table[word]['translation'] = translation
        mod_counts()
    else:
        print('Try to modify a word not in words table')


def next():
    '''print next word'''

    table = []
    key = random.choice(list(words_table.keys()))
    table.append([key, words_table[key]['translation']])
    print_words(table)


# search functons

def serach(word):
    '''search a word's translation'''

    if word in words_table:
        table = []
        table.append([word, words_table[word]['translation']])
        print_words(table)
    else:
        print("{0} doesn't in words table".format(word))


def all_words():
    '''print all words in words_table'''

    table = []
    for key in words_table.keys():
        table.append([key, words_table[key]['translation']])
    print_words(table)


# import and export functions

def import_words():
    '''import words from a file into words table'''

    try:
        with open('words.txt', 'r', encoding='utf-8') as f:
            while True:
                line = f.readline().split()
                if not line:
                    break
                add_word(line[0], line[1])
    except Exception as e:
        print('Import Error')
        print(e)


def export_words():
    '''export words from words table into file'''

    keys = list(words_table.keys())
    try:
        with open('words.txt', "w", encoding='utf-8') as f:
            for key in keys:
                line = '{0} {1}\n'.format(key, words_table[key]['translation'])
                f.write(line)
    except Exception as e:
        print('Export Error')
        print(e)


command = {
    'help':     help_info,
    'all':      all_words,
    'next':     next,
    'info':     print_info,
    'quit':     quits,
    'add':      add_word,
    'del':      del_word,
    'mod':      mod_translation,
    'search':   serach,
    'import':   import_words,
    'export':   export_words,
    'auto_cls': auto_cls
}


def main():
    load_data()
    help_info()

    while True:
        cmd = input('command: ')
        if cmd == '':
            if last_cmd == '':
                continue
            else:
                cmd = last_cmd
        else:
            last_cmd = cmd

        clear_screen()
        args = cmd.split()
        if args[0] in command:
            tmp_args = tuple(args[1:])
            command[args[0]](*tmp_args)
        else:
            print("Wrong command ,input help for more information")


if __name__ == '__main__':
    main()
