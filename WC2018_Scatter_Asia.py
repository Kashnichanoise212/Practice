
# coding: utf-8



import pandas as pd
import plotly
import plotly.graph_objs as graph
plotly.offline.init_notebook_mode(connected=False)

#disc size: Average = 25, others = 15
def sizes(a):
    size = df["association"]==a
    lengs=size.sum()
    sizes=[]
    for i in range(lengs-1):
        sizes.append(15)
    sizes.append(25)
    return(sizes)

#reading the file
df = pd.read_csv("afc_Wc2018.csv")
df.drop(columns=["age", "birth date"],  inplace=True)
df.rename(columns={'age2': 'age'},inplace=True)

#opacity
Opacity = 0.7
#disc sizes
len_aus=sizes("AUS")
len_irn=sizes("IRN")
len_jpn=sizes("JPN")
len_kor=sizes("KOR")
len_ksa=sizes("KSA")

trace0 = graph.Scatter(x = df["age"][df['association'] == 'AUS'], y = df["height"][df['association'] == 'AUS'], mode = 'markers', text= df["name"][df['association'] == 'AUS'], name="AUS", marker=dict(size =len_aus, color="#FEC34F"), opacity=Opacity)
trace1 = graph.Scatter(x = df["age"][df['association'] == 'IRN'], y = df["height"][df['association'] == 'IRN'], mode = 'markers', text= df["name"][df['association'] == 'IRN'],name="IRN",  marker=dict(size =len_irn, color="#BE81F7"), opacity=Opacity)
trace2 = graph.Scatter(x = df["age"][df['association'] == 'JPN'], y = df["height"][df['association'] == 'JPN'], mode = 'markers', text= df["name"][df['association'] == 'JPN'], name="JPN", marker=dict(size =len_jpn, color="#295DF8"), opacity=Opacity)
trace3 = graph.Scatter(x = df["age"][df['association'] == 'KOR'], y = df["height"][df['association'] == 'KOR'], mode = 'markers', text= df["name"][df['association'] == 'KOR'], name="KOR", marker=dict(size =len_kor,color="#F0403C"), opacity=Opacity)
trace4 = graph.Scatter(x = df["age"][df['association'] == 'KSA'], y = df["height"][df['association'] == 'KSA'], mode = 'markers', text= df["name"][df['association'] == 'KSA'], name="KSA", marker=dict(size =len_ksa, color="#027D46"), opacity=Opacity)


layout = graph.Layout(
    width=960,
    height=540,
    xaxis = dict(title="age", range = [15,40], dtick=10),
    yaxis = dict(title="height", range = [160,200], dtick=10))


fig = dict(data = [trace0, trace1, trace2, trace3, trace4], layout = layout)



plotly.offline.plot(fig)

#for Jupyter notebook
#plotly.offline.iplot(fig)
