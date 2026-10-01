import pandas as pd
data={"Subjects":["History","Music","Arts"],
      "Sub_id":[1,2,3]}
std={"Students":["Alex","Ben","Cavin"],"Sub_id":[1,2,3],"Grades":[97,87,77]}
dates={"Sub_id":[1,2,3],"testdate":["10-10-2026","11-10-2026","12-10-2026"]}
date_df=pd.DataFrame(dates)
#pd.DataFrame(data)
df = pd.DataFrame(data)
#print(df["Grades"].mean())
#print(df["Grades"].describe())
#print(df[df["Grades"]>88])
std_df=pd.DataFrame(std)
#print(std_df["Grades"].describe())
std_df["crt_score"]=std_df["Grades"] - 5
combined_df=pd.merge(df, std_df, on="Sub_id", how="right")
#print(combined_df)
#print(combined_df.loc[0,"Subjects"])
#print(combined_df.iloc[2,3])
date_df["testdate"]=pd.to_datetime(date_df["testdate"],dayfirst=True)
combine_df=pd.merge(combined_df,date_df, on="Sub_id", how="left")
combine_df["month"]=date_df["testdate"].dt.month
combine_df["month_name"]=date_df["testdate"].dt.month_name()
combine_df["day_name"]=date_df["testdate"].dt.day_name()
#print(combine_df.groupby("month_name")["Grades"].agg(["mean"]))
combine_df.to_csv("students_report.csv", index=False)