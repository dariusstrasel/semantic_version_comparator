"""
Title: Semantic Versioning Comparator
Author: Darius Strasel | strasel.darius@gmail.com
Objective:

Create a Python library from scratch that will compare two semantic version strings. A successful implementation will be able to test two strings for the following:

Equal (==)
Greater than (>)
Greater than or equal to (>=)
Pessimistic (~>)
Less than (<)
Less than or equal to (<=)

Constraints:
Only use libraries built into Python itself (ie. ‘os’, ‘sys’, etc). Nothing from pypi or other external sources.
Use Python 2.7 or 3+

"""
import argparse


def valid_input():
    parser = argparse.ArgumentParser(description='Compare two semantic version strings to determine which is greater.')
    parser.add_argument('versions', metavar='version-strings', type=str, nargs=2,
                        help='an indiviual string representing one semantic version.')
    args = parser.parse_args()
    if args:
        return args



def main():
    if valid_input():
        print("Success")
    else:
        print("Failed")

if __name__ == "__main__":
    main()