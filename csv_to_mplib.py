import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("students_report.csv")
plt.bar(df["Students"],df["Grades"])
plt.title("Students report")
plt.xlabel("Students")
plt.ylabel("Grades")
plt.show()