import streamlit as st
from health_predictor import health_prediction

if __name__=='__main__':
    st.set_page_config(page_title="Health Predictor")
    st.header("Health Predictor")
    st.write("**Find out if you are susceptible to Diabetes, Hypertension or Stroke**")
    
    age_cats = {'18-24':1,'25-29':2,'30-34':3,'35-39':4,'40-44':5,
                '45-49':6,'50-54':7,'55-59':8,'60-64':9,'65-69':10,
                '70-74':11,'75-79':12,'80 or older':13}
    yn = {"Yes":1,"No":0}
    
    with st.form("Inputs"):
        st.write("**Physical Details**")
        
        age_in = st.radio("Age",['18-24','25-29','30-34','35-39','40-44',
                              '45-49','50-54','55-59','60-64','65-69',
                              '70-74','75-79','80 or older'])
        age = age_cats[age_in]
        
        gender = st.radio("Gender",["Male","Female"])
        if gender == "Male":
            sex=1
        else:
            sex=0
        
        weight = st.number_input("Weight (kg): ",min_value=0,step=1,value=0)
        
        height = st.number_input("Height (m): ",min_value=0.0,step=0.01,value=1.60)
        
        st.markdown("""----------""")
        st.write("**Lifestyle Details**")
        
        chol = st.radio("Do you have high cholesterol?",["Yes","No"])
        highchol = yn[chol]
        
        cholch = st.radio("Have you had a cholesterol check in last 5 years?",["Yes","No"])
        cholcheck=yn[cholch]
        
        smoke = st.radio("Have you smoked at least 100 cigarettes in your entire life?",
                         ["Yes","No"])
        smoker=yn[smoke]
        
        heartdis = st.radio("Do you suffer from Coronary Heart Disease (CHD) or had an incident of Myocardial Infarction (MI - a heart attack)?",
                            ["Yes","No"])
        heartdiseaseorattack=yn[heartdis]
        
        physac = st.radio("Have you had any physical activity in the past 30 days (not including job)?",
                          ["Yes","No"])
        physactivity = yn[physac]
        
        fruit = st.radio("Do you consume fruit one or more times a day?",
                         ["Yes","No"])
        fruits = yn[fruit]
        
        veg = st.radio("Do you consume vegetables one or more times per day?",
                       ["Yes","No"])
        veggies = yn[veg]
        
        drink = st.radio("Adult male: Do you drink more than 14 drinks a week?  Adult female: Do you drink more than 7 drinks a week?",
                         ["Yes","No"])
        hvyalcoholconsump = yn[drink]
        
        genh = st.radio("What do you think your general health is?",
                        ["Excellent","Very good","Good","Fair","Poor"])
        gh_vals = {"Excellent":1,"Very good":2,"Good":3,"Fair":4,"Poor":5}
        genhlth = gh_vals[genh]
        
        menthlth = st.slider("How many days of poor mental health have you had in past 30 days",
                         min_value=0,max_value=30,step=1,value=3)
        
        physhlth = st.slider("How many days of physical injury or illness have you had in past 30 days",
                         min_value=0,max_value=30,step=1,value=5)
        
        diffw = st.radio("Do you have serious difficulty walking or climbing stairs?",
                         ["Yes","No"])
        diffwalk = yn[diffw]
        
        submit_form = st.form_submit_button("Submit")
    
    if submit_form:
        bmi = weight/height/height
        col_vals = [age,sex,highchol,cholcheck,bmi,smoker, heartdiseaseorattack, 
                    physactivity, fruits, veggies, hvyalcoholconsump, genhlth,
                    menthlth, physhlth, diffwalk]
        
        dia,hyp,stk = health_prediction(col_vals=col_vals)
        
        st.write("**Susceptibility**")
        st.write("Diabetes: **{}**".format(dia))
        st.write("Hypertension: **{}**".format(hyp))
        st.write("Stroke: **{}**".format(stk))
        
        if (dia=='No')&(hyp=='No')&(stk=='No'):
            st.write("Congratulations! You are in good health. Continue what you're doing.") 
        else:
            st.write("Better cut those carbs and sweets and savories, hit the treadmill, and lay off those beers and cigarettes.")
        st.markdown("----")
        st.markdown("""This health predictor was built by training machine learning models on this dataset from [kaggle](https://www.kaggle.com/datasets/prosperchuks/health-dataset).
                    Look at the source code [here](https://github.com/spikspiks/health_predictor).""")