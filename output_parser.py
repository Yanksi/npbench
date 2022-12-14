results = {
    "benchmark": {"Numpy": "Numpy", "Parallel": "Parallel", "Tasking": "Tasking", "ChunkingRelative32": "ChunkingRelative32", "ChunkingAbsolute16": "ChunkingAbsolute16", "ChunkingAbsolute32": "ChunkingAbsolute32", "ChunkingAbsolute64": "ChunkingAbsolute64"}
}
with open("benchmark_chunking.txt", "r") as f:
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
        elif l.startswith("DaCe CPU - auto_opt_omp_tasking_chunking_relative_32 - "):
            f.readline()
            curr_result["ChunkingRelative32"] = int(f.readline()[63:-3])
        elif l.startswith("DaCe CPU - auto_opt_omp_tasking_chunking_absolute_16 - "):
            f.readline()
            curr_result["ChunkingAbsolute16"] = int(f.readline()[63:-3])
        elif l.startswith("DaCe CPU - auto_opt_omp_tasking_chunking_absolute_32 - "):
            f.readline()
            curr_result["ChunkingAbsolute32"] = int(f.readline()[63: -3])
        elif l.startswith("DaCe CPU - auto_opt_omp_tasking_chunking_absolute_64 - "):
            f.readline()
            curr_result["ChunkingAbsolute64"] = int(f.readline()[63: -3])
        elif l.startswith("***** "):
            results[curr_bench_name] = curr_result
            curr_bench_name = l.split(" ")[5]
            curr_result = {}

with open("results_chunking.csv", "w") as f:
    for bench_name in results:
        f.write(
            "{},{},{},{},{},{},{},{}\n".format(
                bench_name,
                results[bench_name]["Numpy"],
                results[bench_name]["Parallel"],
                results[bench_name]["Tasking"],
                results[bench_name]["ChunkingRelative32"],
                results[bench_name]["ChunkingAbsolute16"],
                results[bench_name]["ChunkingAbsolute32"], 
                results[bench_name]["ChunkingAbsolute64"]

            )
        )
