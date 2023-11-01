def format_table(benchmarks, algos, results):
    first_column_len = max(map(len, benchmarks + ['Benchmark']))

    col_len = [max(map(len, [(algos[i])] + [(str(results[0][i]))] + [(str(results[1][i]))] )) for i in
               range(len(algos))]
    print(col_len)

    head = f"| {'Benchmark': <{first_column_len}} |"
    total_len = first_column_len + len(algos) + 2  # +2 there

    i = 0
    for alg in algos:
        head += f" {alg: <{col_len[i]}} |"
        total_len += col_len[i] + 2  # and there means +2 additional spaces
        i += 1
    print(head)

    print(f"|{'-' * total_len}|")

    for bench in range(len(benchmarks)):
        line = f"| {benchmarks[bench]: <{first_column_len}} |"
        for alg in range(len(results[bench])):
            line += f" {results[bench][alg]: <{col_len[alg]}} |"
        print(line)


format_table(["the besttttttttttttttt", "the worst"],
             ["quick sort", "merge sort", "bubble sort", "super-new ultra sort"],
             [[1.2888888888777777777778883, 1.56, 2.0, 1.0], [3.3, 2.9, 3.9, 1.1]])
