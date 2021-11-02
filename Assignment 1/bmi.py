height, weight = map(int, input().split(","))
bmi = weight / (height*height/100)
bmi = bmi*100
bmi = round(bmi, 1)
# print(bmi)


if bmi >= 18.5 and bmi <=24.9:
    print("Score is "+str(bmi)+". You are Normal")
elif bmi >= 25 and bmi <=30:
    print("Score is "+str(bmi)+". You are Overweight")
elif bmi > 30:
    print("Score is "+str(bmi)+". You are Obese")