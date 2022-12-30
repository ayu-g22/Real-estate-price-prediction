from flask import Flask,request,jsonify,render_template
import utils
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello"

@app.route('/get_location_name',methods=['GET'])
def get_location():
    response = jsonify({
        'locations': utils.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/prediction',methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['BHK'])
    bath = int(request.form['bath'])
    response = jsonify({
        'estimated_price': utils.get_predicted_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Flask server")
    utils.get_artifacts()
    app.run()