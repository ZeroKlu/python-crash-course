print("Chapter 10:")
print("Exercise 12 - Bonus Lesson - Why 'except: pass' is bad!\n")

# I mentioned before that using the pass command is frequently bad form in an except block,
#   especially in a generic one. Let's take a look at a concrete example of why

# Here, I have created an obvious infinite loop. In the real world it will be more difficult
#   to detect infinite-run conditions, but this illustrates the idea

i = 0
while True:
    try:
        i += 1
        print(f"(iteration {i}) - I'm just gonna run forever...")
    except KeyboardInterrupt:
        # A keyboard interrupt (like CTRL+C) is an exception in Python, so it will be caught in an except block
        print("OK... I'll stop... :(")
        break
    except Exception as ex:
        # Any other kind of exception will not break the loop
        print(ex)
        # I am using pass correctly here, since I have already handled the exception
        pass

# The above example will still allow you to use CTRL+C to stop your infinite loop, since you're
#   explicitly calling break when you catch a KeyboardInterrupt exception

# But imagine if your code looked like this (WARNING! Uncomment lines 30 to 36 at your own risk)

# i = 0
# while True:
#     try:
#         i += 1
#         print(f"(iteration {i}) I'm just gonna run forever...")
#     except:
#         pass

# Now, a KeyboardInterrupt still gets caught by the except block, but since you're just passing on to the
#   next command, it doesn't do anything, and you have no way to kill the infinite loop.

# This is just one example, and there are hundreds of reasons why 'except: pass' is bad, but I hope this
#   helps drive home the idea that you simply shouldn't do it.
