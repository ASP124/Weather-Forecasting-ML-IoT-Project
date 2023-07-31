import pickle
from flask import Flask, request, render_template
import pandas

temperature = pickle.load(open('temperaturepred.pkl','rb'))
humidity = pickle.load(open('humiditypred.pkl', 'rb'))
pressure = pickle.load(open('pressurepred.pkl','rb'))

temp_html = temperature.to_html(classes='table', index=False)
humidity_html = humidity.to_html(classes='table', index=False)
pressure_html = pressure.to_html(classes='table', index=False)



app = Flask(__name__)

@app.route('/')
def index():
    with open('templates/output1.html', 'w') as f:
        f.write("""
        <!DOCTYPE html>
<html>

<head>
  <!--<link rel="stylesheet" type="text/css" href="styles.css"> -->
  <style>
    body {
      background-image: url('image1.jpg');
    }

    .table {
      width: 100%;
      border-collapse: collapse;
      max-width: 750px;
      margin: 0px auto;
    }

    .table th {
      background-color: black;
      color: aqua;
      font-weight: 200;
      padding: 10px;

    }

    .table td {
      background-color: lavender;
      color: black;
      border: 2px solid;
      padding: 10px;
    }

    #table1 {
      margin: 20px;
      font-size: 20px;
    }

    #table2 {
      margin: 20px;
      font-size: 20px;
    }

    #table3 {
      margin: 20px;
      font-size: 20px;
    }
  </style>
</head>

<body>

  <div class="container" style="display: flex;
  justify-content: center;
  margin: 40px 0;">
    <img src="image1.jpg" alt="">
        """)
        f.write(temp_html)
        f.write(humidity_html)
        f.write(pressure_html)
        f.write("""
  </div>
</body>


</html>""")
    # generate HTML table
    return render_template('output1.html')


if __name__ == '__main__':
    app.run(debug=True)