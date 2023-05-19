import streamlit as st
import pickle 
print('Successfully executed')
model = pickle.load(open('model1.pkl','rb'))
def predict(gender, SeniorCitizen, Partner, Dependents, tenure,
        PhoneService, MultipleLines, InternetService, OnlineSecurity,
        OnlineBackup, DeviceProtection, TechSupport, StreamingTV,
        StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
        MonthlyCharges, TotalCharges):
    prediction = model.predict([[gender, SeniorCitizen, Partner, Dependents, tenure,
        PhoneService, MultipleLines, InternetService, OnlineSecurity,
        OnlineBackup, DeviceProtection, TechSupport, StreamingTV,
        StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
        MonthlyCharges, TotalCharges]])
    if prediction == 0:
        return 'No Churn'
    else:
        return 'Churn'
def main():
    st.title("Churn Prediction For Telecom")
    html_temp = """
    <div style="background-color:Black;padding:20px">
    <h2 style="color:white;text-align:center;">Streamlit Insurance Fraud Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    gender = st.radio(
         "Gender",
         [
         ('0','Male'),
          ("1",'Female')
         ]
     )
    Partner = st.radio(
         "Partner",
         [('0','Incase of no'),
         ('1','Incase of yes')]
     )
    SeniorCitizen = st.radio(
        "Senior Citizen",
        [
            ("1", "Yes"),
            ("0", "No")
        ]
    )
    Dependents = st.radio(
        "Dependents",
        [
            ('1','Incase of Yes'),
            ('0','Incase of No')
        ]

    )
    tenure = st.text_input('Tenure','Type here')
    OnlineBackup = st.radio(
        'Online Backup',
        [('0','No internet service'),
         ('1','No'),
         ('2','Yes')]
    )
    PhoneService = st.radio(
        "Phone Service",
        [
            ("1","Incase of Yes"),
            ("0","Incase of No")
            ]
    )
    MultipleLines = st.radio(
        "Multiple Lines",
        [
            ('0','No Phone service'),
            ('1','Incase of No'),
            ('2','Incase of Yes')
        ]
    )
    InternetService = st.radio(
        'Internet Service',
        [
            ('1','DSL'),
            ('0','No'),
            ('2','Fiber optic')]
    )
    OnlineSecurity = st.radio(
        'Online Security',
        [('0','No internet service'),
         ('1','No'),
         ('2','Yes')]
    )
    DeviceProtection = st.radio(
        "Device Protection",
        [
            ('0','No internet services'),
            ('1','No'),
            ('2','Yes')
        ]
    )
    TechSupport = st.radio(
        'Tech Support',
        [
        ('0','No internet services'),
        ('1','No'),
        ('2','Yes')   
        ]
    )
    StreamingTV = st.radio(
        'Streaming TV',
        [
            ('0','No internet services'),
            ('1','No'),
            ('2','Yes')
        ]
    )
    StreamingMovies = st.radio(
        'Streaming Movies',
        [
            ('0','No internet services'),
            ('1','No'),
            ('2','Yes')
        ]
    )
    Contract = st.radio(
        'Contract',
        [
            ('2','Two year'),('1','One year'),('0','Month-to-month'),
        ])
    PaperlessBilling = st.radio(
        'Paperless Billing',
        [
        ('0','Incase of no'),
         ('1','Incase of yes')
        ]
    )
    PaymentMethod = st.radio(
        'Payment Method',
        [('0','Credit card (automatic)'),
         ('1','Mailed check'),
         ('2','Electronic check'),
         ('3','Bank transfer (automatic)')
         ])
    
    MonthlyCharges = st.text_input('Monthly Charges','Type Here')
    TotalCharges = st.text_input('Total Charges','Type here')
    result = ""
    if st.button('Predict'):
        result = predict(gender[0], SeniorCitizen[0], Partner[0], Dependents[0], tenure[0],
        PhoneService[0], MultipleLines[0], InternetService[0], OnlineSecurity[0],
        OnlineBackup[0], DeviceProtection[0], TechSupport[0], StreamingTV[0],
        StreamingMovies[0], Contract[0], PaperlessBilling[0], PaymentMethod[0],
        MonthlyCharges[0], TotalCharges[0])
        st.success('You have{}'.format(result))
    if st.button("About"):
       st.text("Lets Detect Churn")
       st.text("Built with StreamLit")
       st.text("Created By Saish")     
main()
