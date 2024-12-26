inp = [l.strip().split() for l in open("day1/inp.txt", "r").readlines()]
print(
    sum(
        [
            abs(x - y)
            for x, y in zip(
                sorted([int(split[0]) for split in inp]),
                sorted([int(split[-1]) for split in inp]),
            )
        ]
    )
)
