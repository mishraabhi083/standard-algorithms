def bin_search(arr, ele):
    start, end = 0, len(arr)
    while start <= end:
        # print(arr[start:end])
        mid = (start + end) // 2
        if arr[mid] == ele:
            return mid + 1
        else:
            if arr[mid] < ele:
                start = mid + 1
            elif arr[mid] > ele:
                end = mid - 1
    return False


if __name__ == "__main__":
    print(
        'found : ',
        bin_search(list(map(int,
                            input("Enter data : ").strip().split())),
                   int(input("Enter num to search : "))))
