
# coding: utf-8


import plotly
plotly.offline.init_notebook_mode(connected=False)
import plotly.graph_objs as graph
import pandas as pd

# Reading CSV
df = pd.read_csv("AFC_WC2018_Players_Data_2nd.csv")


#df1:  Average
df1 = df[df["name"]=="AVERAGE"]
df1= df1.drop(columns=["age", "num", "min"])
df1 = df1.rename(columns={'age2': 'age'})


coloring=("#feca04", "#BE81F7", "#020372", "#F0403C",  "#0B4E2F")
naming=("AUS", "IRN", "JPN", "KOR",  "KSA")

#Graph - Average Data  
trace_0= graph.Scatter(x = df1["age"], y = df1["height"], mode = 'markers', name="Average", text= naming, marker=dict(size =30, color=coloring), opacity=0.9)
trace_1= graph.Scatter(x = df1["Ave. A w/o GK"], y = df1["Ave. H w/o GK"], mode = 'markers', name="Average_without Goal keepers", text= naming, marker=dict(size =30, color=coloring), opacity=0.75)
trace_2= graph.Scatter(x = df1["Ave. A w/o 0min"], y = df1["Ave. H w/o 0min"], mode = 'markers', name="Average_without no-playing(0min) players", text= naming, marker=dict(size =30, color=coloring), opacity=0.6)
trace_3= graph.Scatter(x = df1["Ave. A w/o GK&0min"], y = df1["Ave. H w/o GK&0min"], mode = 'markers', name="Average_without Goal keepers & no-playing(0min) players", text= naming, marker=dict(size =30, color=coloring), opacity=0.45)
trace_4= graph.Scatter(x = df1["weighted age by min"], y = df1["weighted height by min"], mode = 'markers', name="Average_weighted by playing minutes", text= naming, marker=dict(size =30, color=coloring), opacity=0.3)

layout1 = graph.Layout( width=1200, height=450*1.5, xaxis = dict(title="age", range = [25,30], dtick=1), yaxis = dict(title="height", range = [170,190], dtick=5))

fig1=dict(data = [trace_0, trace_1, trace_2, trace_3, trace_4], layout = layout1)

plotly.offline.plot(fig1)




#df2: Players Data
df2 = df[df["name"]!="AVERAGE"]
df2 = df2.dropna(how='all')
df2 = df2.dropna(how='all',  axis=1)
df2 = df2.dropna(how='any')
df2 = df2.drop(columns=["age", "weighted height by min", "weighted age by min"])
df2 = df2.rename(columns={'age2': 'age'})

# Function: marker size. Depend on playing minutes(0min: 5)
def sizes(a):
    sizes=[]
    maxi = df2["min"][df2["association"]==a].max()
    for m in df2["min"][df2["association"]==a]:
        s = (m/maxi*20)+5
        sizes.append(s)
    return(sizes)


len_aus=sizes("AUS")
len_irn=sizes("IRN")
len_jpn=sizes("JPN")
len_kor=sizes("KOR")
len_ksa=sizes("KSA")

Opa = 0.7

# Graph
trace_aus = graph.Scatter(x = df2["age"][df2['association'] == 'AUS'], y = df2["height"][df2['association'] == 'AUS'], mode = 'markers', text= df2["name"][df2['association'] == 'AUS'], name="AUS", marker=dict(size =len_aus, color="#feca04"), opacity=Opa) 
trace_irn = graph.Scatter(x = df2["age"][df2['association'] == 'IRN'], y = df2["height"][df2['association'] == 'IRN'], mode = 'markers', text= df2["name"][df2['association'] == 'IRN'],name="IRN",  marker=dict(size =len_irn, color="#BE81F7"), opacity=Opa) 
trace_jpn = graph.Scatter(x = df2["age"][df2['association'] == 'JPN'], y = df2["height"][df2['association'] == 'JPN'], mode = 'markers', text= df2["name"][df2['association'] == 'JPN'], name="JPN", marker=dict(size =len_jpn, color="#295DF8"), opacity=Opa) 
trace_kor = graph.Scatter(x = df2["age"][df2['association'] == 'KOR'], y = df2["height"][df2['association'] == 'KOR'], mode = 'markers', text= df2["name"][df2['association'] == 'KOR'], name="KOR", marker=dict(size =len_kor,color="#F0403C"), opacity=Opa) 
trace_ksa = graph.Scatter(x = df2["age"][df2['association'] == 'KSA'], y = df2["height"][df2['association'] == 'KSA'], mode = 'markers', text= df2["name"][df2['association'] == 'KSA'], name="KSA", marker=dict(size =len_ksa, color="#027D46"), opacity=Opa)

layout2 = graph.Layout( width=1200, height=450*1.5, xaxis = dict(title="age", range = [15,40], dtick=5), yaxis = dict(title="height", range = [160,200], dtick=5))


fig2 = dict(data = [trace_aus, trace_irn, trace_jpn, trace_kor, trace_ksa], layout = layout2)

plotly.offline.plot(fig2, filename="temp-plot2.html")



