
import random

def generate_vitals():
    heart_rate = random.randint(60, 100)
    breaths_per_minute = random.randint(12, 20)
    systolic_bp = random.randint(110, 140)
    diastolic_bp = random.randint(70, 90)
    spo2 = random.randint(95, 100)
    temperature = round(random.uniform(97.0, 99.0), 1)
    return {
        "heart_rate": heart_rate,
        "breaths_per_minute": breaths_per_minute,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "spo2": spo2,
        "temperature": temperature
    }

if __name__ == '__main__':
    print(generate_vitals())
