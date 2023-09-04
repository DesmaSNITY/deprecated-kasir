from flask import Flask ,render_template ,url_for ,request
import koneksi








app = Flask(__name__)


    


@app.route('/')
def index():
    koneksi.mycursor.execute("SHOW TABLES;")    
    for x in koneksi.mycursor:
        return f"{x}"


    # desma = "hai kamu"
    # return render_template("belajar.html")

@app.route('/parahmen')
def hallo():
    return render_template("kocak.html")

@app.route('/databases-connection')
def databases(information):   
    return information

databases(koneksi.nyambung)
app.run(debug=True)