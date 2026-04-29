import random
import time
from mergesort import merge_sort
from quicksort import quick_sort


def generate_data(size):
    return [random.randint(1, 100000) for _ in range(size)]


def time_sort(sort_function, data):
    test_data = data[:]
    start = time.perf_counter()
    sorted_data = sort_function(test_data)
    end = time.perf_counter()
    return sorted_data, end - start


def benchmark_size(size, trials=7):
    merge_total = 0
    quick_total = 0

    for trial in range(1, trials + 1):
        data = generate_data(size)

        merge_result, merge_time = time_sort(merge_sort, data)
        quick_result, quick_time = time_sort(quick_sort, data)

        expected = sorted(data)

        if merge_result != expected or quick_result != expected:
            raise ValueError(
                f"Sorting results were incorrect for size {size}, trial {trial}."
            )

        merge_total += merge_time
        quick_total += quick_time

    return merge_total / trials, quick_total / trials


def main():
    sizes = [1000, 5000, 10000, 20000, 50000, 100000, 200000, 300000]
    trials = 7

    print(f"Running {trials} trials per dataset size.")
    print()

    for size in sizes:
        merge_avg, quick_avg = benchmark_size(size, trials)

        if merge_avg < quick_avg:
            faster = f"Merge Sort ({quick_avg / merge_avg:.2f}x faster)"
        elif quick_avg < merge_avg:
            faster = f"Quick Sort ({merge_avg / quick_avg:.2f}x faster)"
        else:
            faster = "Tie"

        print(f"Dataset size: {size}")
        print(f"  Merge Sort average: {merge_avg:.6f} seconds")
        print(f"  Quick Sort average: {quick_avg:.6f} seconds")
        print(f"  Faster: {faster}")
        print()


if __name__ == "__main__":
    main()