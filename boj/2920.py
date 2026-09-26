music_sort_list = [1, 2, 3, 4, 5, 6, 7, 8]
music_reverse_list = [8, 7, 6, 5, 4, 3, 2, 1]

input_list = list(map(int, input().split()))
if input_list == music_sort_list:
    print("ascending")
elif input_list == music_reverse_list:
    print("descending")
else:
    print("mixed")
