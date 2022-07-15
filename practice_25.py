# 가변 인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5): - 언어6번째가 생기면 복잡해 지므로 가변인자 사용
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5) 

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("송우기", 24, "python", "Java", "C", "C++", "C#","javaScript")
profile("조미연", 26, "kotlin", "swift")
