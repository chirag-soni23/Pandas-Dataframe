import pandas as pd
# create data frame
student_data=[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
def createDataframe(student_data:list[list[int]])->pd.DataFrame:
    return pd.DataFrame(student_data,columns=["student_id","age"])
print(createDataframe(student_data))
    
    
    