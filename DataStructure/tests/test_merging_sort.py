from Linked_List.merging_sort import merge,merge_sort
import pytest
def test_merge_sort():
    arr1 = [8, 4, 23, 42, 16, 15]
    merge_sort(arr1)
    assert arr1 == [4, 8, 15, 16, 23, 42]

    arr2 = [20, 18, 12, 8, 5, -2]
    merge_sort(arr2)
    assert arr2 == [-2, 5, 8, 12, 18, 20]

    arr3 = [5, 12, 7, 5, 5, 7]
    merge_sort(arr3)
    assert arr3 == [5, 5, 5, 7, 7, 12]

    arr4 = [2, 3, 5, 7, 13, 11]
    merge_sort(arr4)
    assert arr4 == [2, 3, 5, 7, 11, 13]

    print("All tests pass!")


test_merge_sort()
