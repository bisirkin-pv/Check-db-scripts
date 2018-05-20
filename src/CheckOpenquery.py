# -*- coding: utf-8 -*-
import re
import os
import time

FILE = 'testGood.sql'


# Check file on contains openquery
class CheckQpenquery:
    def __init__(self, input_file):
        self.__filename = input_file
        self.__pattern_one = re.compile(r'[ ]+openquery\b', re.I)
        self.__pattern_two = re.compile(r'([a-z_\[\]]+)\.(?:[a-z_\[\]]+)\.(?:[a-z_\[\]]+)\.(?:[a-z_\[\]]+)', re.I)
        self.__result = ''
        self.__count_error = 0

    def print_name(self):
        print('File "{0}" ({1})'.format(self.__filename, self.__count_error))

    def print_file(self):
        try:
            with open(self.__filename) as file_handler:
                for line in file_handler:
                    print(line.replace('\n', ''))
        except IOError:
            print("An IOError has occurred!")

    def check(self):
        try:
            with open(self.__filename) as file_handler:
                for num, line in enumerate(file_handler):
                    res = re.findall(self.__pattern_one, line)
                    if len(res) > 0:
                        self.__result += '\tLine {0:4} [Error] contains openquery\n'.format(num)
                        self.__count_error += 1
                    res = re.findall(self.__pattern_two, line)
                    if len(res) > 0:
                        self.__result += '\tLine {0:4} [Error] contains linked server [{1}]\n'.format(num+1
                                                                                                      , res[0]
                                                                                                      )
                        self.__count_error += 1
        except IOError:
            print("An IOError has occurred!")

    def print_result(self):
        print(self.__result)

    def result(self):
        return self.__count_error


def get_file_list(current_dir):
    return [__file for __file in os.listdir(current_dir) if __file.endswith('.sql')]


def run(check_file, show_all_info):
    check_openquery = CheckQpenquery(check_file)
    check_openquery.check()
    check_openquery.print_name()
    if show_all_info:
        check_openquery.print_result()
    return check_openquery.result()


if __name__ == "__main__":
    start_time = time.time()
    files = get_file_list(os.getcwd())
    count_error_file = 0
    count_error_line = 0
    print('Start check file\n')
    for file in files:
        res = run(file, True)
        count_error_line += res
        count_error_file += res > 0 if 1 else 0
    print('Statistic: check {0} file(s), {1} error(s) file(s), {2:.2f}% percent'.format(len(files)
                                                                                        , count_error_file
                                                                                        , count_error_file / len(files)
                                                                                        ))
    print('Line with error(s): {0}'.format(count_error_line))
    print('Finish, executing time({0:.3f}ms)'.format(time.time() - start_time))
    exit(count_error_file > 0 if 1 else 0)



