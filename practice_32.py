# with

# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file)) # 이러면 따로 종료하지 않아도 with문을 탈출하면서 자동으로 종료해줌

# with open("study.txt", "w", encoding="utf8")as study_file:
#     study_file.write("파이썬을 공부하고 있어요") # with 이용해서 파일 쓰는것

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read()) # with 이용해서 파일 읽는 것, 매번 close 할 필요가 없어서 수월함

