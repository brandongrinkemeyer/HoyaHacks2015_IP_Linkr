import plotly.plotly as py
import plotly.graph_objs as go
from flask import Flask
from flask.templating import render_template
from plotly.tools import FigureFactory as FF
import plotly
import re
app = Flask(__name__)
plotly.tools.set_credentials_file(username='bgrinkem', api_key='o36xptvygo')
 
 
file = "NMAP.txt"
stream = open(file, "r")
 
macs= []
ips= []
manufacturers= []
for brandon in stream:
    if "MAC" in brandon:
        macs.append(brandon[22:31])
        manufacturers.append(brandon[32:len(brandon)-2])
    if "Nmap scan" in brandon:
        ips.append(brandon[15:len(brandon)-1])
num_lines = sum(1 for line in open('NMAP1.txt'))
file1 = open('NMAP1.txt', 'r')
x = [] 
y = []
for q in xrange(num_lines/2-1):
    x.append(file1.readline())
    y.append((int)(file1.readline()))
trace = go.Scatter(
    x = x,
    y = y
)
data = [trace]
py.plot(data, filename='basic-line', auto_open=False)
 
data_matrix = [['Manufacturer', 'IP Address', 'MAC Address'],
               ]
p = 0
for x in macs:
    data_matrix.append([manufacturers[p], ips[p], macs[p]])
    p += 1
table = FF.create_table(data_matrix)
py.plot(table, filename='simple_table', auto_open=False)
@app.route('/')
def index():
    return 'BG'

if __name__ == '__main__':
    app.run(host='0.0.0.0')