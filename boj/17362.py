n = int(input())

finger = [1, 2, 3, 4, 5, 4, 3, 2]
finger_answer = n % 8
print(finger[finger_answer - 1])