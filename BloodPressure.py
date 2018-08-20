def check_blood_pressure(syntolic,diastolic):
    if syntolic <= 90 and diastolic <= 60:
        return "Low"
    elif syntolic <= 120 and diastolic <= 80:
        return "Ideal"
    elif syntolic <= 140 and diastolic <= 90:
        return "Pre-high"
    elif syntolic <= 190 and diastolic <= 100:
        return "High"



test_systolic = 110
test_diastolic = 70

print(check_blood_pressure(test_systolic, test_diastolic))

