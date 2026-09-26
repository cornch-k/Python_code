grade_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F':0.0}

subject_list = list()
# 과목 명 담기.

score_list = list()

grade_list = list()
# 학점 담을거임.

# sum(grade_list) / len(subject_list) 로 학점 구하기

for i in range(20):
    subject, score, grade = map(str, input().split())
    subject_list.append(subject)
    if grade == 'P':
        pass
    else:
        score_list.append(float(score))
        grade_list.append(float(score) * grade_dict[grade])

total_score = sum(grade_list) / sum(score_list)
print(total_score)