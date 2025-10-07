# from flask import Flask, request, render_template
# import numpy as np
# import pandas as pd
# from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# application = Flask(__name__)
# app = application


# # Route to Home Page
# @app.route('/')
# def index():
#     return render_template('index.html')


# # Route to Car Price Prediction Form
# @app.route('/predictdata', methods=['GET', 'POST'])
# def predict_datapoint():
#     if request.method == 'GET':
#         return render_template('home.html')
#     else:
#         # Collecting form data
#         data = CustomData(
#             brand=request.form.get('brand'),
#             model=request.form.get('model'),
#             vehicle_age=int(request.form.get('vehicle_age')),
#             km_driven=int(request.form.get('km_driven')),
#             seller_type=request.form.get('seller_type'),
#             fuel_type=request.form.get('fuel_type'),
#             transmission_type=request.form.get('transmission_type'),
#             mileage=float(request.form.get('mileage')),
#             engine=int(request.form.get('engine')),
#             max_power=float(request.form.get('max_power')),
#             seats=int(request.form.get('seats'))
#         )

#         # Convert to DataFrame
#         pred_df = data.get_data_as_data_frame()
#         print("Input DataFrame:")
#         print(pred_df)

#         # Prediction pipeline
#         predict_pipeline = PredictPipeline()
#         print("Performing Prediction...")
#         results = predict_pipeline.predict(pred_df)
#         print("Prediction Complete")

#         # Round result for cleaner display (optional)
#         predicted_price = round(float(results[0]), 2)

#         return render_template('result.html', results=predicted_price)


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True)


from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Validate numeric inputs
            vehicle_age = int(request.form.get('vehicle_age', 0))
            km_driven = int(request.form.get('km_driven', 0))
            mileage = float(request.form.get('mileage', 0))
            engine = int(request.form.get('engine', 0))
            max_power = float(request.form.get('max_power', 0))
            seats = int(request.form.get('seats', 0))

            data = CustomData(
                brand=request.form.get('brand'),
                model=request.form.get('model'),
                vehicle_age=vehicle_age,
                km_driven=km_driven,
                seller_type=request.form.get('seller_type'),
                fuel_type=request.form.get('fuel_type'),
                transmission_type=request.form.get('transmission_type'),
                mileage=mileage,
                engine=engine,
                max_power=max_power,
                seats=seats
            )

            pred_df = data.get_data_as_data_frame()
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            predicted_price = round(float(results[0]), 2)

            return render_template('result.html', results=predicted_price)
        except Exception as e:
            return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
