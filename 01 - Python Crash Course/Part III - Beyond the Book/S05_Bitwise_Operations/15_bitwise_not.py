def set_bit(word: int, pos: int, value: int) -> int:
    mask = 1 << pos
    if value == 0:
        return word & ~mask
    elif value == 1:
        return word | mask
    else:
        return word

def bitwise_not(n, num_bits=8) -> int:
    return ~n & ((1 << num_bits) - 1)

def main() -> None:
    b = 0b10011100
    print(f"b = {b:>08b}")
    n = ~b
    
    # Note: This doesn't give the expected answer
    print("n =", bin(n).split('b')[1], "*wrong")

    # That happens because all integers in Python are signed
    # Because of this, you should be careful with using ~ in Python

    # We can compensate for this by using a more complicated operation
    n = bitwise_not(b)
    print(f"n = {n:>08b} *right")

    for pos in range(0, 8):
        print(set_bit(0, pos, 1))

if __name__ == "__main__":
    main()