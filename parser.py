results = {"benchmark":{"Numpy":"Numpy", "Parallel":"Parallel", "Tasking":"Tasking"}}
with open("results.txt", "r") as f:
    curr_bench_name = f.readline().split(" ")[5]
    curr_result = {}
    for l in f:
        if l.startswith("NumPy - default - validation: "):
            np_time = int(l[30:-3])
            curr_result["Numpy"] = np_time
        elif l.startswith("DaCe CPU - auto_opt_omp_parallel - "):
            f.readline()
            curr_result["Parallel"] = int(f.readline()[43:-3])
        elif l.startswith("DaCe CPU - auto_opt_omp_tasking - "):
            f.readline()
            curr_result["Tasking"] = int(f.readline()[42:-3])
        elif l.startswith("***** "):
            results[curr_bench_name] = curr_result
            curr_bench_name = l.split(" ")[5]
            curr_result = {}

with open("parsed_result.csv", "w") as f:
    for bench_name in results:
        f.write("{},{},{},{}\n".format(
            bench_name,
            results[bench_name]["Numpy"],
            results[bench_name].get("Parallel", "NULL"),
            results[bench_name].get("Tasking", "NULL"),
        ))

