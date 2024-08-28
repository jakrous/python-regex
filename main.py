import re
import json


def find_matches(pattern, test_string):
    # Compile the pattern
    compiled_pattern = re.compile(pattern)

    # Initialize an empty list to hold match details
    matches = []
    matches_found = False

    # Find all matches in the test string
    for match in compiled_pattern.finditer(test_string):
        matches_found = True
        start = match.start()
        end = match.end()
        matched_text = match.group()

        # Create a dictionary for each match
        match_object = {
            "matchedText": matched_text,
            "startIndex": start,
            "endIndex": end
        }

        # Add the match dictionary to the list of matches
        matches.append(match_object)

    # Create the final result dictionary
    result = {
        "pattern": pattern,
        "testString": test_string,
        "matchesFound": matches_found,
        "matches": matches
    }

    # Convert the result to a JSON string
    return json.dumps(result, indent=2)


# Example usage
pattern = "gray|grey"
test_string = "there is a grey fox in the gray building"
json_result = find_matches(pattern, test_string)
print(json_result)
