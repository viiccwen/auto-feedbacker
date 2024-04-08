import pandas as pd
import numpy as np
from pathlib import Path
from test import ShowFeedbackMean, ShowGroupData

path = ""
input_file = ""
output_file = ""
MODE = ""
feedback_group_name = ""
feedback_point_name = "" 
group = []

def ReadConfig():
    f = open("config.txt", "r")
    
    for line in f.readlines():
        s = line.split("=")

        if s[0] == "path":
            global path
            path = s[1].strip()
        elif s[0] == "input_file":
            global input_file
            input_file = s[1].strip()
        elif s[0] == "output_file":
            global output_file
            output_file = s[1].strip()
        elif s[0] == "mode":
            global MODE
            MODE = s[1].strip()
        elif s[0] == "feedback_group_name":
            global feedback_group_name
            feedback_group_name = s[1].strip()
        elif s[0] == "feedback_point_name":
            global feedback_point_name
            feedback_point_name = s[1].strip()
            
    f.close()

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
    ReadConfig()
    
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