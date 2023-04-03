import random
import matplotlib.pyplot as plt
from algorithm import SortingAlgorithm, bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, bogo_sort


class SortingVisualizer:
    def __init__(self, array_size=50):
        self.array_size = array_size
        self.array = [random.randint(1, 100) for _ in range(array_size)]

    def visualize(self, arr):
        plt.clf()
        plt.bar(range(len(arr)), arr)
        plt.pause(0.05)

    def run(self, sorting_algorithm: SortingAlgorithm):
        plt.ion()
        plt.title(sorting_algorithm.name)
        sorting_algorithm.function(self.array, self.visualize)
        plt.show(block=True)


def main():
    sorting_algorithms = [
        SortingAlgorithm("Bubble Sort", bubble_sort),
        SortingAlgorithm("Selection Sort", selection_sort),
        SortingAlgorithm("Insertion Sort", insertion_sort),
        SortingAlgorithm("Merge Sort", merge_sort),
        SortingAlgorithm("Quick Sort", quick_sort),
        SortingAlgorithm("Bogo sort", bogo_sort),
    ]

    visualizer = SortingVisualizer()

    print("Available sorting algorithms:")
    for index, algorithm in enumerate(sorting_algorithms):
        print(f"{index + 1}. {algorithm.name}")

    selected_algorithm = int(
        input("Enter the number of the algorithm you want to visualize: ")) - 1
    algorithm = sorting_algorithms[selected_algorithm]

    print(f"Visualizing {algorithm.name}...")
    visualizer.run(algorithm)


if __name__ == "__main__":
    main()
