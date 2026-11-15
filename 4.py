import json

with open ("students.json", encoding="utf-8")as f:
    students=json.load(f)

    # 2. Eng yuqori baholi talaba
grade=[]
for student in students:
     grade.append(student['grade'])

m=max(grade)


for best in students:
    if m ==best['grade']:
        print(f"Eng yaxshi talaba: {best['name']} — {best['grade']}")

# 3. Eng past baholi talaba

n=min(grade)

for worst in students:
        if n==worst['grade']:
            print(f"Eng past baho: {worst['name']} — {worst['grade']}")


# 4. O'rtacha baho
average = sum(grade)/len(grade)
print(f"O'rtacha baho: {average}")

