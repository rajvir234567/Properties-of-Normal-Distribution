import plotly.figure_factory as ff
import pandas as pd
import statistics as stat
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

mean = stat.mean(df["maths score"].tolist())
print(mean)
mode = stat.mode(df["maths score"].tolist())
print(mode)
median = stat.median(df["maths score"].tolist())
print(median)

sd = stat.stdev(df["maths score"].tolist())
print(sd)

sd1_start,sd1_end = mean - sd, mean + sd
sd2_start,sd2_end = mean - 2*sd, mean + 2*sd
sd3_start,sd3_end = mean - 3*sd, mean + 3*sd

graph = ff.create_distplot([df["maths score"].tolist()], ["scores in maths"], show_hist = False)
graph.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "mean"))

graph.add_trace(go.Scatter(x = [sd1_start,sd1_start], y = [0,0.17], mode = "lines", name = " 1st sd"))
graph.add_trace(go.Scatter(x = [sd1_end,sd1_end], y = [0,0.17], mode = "lines", name = " 1st sd"))

graph.add_trace(go.Scatter(x = [sd2_start,sd2_start], y = [0,0.17], mode = "lines", name = " 2nd sd"))
graph.add_trace(go.Scatter(x = [sd2_end,sd2_end], y = [0,0.17], mode = "lines", name = " 2nd sd"))

graph.add_trace(go.Scatter(x = [sd3_start,sd3_start], y = [0,0.17], mode = "lines", name = " 3rd sd"))
graph.add_trace(go.Scatter(x = [sd3_end,sd3_end], y = [0,0.17], mode = "lines", name = " 3rd sd"))
graph.show()