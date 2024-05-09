from flask import Flask, jsonify,render_template
app=Flask(__name__)

INVEST=[
    {
        "name":"go green",
        "fund":"$100,000",
        "stock_available":'10%'
    },
    {
        "name":"life saver",
        "fund":"$120,000",
        "stock_available":'20%'
    }
]
@app.route("/")
def demo():
  return render_template('home.html',invest=INVEST,name="ChangeForge")
@app.route("/api/invest")
def list_invest():
  return jsonify(INVEST)
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)