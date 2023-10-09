total = int(input())
sx, s1 = set(), set()
for _ in range(total):
    n = int(input())
    student_languages = set()
    for _ in range(n):
        l = input()
        student_languages.add(l) 
    if not sx:
        sx = student_languages.copy()
        s1 = student_languages.copy()
    else:
        sx &= student_languages
        s1 |= student_languages

sx = sorted(sx)
s1 = sorted(s1)
print(len(sx))
for l in sx:
    print(l)

print(len(s1))
for l in s1:
    print(l)