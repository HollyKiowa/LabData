# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 12:54:48 2023

@author: alexa
"""


import streamlit as st
import json


       
# Define Streamlit app
def app():
    with open ('sample_HB.json') as HB:
        normal_rangesHB=json.load(HB)
        
    with open('sample_LC.json') as LC:
        normal_rangesLC=json.load(LC)
           
    
    st.title('LabData')
    st.write(":red[**Important Notice:**] The information provided in this app is for educational purposes only",
             " and should not be considered medical advice. This app is not intended to replace a doctor's visit.",
             " Always consult a healthcare professional for any concerns or questions regarding your health.")
    
    
    # Get user input for age, sex, and value to compare
    input_Blood= st.radio('Choose what Blood value you are interessted it:', ('Hemoglobin', 'Leukocytes/WBC'))
    sex = st.radio('Choose your biological sex:',('Male','Female'))
    #input_extra= st.selectbox('Choose additional Information:', ('None','Pregnant', 'Diabetes'))
    age = st.slider('Enter your age', 0,120,0)
    st.caption('For Children under 1, use 0')

    #Choose if HB or LC/WBC
    if input_Blood == 'Hemoglobin' : 
        normal_ranges = normal_rangesHB
        critical_low = 7
        critical_high = 16
        unit = 'g/dL'
    
    elif input_Blood == 'Leukocytes/WBC':
        normal_ranges = normal_rangesLC
        critical_low= 500
        critical_high = 30000
        unit = 'units/µL'
          
    #Get value from User
    value = st.number_input(f'Enter your value in {unit} to compare', min_value=0.0)
        
    # Get normal range for user's age and sex
    age_range = None
    for age_group, range_list in normal_ranges[sex].items():
            start_age, end_age = age_group.split('-')
            if int(start_age) <= age <= int(end_age):
                age_range = range_list
                break

    # Display graph of user's value compared to normal range
    if age_range:
            st.write(f'Normal range for {sex.lower()}s your age is {age_range[0]}-{age_range[1]} {unit}')
            if value < critical_low:
                st.warning('Value critical, please seek advice from a medical professional!')
            elif value < age_range[0]:        
                st.warning('Value is below normal range')
            elif value > critical_high:
                st.warning ('Value critical, please seek advice from a medical professional!')                
            elif value > age_range[1]:
                st.warning('Value is above normal range')  
            else:
                st.success('Value is within normal range')
            st.line_chart({'Your Value': [value], 'Normal Range': age_range} )
    else:
            st.warning('Invalid age or sex selected')
                    
#Display additional information about the Value looked at        
    if input_Blood == 'Hemoglobin' :     
        st.write("""Hemoglobin is an iron-contraining protein found in red blood cells and is responsible for transporting oxygen and carbon dioxide
                 in the blood.  
                 A low hemoglobin count (anemia) means your body is producing fewer red blood cells than usual, destroying them faster than they can 
                 be produced or you have blood loss. Most common cause for anemia is an iron deficiency.  
                 A high hemoglobin count is most often caused by low oxygen levels in the blood over a long period of time.  
                 An elevated value of a special type of hemoglobin HbA1c can be an indication of uncontrolled blood sugar.  
                 In pregnancy, the normal level of hemoglobin decreases to 10.5 g/dL.""")
                 
    if input_Blood=='Leukocytes/WBC' : 
         st.write("""Leukocytes or white blood cells are components of the immune system and serve to protect the body against infections and diseases.  
                  An increased number of leucocytes (leukocytosis) could indicate an infection or stress.  
                  A decreased number of leucocytes (leukopenia) means your body is not creating enough leukocytes, this can be caused by certain diseases or medications.   
                  In type 2 diabetes, the number of leukocytes in the blood can be used as an indicator of worsening insulin sensitivity and predicts the 
                  development of the disease.   
                  In pregnancy, leucocyte numbers increase significantly, usually between 10.000-16.000 units/µL but can rise up to 29.000 units/µL.""")
    
    

# Run Streamlit app
if __name__ == '__main__':
    app()