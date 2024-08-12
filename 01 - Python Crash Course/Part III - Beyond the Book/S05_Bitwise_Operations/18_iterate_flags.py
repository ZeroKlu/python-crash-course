from enum import IntFlag
from random import randint

class Settings(IntFlag):
    DebugMode = 1,
    InteractiveMode = 2,
    RememberSettings = 4,
    Optimize = 8

def main() -> None:
    settings = randint(0, 15)
    print(f"With Settings: {settings}, the following bits are set:")
    currentValue = 1
    while settings > 0:
        if settings & 1: print(f"- {Settings(currentValue).name}")
        settings >>= 1
        currentValue <<= 1

if __name__ == "__main__":
    main()
