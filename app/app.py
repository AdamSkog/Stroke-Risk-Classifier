import streamlit as st
import pandas as pd
import joblib


model = joblib.load('app/pipelines/lr_pipeline.pkl')


def main():
    st.title('Stroke Prediction App')

    # User inputs
    st.sidebar.header('User Input:')
    age = st.sidebar.slider('Age', 0, 100, 45)
    hypertension = st.sidebar.checkbox('Hypertension')
    heart_disease = st.sidebar.checkbox('Heart Disease')
    avg_glucose_level = st.sidebar.slider('Average Glucose Level', 0.0,
                                          300.0, 85.0)
    bmi = st.sidebar.slider('BMI', 0.0, 100.0, 28.5)
    sex = st.sidebar.selectbox('Sex', ['Male', 'Female'])
    marriage_status = st.sidebar.checkbox('Ever Married?')
    employment = st.sidebar.selectbox(
        'Employment', ['Private', 'Self-employed',
                       'Government Job', 'Child Care', 'Never Worked']
    )
    residency = st.sidebar.selectbox('Residency', ['Urban', 'Rural'])
    smoker = st.sidebar.selectbox(
        'Smoker', ['Formerly Smoked', 'Never Smoked', 'Smokes', 'Unknown']
    )

    match employment:
        case 'Government Job':
            employment = 'govt_job'
        case 'Child Care':
            employment = 'children'
        case 'Never Worked':
            employment = 'never_worked'

    if st.button('Predict'):
        # Prepare user input data as a DataFrame
        user_data = pd.DataFrame({
            'age': [age],
            'hypertension': [1 if hypertension else 0],
            'heart_disease': [1 if heart_disease else 0],
            'avg_glucose_level': [avg_glucose_level],
            'bmi': [bmi],
            'gender': [sex.lower()],
            'ever_married': ['yes' if marriage_status else 'no'],
            'work_type': [employment.lower()],
            'residence_type': [residency.lower()],
            'smoking_status': [smoker.lower()]
        }, index=[0])

        # Use the model to make predictions
        prediction = model.predict(user_data)

        # Display the prediction result
        if prediction[0] == 1:
            st.error('Prediction: High Risk of Stroke')
        else:
            st.success('Prediction: Low Risk of Stroke')
    st.sidebar.info(
        'Adjust the input values and click "Predict" to see the prediction.'
    )


if __name__ == "__main__":
    main()
