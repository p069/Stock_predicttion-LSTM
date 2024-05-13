from flask import Flask, render_template, request
import pickle

# Import your ML model here

app = Flask(__name__)

model=pickle.load(open('model.pkl' , 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        # Get input data from the form
        stock_symbol = request.form['stock_symbol']
        # You may have more input fields depending on your model

        # Call your ML model to get prediction
        prediction = model.predict(stock_symbol)
        
        # Render prediction template with the result
        return render_template('prediction.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
