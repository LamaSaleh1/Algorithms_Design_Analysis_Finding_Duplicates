import time
import random

def find_duplicates_optimized(arr):
    """
    Optimized duplicate detection using two sets
    Time Complexity: O(n) 
    Space Complexity: O(n) 
    """
    seen = set()
    duplicates_set = set()

    for num in arr:
        if num in seen:
            duplicates_set.add(num)
        else:
            seen.add(num)

    return list(duplicates_set)


def generate_test_data(size):
    """Generate student ID test data with random duplicates"""
    # Generate random base IDs between 100 and 200
    count = min(80, max(1, size // 2)) 
    base_ids = random.sample(range(100, 201), count)

    test_data = []
    for _ in range(size):
        # 50% chance to pick from base IDs (creating duplicates)
        if random.random() < 0.5 and base_ids:
            test_data.append(random.choice(base_ids))
        else:
            # Generate a new random ID
            test_data.append(random.randint(100, 200))
            
    return test_data

def test_optimized_algorithm():
    """Test optimized algorithm with 3 sizes: 10, 100, 1000"""

    print("OPTIMIZED ALGORITHM PERFORMANCE TEST")
    print("-" * 50)

    sizes = [10, 100, 1000, 10000]

    for size in sizes:
        print(f"\nTesting with {size} elements:")

        # Generate test data
        test_data = generate_test_data(size)
        print(f"Sample data: {test_data[:8]}") # Show first 8 elements

        # Run optimized algorithm
        start_time = time.time()
        duplicates = find_duplicates_optimized(test_data)
        end_time = time.time()

        execution_time = end_time - start_time

        print(f"Execution time: {execution_time:.6f} seconds")
        print(f"Duplicates found: {len(duplicates)}")
        if duplicates:
            print(f"First 5 duplicates: {duplicates[:5]}")
        else:
            print(f"No duplicates found")

# Run the tests
if __name__ == "__main__":
    test_optimized_algorithm()