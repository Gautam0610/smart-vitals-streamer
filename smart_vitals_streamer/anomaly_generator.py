import random

def inject_anomalies(vitals):
    if random.random() < 0.05:  # 5% chance of anomaly
        if random.random() < 0.5:
            # Extreme heart rate
            vitals["heart_rate"] = random.randint(150, 220)  # Tachycardia
        else:
            # Extreme breaths per minute
            vitals["breaths_per_minute"] = random.randint(30, 50)  # Tachypnea
    return vitals

if __name__ == '__main__':
    # Example usage
    sample_vitals = {"heart_rate": 75, "breaths_per_minute": 15}
    anomalous_vitals = inject_anomalies(sample_vitals)
    print(anomalous_vitals)