# To use regular expressions, import the "re" module
import re

def pause():
    input("\nPress <ENTER> to continue...")

# The following special characters are supported
#
#   .           Any character except newline (If DOTALL flag is on, matches newline as well)
#   ^           Start of string
#   $           End of string
#   *           Zero or more of the immediately preceding item
#   +           One or more of the immediately preceding item
#   ?           Zero or one of the immediately preceding item
#   *?          Zero or more of the immediately preceding item (non-greedy match)
#   +?          One or more of the immediately preceding item (non-greedy match)
#   ??          Zero or one of the immediately preceding item (non-greedy match)
#   {n}         Matches exactly n instances of the preceding item
#   {m, n}      Matches m to n instances of the preceding item
#   {m, n}?     Matches m to n instances of the preceding item (non-greedy match)
#   \           Escapes special characters or signals special sequence
#   []          Set: matches any character in the contained set
#   a|b         Matches regex a or regex b
#   (regex)     Matches entire contained regex
#   \A          Matches only at beginning of string
#   \b          Matches empty string at beginning or end of a word (boundary between \w and \W)
#   \B          Matches empty string EXCEPT at beginning or end of a word
#   \d          Any digit (equivalent to [0-9])
#   \D          Any non-digit (equivalent to [^0-9])
#   \s          Any whitespace character ([ \t\n\r\f\v] and potentially others)
#   \S          Any non-whitespace character ([^ \t\n\r\f\v])
#   \w          Any word character ([a-zA-Z0-9_])
#   \W          Any non-word character ([^a-zA-Z0-9_])
#   \Z          Matches only at end of string

# Also supports standard Python character escapes  (\a  \b  \f  \n  \N  \r  \t  \u  \U  \v  \x  \\)

# Notes on sets []
#   ^           If the first character in the set, negates is (match anything EXCEPT what is in the remaining set)
#   -           Indicates range, e.g.:   a-z 0-9
#   all         Special characters lose their meaning in a set (except square-brackets)

# Some examples of phone numbers:
phone_numbers = ["7134833111", "713-483-3111", "713.483.3111", "713,483,3111", "(713) 483-3111", "(713) 483-3111 ext: 42"]

# Some regular expressions for a phone number
regex_examples = {
    "naive": r"\d{10}",
    "bad": r"\d{3}-\d{3}-\d{4}",
    "mediocre": r"\d{3}[-.,]\d{3}[-.]\d{4}",
    "ok": r"^\(?\d{3}[)-.,]?\s?\d{3}[-.,]?\d{4}$",
    "good": r"^\(?\d{3}[)-.,]?\s?\d{3}[-.,]?\d{4}\s?e?x?t?:?\s?\d*$"
}

for key in regex_examples.keys():
    numbers = []
    regex = re.compile(regex_examples[key])
    for phone in phone_numbers:
        if regex.search(phone): numbers.append(phone)
    print(f"\nUsing the {key} regex, matched the following phone numbers:")
    for number in numbers:
        print(f" - {number}")
    pause()
