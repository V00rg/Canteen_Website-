from flask import Flask , jsonify , request , render_template

app = Flask(__name__)

#menu = {"Poha" : 30 ,"Tea " : 15 , "Sandwich" : 50 }

@app.route("/")
@app.route("/menu")
def get_menu(): 
    return render_template("index.html")

@app.route("/order",methods = ["POST"])
def place_order () : 
    order = request.get_json()
    item = order["items"]
    qty = order["quantity"]
    total = menu[item ]*qty
    return jsonify ({
        "order_id": 101, 
        "total ": total 
        
    })
app.run(host="0.0.0.0" , port = 5001)