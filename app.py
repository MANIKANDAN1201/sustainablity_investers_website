from flask import Flask,render_template
app=Flask(__name__)

# INVEST=[
#     {
#         "name":"go green",
#         "fund":"$100,000",
#         "stock_available":'10%'
#     },
#     {
#         "name":"life saver",
#         "fund":"$120,000",
#         "stock_available":'20%'
#     }
# ]
@app.route("/")
def demo():
  return render_template('index.html')

if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)