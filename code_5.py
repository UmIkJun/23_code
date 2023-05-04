print("#"* 23)
print("# 이름, 나이, 답변 앱 # ")
print("#"* 23)

you_name = str(input("이름: "))
you_age = int(input("나이: "))

if you_age <= 25:
    print("와우! 코딩 배우기 좋을 나이 입니다!")
else:
    print("포기하기엔 아직 늦지 않았어요.")
print('\n')