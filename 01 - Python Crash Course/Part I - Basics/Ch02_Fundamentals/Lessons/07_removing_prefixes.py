"""Lesson 2.7"""

print("Chapter 2:")
print("Exercise 7 - Removing Prefixes")

no_starch_url = "https://nostarch.com"

# Here, we remove the protocol from the beginning of a URL
print(no_starch_url.removeprefix("https://"))

# Note: This function does not modify the original string
print(no_starch_url)

# The removesuffix() function allows you to remove specified characters at the end of a string
print("\nThe protocol used by the No Starch URL is " + \
      f"{no_starch_url.removesuffix('://nostarch.com')}")

# Note: This function does not modify the original string either
print(no_starch_url)
