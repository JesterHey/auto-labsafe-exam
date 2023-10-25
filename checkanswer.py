
import csv

def find_matching_values( value_to_match,filename='quzibase.csv'):
    results = []
    value_to_match = value_to_match.split('、')[-1]
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        # 如果CSV文件有标题行，使用下面的语句跳过它
        #next(reader)
        for row in reader:
            if row[0] == value_to_match:
                results.append(row[1])
    return results

# 测试
filename = 'quzibase.csv'  # 替换为你的CSV文件名
value_to_match = '凡涉及有害或有刺激性气体的实验应在通风柜内进行。'   # 替换为你想匹配的值
print(find_matching_values(filename, value_to_match))
