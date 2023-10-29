def format_table(benchmarks, algos, results):
    first_column_len = max(map(len, benchmarks + ['Benchmark']))
    head = f"| {'Benchmark': <{first_column_len}} |"
    total_len = first_column_len + len(algos) + 2  # +2 there

    for alg in algos:
        head += f" {alg} |"
        total_len += len(alg) + 2  # and there means +2 additional spaces
    print(head)

    print(f"|{'-' * total_len}|")

    for bench in range(len(benchmarks)):
        line = f"| {benchmarks[bench]: <{first_column_len}} |"
        for alg in range(len(results[bench])):
            line += f" {results[bench][alg]: <{len(algos[alg])}} |"
        print(line)


format_table(["the best case", "worst"],
             ["quick sort", "merge sort", "bubble sort", "super-new ultra sort"],
             [[1.23, 1.56, 2.0, 1.0], [3.3, 2.9, 3.9, 1.1]])
