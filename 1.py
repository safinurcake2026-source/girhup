def count_vowels_and_consonants(text: str) -> dict:

    x=[]
    for i in text:
        if i.isalpha():
            x.append(i)

    y=[]
    for j in x:
        if j in "aeiou":
            y.append(j)

    z=len(x)-len(y)
    print(f"unli harflar {len(y)}\n")
    print(f"undosh harflar {z}")

print(count_vowels_and_consonants("Salom Dunyo!"))