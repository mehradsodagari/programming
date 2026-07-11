problem_sizes = [1000, 2000, 4000, 10_000, 100_000]
print("problem size", "|", "iterations")
for problem_size in problem_sizes:
    counter = 0
    print(problem_size, "|", end="")
    while problem_size > 0:
        counter += 1
        problem_size //= 2
    print(counter)
    counter = 0
