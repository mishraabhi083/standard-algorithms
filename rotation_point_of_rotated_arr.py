def rotation_generator(arr, x):
    print('rotated array : ', arr[x:] + arr[:x])
    return arr[x:] + arr[:x]


def rotation_point_finder(arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        print(arr[low:high])
        if arr[low] <= arr[high]:
            return low
        mid = (low + high) // 2

        if arr[(mid - 1 + len(arr)) % len(arr)] > mid < arr[(mid + 1) %
                                                            len(arr)]:
            return mid

        if arr[low] >= arr[mid]:
            low = mid + 1
        elif arr[mid] >= arr[high]:
            high = mid - 1


if __name__ == "__main__":
    print(
        'rotation point at : ',
        rotation_point_finder(
            rotation_generator(
                list(map(int,
                         input("Enter array : ").strip().split())),
                int(input("Enter rotations to be performed : ")))))
