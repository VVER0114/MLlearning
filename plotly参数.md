# plotly 画图参数
> 抄网上的

## 常用
设置第一坐标轴画的条形图  
trace0 = go.Bar(  
y=count_unit_2018.index,  
x=count_unit_2018,  
1. 设置图形的颜色外观等  
marker=dict(color='#483D8B',#设置条形图的颜色  
line=dict(color='rgb(256, 256, 256)',width=1.0,)),#设置条形图边框  
name='总次数',#设置这个图的名字，和图例对应  
orientation='h',#如果水平条形图需设置，竖直条形图不用设置  
opacity=0.9)#条形图颜色的不透明度 
 
2. 设置第二坐标轴画的散点图  
trace1 = go.Scatter(  
y=count_unit_2018.index,  
x=round(count_unit_2018/130),  
text=round(count_unit_2018/130),#设置数值标签的值  
textposition='right center',#设置数值标签的位置  

3. 散点图特有的参数mode  
mode='text',#设置画图的种类，有'markers+text'、 mode='lines+markers+text',等各种组合  
textfont=dict(size=32,color='balck'),#设置标签的字体  
marker=dict(size=32,color='black',  
line=dict(width=1,color='black'),),  
name = '日均次数',  
xaxis='x2')#如果不是第二坐标轴不用设置，如果是纵向的图，设置成yaxis='y2'  
4. 组合所有图像展示的图  
data = [trace0,trace1]

5. 设置图层  
layout = go.Layout(  
plot_bgcolor='#E6E6FA',#图的背景颜色  
paper_bgcolor='#F8F8FF',#图像的背景颜色  
autosize=False,width=1450,height=800,#设置图像的大小  
6. 设置图离图像四周的边距  
margin=go.Margin(l=480,r=60,b=50,t=60,pad=0),#pad参数是刻度与标签的距离  
7. 设置y轴的刻度和标签  
yaxis=dict(title='人均会议申请次数',#设置坐标轴的标签  
titlefont=dict(color='rgb(148, 103, 189)',size=24),#设置坐标轴标签的字体及颜色  
tickfont=dict(color='rgb(148, 103, 189)',size = 24,),#设置刻度的字体大小及颜色  
showticklabels=False,#设置是否显示刻度  
8. 设置刻度的范围及刻度  
autorange=False,range=[-0.05674507980728292, -0.0527310420933204],type='linear',  
),

9. 设置x轴的刻度和标签  
xaxis=dict(title='人均会议申请次数',#设置坐标轴的标签  
titlefont=dict(color='rgb(148, 103, 189)',size=24),  
tickfont=dict(color='rgb(148, 103, 189)',size = 24,),  
tickangle=270,#设置刻度旋转的角度  
showticklabels=False,#设置是否显示坐标轴  

10. 设置刻度的范围及刻度  
autorange=False,range=[-0.05674507980728292, -0.0527310420933204],type='linear',  
),

10. 设置第二坐标轴,如果第二坐标轴是纵向，设置yaxis2  
xaxis2=dict(overlaying='x',#设置第二坐标轴的在的方向，如果第二坐标轴是纵向，设置为'y'  
side='top',#设置第二坐标轴的位置，或者是'bottom',如果第二坐标轴是纵向，设置为'right'或者'left'  
title='人均会议申请次数',#设置坐标轴的标签  
titlefont=dict(color='rgb(148, 103, 189)',size=24),  
tickfont=dict(color='rgb(148, 103, 189)',size = 24,),  
tickangle=270,#设置刻度旋转的角度  
showticklabels=False,#设置是否显示该坐标轴  
11. 设置刻度的范围及刻度  
autorange=False,range=[-0.05674507980728292, -0.0527310420933204],type='linear',  
),

12. 设置图例  
legend=dict(x=0.5,y=0.8,#设置图例的位置，[0,1]之间  
font=dict(family='sans-serif',size=26,color='black'),#设置图例的字体及颜色  
bgcolor='#E2E2E2',bordercolor='#FFFFFF'),#设置图例的背景及边框的颜色  
showlegend=False,#设置不显示图例  
annotations=[#注释可以是列表，也可以是单个字符串  
1. 设置注释1  
dict(x=2,y=5,  
xref='x',yref='y',  
text='dict Text',  
1. 设置注释的字体参数  
font=dict(family='Courier New, monospace',size=16,color='#ffffff'),  
showarrow=True,#设置显示箭头  
2. 设置箭头的参数  
ax=20,ay=-30,align='center',arrowhead=2,arrowsize=1,arrowwidth=2,arrowcolor='#636363',  
1. 设置注释的边框  
bordercolor='#c7c7c7',borderwidth=2,borderpad=4,bgcolor='#ff7f0e',opacity=0.8),  
1. 设置注释2  
dict(x=2,y=5,  
xref='x',yref='y',  
text='dict Text',  
1. 设置注释的字体参数  
font=dict(family='Courier New, monospace',size=16,color='#ffffff'),  
showarrow=True,#设置显示箭头  
1. 设置箭头的参数  
ax=20,ay=-30,align='center',arrowhead=2,arrowsize=1,arrowwidth=2,arrowcolor='#636363',  
1. 设置注释的边框  
bordercolor='#c7c7c7',borderwidth=2,borderpad=4,bgcolor='#ff7f0e',opacity=0.8)]

## 特殊

