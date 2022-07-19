# pickle - 프로그램에서 사용하는 데이터를 파일 형태로 저장해줌
import pickle
# profile_file = open("profile.pickle", "wb") #쓰기목적 w , b 바이널리 pickle에서는 항상 바이널리 타입 정의해주어야함, 따로 인코딩 설정 안해도 됨
# profile = {"이름":"송우기", "나이":24, "취미":["노래", "춤", "작곡"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
# profile_file.close() 

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()