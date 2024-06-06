"""
This module is the setup for running the tests. It allows you to test one
algorithm at a time. That algorithm is sent to the config file which will be
read by the test file and added to the parameterize decorator.
"""

import subprocess
import configparser
from pathlib import Path
from test_sort import available

algorithms = list(available.keys())
config_path = Path.joinpath(Path.cwd(), 'config.ini')


def read_config():
    """Open and read the config file"""
    config = configparser.ConfigParser()
    config.read(config_path)
    return config


def write_current_algorithm(config, algorithm):
    """Writes the algorithm that the user wants to test to the config file."""
    config.set('algorithm', 'current', algorithm)
    with open(config_path, 'w') as file:
        config.write(file)


def run_test():
    """Runs the pytest file using subprocess"""
    subprocess.run(['pytest', '--verbose'])


def input_loop():
    """The main loop that allows the user to run as many tests as they want."""
    while True:
        print("\nEnter 'q' at any time to quit\n")
        for algorithm in algorithms:
            print(algorithm)
        choice = input('\nEnter which algorithm you want to test:\n>>> ').strip().lower()
        choice = choice.replace(' ', '_')
        if choice == 'q':
            break
        elif choice not in algorithms:
            print(f'"{choice.upper()}" not a valid option, try again')
            continue
        else:
            write_current_algorithm(config, choice)
            run_test()
            another = input('Test another algorithm? (y/n):\n>>> ').lower().strip()
            if another == 'y':
                continue
            else:
                break


if __name__ == '__main__':
    config = read_config()
    input_loop()
