#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./drunkdriving.csv',encoding='cp949')


x = df['시도']  # x축에 사용될 열 선택
y = df['발생건수']  # y축에 사용될 열 선택


plt.bar(x, y)  # 그래프 그리기
plt.xlabel('시도')  # x축 레이블 설정
plt.ylabel('발생건수')  # y축 레이블 설정
plt.title('음주운전 시도 별 최고 발생건수')  # 그래프 제목 설정
plt.show()  # 그래프 보여주기


# In[ ]:




