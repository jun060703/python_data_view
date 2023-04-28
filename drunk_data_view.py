#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./drunkdriving.csv',encoding='cp949')


x = df['시도']  # x축에 사용될 열 선택, 이름만 가능함
y = df['발생건수']  # y축에 사용될 열 선택


plt.bar(x, y)  # 그래프 그리기
plt.xlabel('시도')  #x축 제목
plt.ylabel('발생건수')  #Y축 메목
plt.title('음주운전 시도 별 최고 발생건수')  
plt.show() 


# In[ ]:




