
def ShowFeedbackMean(data, limit):
    for i in range(1, limit):
        print(data[f'score{i}'].mean())

def ShowGroupData(data, list):
    for group in list:
        print(data.get_group(group))