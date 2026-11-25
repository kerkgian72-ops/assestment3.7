def build_unsorted_unique_letters(full_name: str) -> list[str]:
    """
    Excludes non-alphabetic characters/symbols and discards duplicate letters
    while preserving order of first appearance.
    """
    seen = set()
    unsorted_letters = []
    for ch in full_name.upper():
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            unsorted_letters.append(ch)
    return unsorted_letters


def selection_sort(arr: list[str]) -> list[str]:
    """Sorts a list of characters alphabetically in ascending order."""
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    return sorted_arr


if __name__ == "__main__":
    full_name = "KERK GIAN PUBLICO"

    unsorted_array = build_unsorted_unique_letters(full_name)
    sorted_array = selection_sort(unsorted_array)

    print("=== ASSESSMENT 3.7: SORTING ALGORITHMS ===")
    print(f"Full Name      : {full_name}")
    print(f"Unsorted Array : {unsorted_array}")
    print(f"Sorted Array   : {sorted_array}")