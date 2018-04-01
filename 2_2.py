import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

print(input_file)
print(output_file)

data_frame = pd.read_csv(input_file)
print(data_frame)
# data_frame.to_csv(output_file, index=false)

# 한글은 못읽는 문제 발생함.