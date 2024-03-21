import pandas as pd
import numpy as np
from test import ShowFeedbackMean, ShowGroupData

# Change to your path, if you change the path to somewhere.
path = "<your whole path>"
input_file = "feedback.xlsx"
output_file = "output.xlsx"

# important: you MUST indicate the mode !!!!
MODE = "inter" # SDGs or inter

# The column's name of The Group that you feedback.
feedback_group_name = "feedback group"

# score<x>  ex. score1, score2, score3, ...
feedback_point_name = "score" 

# The list of group.
group = []

def ReadFile():
    data = pd.read_excel(f"{path}\\{input_file}")
    return data

def RemoveGroup(data, mod):
    if mod == "SDGs":
        data[feedback_group_name] = data[feedback_group_name].astype(str)
        data[feedback_group_name] = data[feedback_group_name].str.extract("([0-9])")
        data[feedback_group_name] = data[feedback_group_name].astype(int)
    elif mod == "inter":
        data[feedback_group_name] = data[feedback_group_name].str.extract("(?<![a-zA-Z0-9])([A-Z]+\\W*[0-9]+)")
        data[feedback_group_name] = data[feedback_group_name].str.replace("-", "")
    
    return data
        
def GetFeedbackMean(data, limit):
    return [data[f'score{i}'].mean() for i in range(1, limit)]

def GetGroupData(data, limit):
    return [data.get_group(i) for i in range(1, limit)]

def GetGroupList(data):
    return data.groups.keys()

def GetGroupFeedback(data, list):
    feedback_array = []
    for group in list:
        tmp_str = ""
        a = data.get_group(group)["feedback"].to_list()
        for j in a:
            if pd.isna(j) == False:
                tmp_str += str(j) + "\n"
            
        feedback_array.append(tmp_str)
        
    return feedback_array

def GetAverageList(data, group):
    aver_array = [0 for i in group]
    div = len(data)
    
    for ele in data:
        i = 0
        for i, name in enumerate(group):
            aver_array[i] += ele[name]
    
    aver_array = [round(float(ele / div) * 20, 2) for ele in aver_array]
        
    return aver_array
            
def OutputFile(data):
    data.to_excel(f"{path}\\{output_file}", index=False)
    
if __name__ == '__main__':
    data = ReadFile()
    
    # let the dataframe groupby
    data = RemoveGroup(data, mod=MODE)
    data = data.groupby(feedback_group_name)
    
    # get the list of group
    group = GetGroupList(data)
    
    # get the mean value of each group
    mean_data = GetFeedbackMean(data, 5)
    
    # get the average value of each group
    average_data = GetAverageList(mean_data, group)
    
    # let the feedback to a group
    feedback_array = GetGroupFeedback(data, group)
    
    # create the dataframe and modify the format
    output_data = pd.DataFrame(mean_data)
    output_data = output_data.transpose()
    output_data.insert(0, column="Group", value=[row for row in group])
    output_data["average"] = average_data
    output_data["feedback"] = feedback_array
    print(output_data)
    
    #output file
    OutputFile(output_data)