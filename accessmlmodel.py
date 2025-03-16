import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
#from productsearch import reslst
from datetime import date
from prosres import nextlst
from datetime import datetime
from holidays import IN as IndianHolidays

def predict_discount_price(input_data, model_path):
    """Loads a trained model and makes predictions on new data."""
    try:
        # Load the trained model 
        with open(model_path, 'rb') as file:
            model = pickle.load(file)

        # Ensure input_data is a DataFrame
        if not isinstance(input_data, pd.DataFrame):
            input_data = pd.DataFrame([input_data])  # Convert to DataFrame if it's a dictionary

        # Handle categorical features using the SAME LabelEncoders used during training
        # IMPORTANT: You MUST save the fitted LabelEncoders along with the model
        try:
            with open("label_encoders.pkl", 'rb') as f:
                label_encoders = pickle.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("label_encoders.pkl file not found. Make sure you saved it during training.")
        
        categorical_cols = input_data.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            if col in label_encoders:
                input_data[col] = label_encoders[col].transform(input_data[col])
            else:
                raise ValueError(f"Label encoder for column '{col}' not found. Ensure it was saved during training.")


        # Make predictions
        predictions = model.predict(input_data)
        return predictions

    except FileNotFoundError:
        apple = []
        for i in range(0,len(nextlst),2):
            apple.append(int(int(nextlst[i])*0.85))
        return apple
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    try:
        model_path = "randfor_model.pkl"  # Path to your saved model

        # Example with multiple rows of input data
        cur_date = date.today()
        in_holidays = IndianHolidays()
        #fest = cur_date.apply(lambda date_str: 1 if datetime.strptime(date_str, '%Y-%m-%d').date() in in_holidays else 0) #date format is assumed to be 'YYYY-MM-DD'
        fest = 0
        if cur_date in in_holidays:
            fest = 1
        

        input_data_multiple = pd.DataFrame([
            {'date': cur_date, 'name': 'Samsung Galaxy A35 5G', 'main_category': 'Electronics', 'sub_category': 'Mobile', 'ratings': 4.2, 'no_of_ratings': 500, 'festival': fest, 'no_of_purchases': 2012, 'actual_price': nextlst[0]},
            {'date': cur_date, 'name': 'Apple iPhone 15 Pro', 'main_category': 'Electronics', 'sub_category': 'Mobile', 'ratings': 4.8, 'no_of_ratings': 250, 'festival': fest, 'no_of_purchases': 1748, 'actual_price': nextlst[2]},
            {'date': cur_date, 'name': 'Samsung Galaxy M15 5G', 'main_category': 'Electronics', 'sub_category': 'Mobile', 'ratings': 4.5, 'no_of_ratings': 300, 'festival': fest, 'no_of_purchases': 2983, 'actual_price': nextlst[4]},
            {'date': cur_date, 'name': 'Samsung Galaxy S25 Ultra', 'main_category': 'Electronics', 'sub_category': 'Mobile', 'ratings': 3.7, 'no_of_ratings': 440, 'festival': fest, 'no_of_purchases': 785, 'actual_price': nextlst[6]},
            {'date': cur_date, 'name': 'OnePlus 12R', 'main_category': 'Electronics', 'sub_category': 'Mobile', 'ratings': 4.2, 'no_of_ratings': 380, 'festival': fest, 'no_of_purchases': 3672, 'actual_price': nextlst[8]},
            {'date': cur_date, 'name': 'Realme 11 Pro+ 5G', 'main_category': 'Electronics', 'sub_category': 'Mobile', 'ratings': 4.1, 'no_of_ratings': 390, 'festival': fest, 'no_of_purchases': 1207, 'actual_price': nextlst[10]},
            {'date': cur_date, 'name': 'iQOO Neo 7', 'main_category': 'Electronics', 'sub_category': 'Mobile', 'ratings': 4.5, 'no_of_ratings': 490, 'festival': fest, 'no_of_purchases': 2755, 'actual_price': nextlst[12]},
            {'date': cur_date, 'name': 'Redmi Note 13 Pro', 'main_category': 'Electronics', 'sub_category': 'Mobile', 'ratings': 3.9, 'no_of_ratings': 360, 'festival': fest, 'no_of_purchases': 4211, 'actual_price': nextlst[14]},
            {'date': cur_date, 'name': 'vivo v30 pro', 'main_category': 'Electronics', 'sub_category': 'Mobile', 'ratings': 4.4, 'no_of_ratings': 444, 'festival': fest, 'no_of_purchases': 2074, 'actual_price': nextlst[16]},
            {'date': cur_date, 'name': 'Nothing Phone 2', 'main_category': 'Electronics', 'sub_category': 'Mobile', 'ratings': 4.3, 'no_of_ratings': 420, 'festival': fest, 'no_of_purchases': 1807, 'actual_price': nextlst[18]}
        ])
        input_data_multiple['date'] = pd.to_datetime(input_data_multiple['date']).dt.strftime('%Y-%m-%d')
        predictions_multiple = predict_discount_price(input_data_multiple, model_path)
        return predictions_multiple

    except Exception as e:
        print(f"An error occurred in main: {e}")

if __name__ == "__main__":
    main()