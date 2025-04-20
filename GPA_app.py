from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

@app.route("/predict_gpa", methods=["POST"])
def predict():
    request_data = request.get_json()
    
    with open('GPA_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    input_features = list(request_data.values())
    res = model.predict([input_features])[0]

    # Convert numpy float to Python float
    res = float(res)
    
    return jsonify({"predicted_gpa": res})

if __name__ == "__main__":
    app.run(debug=True)
