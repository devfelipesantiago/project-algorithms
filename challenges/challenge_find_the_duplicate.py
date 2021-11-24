from challenges.merge_sort import merge_sort


def find_duplicate(nums):
    """Faça o código aqui."""
    if not nums:
        return False
    nums = merge_sort(nums)

    for first, secund in zip(nums[:-1], nums[1:]):
        if first == secund and first > 0:
            return first
    return False
