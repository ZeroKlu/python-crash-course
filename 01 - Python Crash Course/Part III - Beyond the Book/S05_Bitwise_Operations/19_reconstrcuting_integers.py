def reconstruct_integers(bytes: list[int], size: int=4) -> list[int]:
    assert len(bytes) % size == 0, "Invalid data!"

    num_units = len(bytes) // size

    integers = []

    for n in range(0, num_units * size, size):
        data = bytes[n:n+size]
        integers.append(reconstruct_integer(data, size))
    
    return integers

def reconstruct_integer(data: list[int], size: int=4) -> int:
    assert len(data) == size, "Invalid data!"

    num = 0

    for p in range(len(data)):
        num += data[p] << (p * 8)
    
    return num

def main() -> None:
    bytes = [
        0b0000_0000, 0b0000_0000, 0b0000_0000, 0b0000_0000,
        0b1101_0010, 0b0000_0010, 0b1001_0110, 0b0100_1001,
        0b0001_0101, 0b1100_1101, 0b0101_1011, 0b0000_0111,
        0b1111_1111, 0b1111_1111, 0b1111_1111, 0b1111_1111
    ]
    values = reconstruct_integers(bytes)
    for value in values:
        out = f"{value:,}"
        print(f"{out:>13}")

if __name__ == "__main__":
    main()
