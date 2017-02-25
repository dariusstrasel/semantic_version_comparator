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


Using: http://semver.org/
Cool Semantic Regex: \bv?(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[\da-z\-]+(?:\.[\da-z\-]+)*)?(?:\+[\da-z\-]+(?:\.[\da-z\-]+)*)?\b
"""
import argparse
import re


def capture_arguments(fake_arguments=None) -> dict:
    """Parse arguments passed into program and verify if valid. Returns arguments as dictionary if valid."""
    parser = argparse.ArgumentParser(description='Compare two semantic version strings.')
    parser.add_argument('versions', metavar='version-string', type=str, nargs=2,
                        help='an individual string representing a semantic version.')
    if fake_arguments:
        arguments = vars(parser.parse_args())
    elif not fake_arguments:
        arguments = vars(parser.parse_args())
    valid_args = [is_valid_version_string(argument).group for argument in arguments["versions"] if is_valid_version_string(argument)]
    # print("Arguments: %s" % arguments)
    # print("Valid Args: %s" % valid_args)
    if len(valid_args) == 2:
        return arguments
    else:
        print("Argument style was not valid semantic version format. Also, alpha, and beta tags not yet supported.")
        return False


def return_weighted_arguments(input_args) -> list:
    """Calculate the weight of input_arguments and return their converted values in a list."""
    if input_args:
        return calculate_weights(input_args)


def is_valid_version_string(input_string) -> object:
    """Return a SRE_match object if the input_string returns a regex pattern match."""
    version_regex = re.compile(r"^[0-9*]+.[0-9*]+.[0-9]+$")
    return version_regex.match(input_string)


def calculate_weights(input_versions) -> list:
    """Convert list of semantic version strings (major, minor, patch)
     into their base ten equivalents and return their sums in a list."""
    result = []
    # print(input_versions)
    if input_versions:
        for version in input_versions:
            # print(version)
            version_as_list = version.split(".")
            major_weight = int(version_as_list[0]) * 100
            minor_weight = int(version_as_list[1]) * 10
            patch_weight = int(version_as_list[2]) * 1
            total_weight = major_weight + minor_weight + patch_weight
            result.append(total_weight)
        return result


def test_versions(versions, weighted_versions):
    """Equal (==)
Greater than (>)
Greater than or equal to (>=)
Pessimistic (~>)
Less than (<)
Less than or equal to (<=)"""
    first_string = versions[0]
    second_string = versions[1]
    first_string_weighted = weighted_versions[0]
    second_string_weighted = weighted_versions[1]
    result_string_schema = "'{}' {} '{}'"
    if first_string_weighted == second_string_weighted:
        print(result_string_schema.format(first_string, "equals", second_string))
    if first_string_weighted > second_string_weighted:
        print(result_string_schema.format(first_string, "is greater than", second_string))
    if first_string_weighted >= second_string_weighted:
        print(result_string_schema.format(first_string, "is greater than or equal to", second_string))
    if first_string_weighted < second_string_weighted:
        print(result_string_schema.format(first_string, "is less than", second_string))
    if first_string_weighted <= second_string_weighted:
        print(result_string_schema.format(first_string, "is less than or equal to", second_string))


def main():
    arguments = capture_arguments()
    if arguments:
        # print("Success")
        # print(arguments["versions"])
        # print(return_weighted_arguments(arguments["versions"]))
        test_versions(arguments["versions"], return_weighted_arguments(arguments["versions"]))
    else:
        print("No valid arguments were captured.")

if __name__ == "__main__":
    main()