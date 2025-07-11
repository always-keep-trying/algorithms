import numpy as np

def recursive_method(nums, val):
    left = 0
    right = len(nums) - 1
    mid = (left+right) // 2

    if nums[mid] > val:
        # Search in the list that is left of mid
        return recursive_method(nums[:mid], val)
    elif nums[mid] < val:
        # Search in the list that is right of the mid
        return mid + 1 + recursive_method(nums[mid+1:],val)
    else: # when nums[mid] == val
        return mid


def iterative_method(nums, val):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2

    while nums[mid] != val:
        if nums[mid] > val:
            # update the right value
            right = mid-1
        else:
            # update the left value
            left = mid + 1
        mid = (left + right) // 2
    return mid


def main(list_example, search_val):
    # list must be sorted!
    list_example.sort()

    correct_index = list_example.index(search_val)
    print(f"{list_example=}")
    print(f"{search_val=}")
    print(f"{correct_index=}\n")

    print("1. Recursive Method")
    Recursive_Method = recursive_method(list_example, search_val)
    print(f"Recursive Ans: {Recursive_Method}")
    print(Recursive_Method == correct_index)

    print("\n2. Iterative Method")
    Iterative_Method = iterative_method(list_example, search_val)
    print(f"Iterative Ans: {Iterative_Method}")
    print(Iterative_Method == correct_index)

if __name__ == "__main__":
    rng = np.random.default_rng()
    test_l = rng.choice(500,size=30,replace=False)
    test_l = list(map(int,sorted(test_l)))
    X = test_l[np.random.choice(30)]

    main(test_l, X)


