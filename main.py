import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro


# ---- Funzioni statistiche ----
def average(data):
    return np.mean(data)

def std(data):
    return np.std(data)

def median(data):
    return np.median(data)

def IQR(data):
    q1, q2, q3 = data.quantile([0.25, 0.5, 0.75])
    return q3 - q1


# ---- Funzioni per outlier ----
def outliers_std(name, data, avg, std_val):
    print(f"{name} - metodo STD")
    return np.array(data[np.abs(data - avg) > 1.5 * std_val])

def outliers_iqr(name, data, med, iqr_val):
    print(f"{name} - metodo IQR")
    return np.array(data[np.abs(data - med) > 1.5 * iqr_val])


# ---- Test di normalità ----
def check_distribution(name, data, avg, std_val, med, iqr_val):
    stat, p = shapiro(data)

    # Se p-value > 0.05 i dati sono considerati normali
    if p > 0.05:
        print(f"{name}: distribuzione normale")
        print("Outlier con deviazione standard:")
        print(outliers_std(name, data, avg, std_val))
    else:
        print(f"{name}: distribuzione NON normale")
        print("Outlier con IQR:")
        print(outliers_iqr(name, data, med, iqr_val))


# ---- Funzione per analizzare una colonna ----
def analyze_column(df, column_name):
    data = df[column_name].dropna()

    print(f"\n----- {column_name} -----")

    avg = average(data)
    std_val = std(data)
    med = median(data)
    iqr_val = IQR(data)

    print(f"avg: {avg}")
    print(f"std: {std_val}")
    print(f"median: {med}")
    print(f"iqr: {iqr_val}")

    return data, avg, std_val, med, iqr_val


# ---- MAIN ----
if __name__ == "__main__":
    df = pd.read_csv("./traffico16.csv")

    month1 = 'ago1'
    month2 = 'ago2'

    # Analisi delle due colonne
    data1, avg1, std1, med1, iqr1 = analyze_column(df, month1)
    data2, avg2, std2, med2, iqr2 = analyze_column(df, month2)

    print("\n----- Outliers (entrambi i metodi) -----")

    print(outliers_std(month1, data1, avg1, std1))
    print(outliers_iqr(month1, data1, med1, iqr1))

    print(outliers_std(month2, data2, avg2, std2))
    print(outliers_iqr(month2, data2, med2, iqr2))

    # Boxplot per i mesi ago1 e ago2
    plt.figure()
    plt.title(f"Boxplot per mesi {month1} e {month2}")
    df[[month1, month2]].boxplot()

    print("\n----- Test di normalità -----")

    check_distribution(month1, data1, avg1, std1, med1, iqr1)
    print("")
    check_distribution(month2, data2, avg2, std2, med2, iqr2)

    plt.show()