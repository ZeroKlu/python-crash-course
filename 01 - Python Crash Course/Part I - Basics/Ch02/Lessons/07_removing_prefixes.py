print("Chapter 2:")
print("Exercise 6a - Removing Prefixes")

# The 3rd edition textbook introduces two additional string manipulation functions

# The removeprefix() function allows you to remove specified characters at the beginning of a string
no_starch_url = "https://nostarch.com"

# Here, we remove the protocol from the beginning of a URL
print(no_starch_url.removeprefix("https://"))

# Note: This function does not modify the original string
print(no_starch_url)

# The removesuffix() function allows you to remove specified characters at the end of a string
print(f"\nThe protocol used by the No Starch URL is {no_starch_url.removesuffix('://nostarch.com')}")

# Note: This function does not modify the original string either
print(no_starch_url)
