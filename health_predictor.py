import pandas as pd
import catboost
import lightgbm
import pickle

def health_prediction(col_vals):
    
    col_names = ['Age','Sex','HighChol','CholCheck','BMI',
            'Smoker','HeartDiseaseorAttack','PhysActivity',
            'Fruits','Veggies','HvyAlcoholConsump',
            'GenHlth','MentHlth','PhysHlth','DiffWalk']
    input_df = pd.DataFrame([col_vals],columns=col_names)
    
    diabetes = pickle.load(open('model_dia.pkl','rb'))
    hypertension = pickle.load(open('model_hyp.pkl','rb'))
    stroke = pickle.load(open('model_str.pkl','rb'))
    
    y_dia = diabetes.predict(input_df)
    y_hyp = hypertension.predict(input_df)
    y_str = stroke.predict(input_df)
    
    yn = {1.0:"Yes",0.0:"No"}
    
    return yn[y_dia[0]],yn[y_hyp[0]],yn[y_str[0]]