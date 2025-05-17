import random
from collections import Counter

FUSION_RULES = {
    frozenset(['red', 'blue']): 'purple',
    frozenset(['blue', 'purple']): 'red',
    frozenset(['purple', 'red']): 'blue'
}

# Start counts with one extra blue egg added (you can change this)
start_counts = {
    'blue': 23 + 1,
    'purple': 33,
    'red': 43
}

def print_counts(counts):
    return f"blue: {counts['blue']}, purple: {counts['purple']}, red: {counts['red']}"

def simulate_fusion_verbose(start_counts):
    eggs = (
        ['blue'] * start_counts['blue'] +
        ['purple'] * start_counts['purple'] +
        ['red'] * start_counts['red']
    )

    step = 1
    print(f"Starting eggs: {print_counts(Counter(eggs))}\n")

    while len(eggs) > 1:
        count = Counter(eggs)
        sorted_colors = sorted(count.items(), key=lambda x: -x[1])
        color1 = sorted_colors[0][0]
        color2 = sorted_colors[1][0]

        # Handle tie for second and third place
        if len(sorted_colors) > 2 and sorted_colors[1][1] == sorted_colors[2][1]:
            color2 = random.choice([sorted_colors[1][0], sorted_colors[2][0]])

        eggs.remove(color1)
        eggs.remove(color2)

        fused = FUSION_RULES[frozenset([color1, color2])]
        eggs.append(fused)

        count_after = Counter(eggs)
        print(f"Step {step}: Fuse '{color1}' + '{color2}' -> '{fused}'")
        print(f"Egg counts now: {print_counts(count_after)}\n")

        step += 1

    print(f"Final egg hatched: {eggs[0]}")
    return eggs[0]

simulate_fusion_verbose(start_counts)
