# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 12:54:48 2023

@author: alexa
"""



import streamlit as st
import json
import matplotlib.pyplot as plt

          
# Define Streamlit app
def app():
        with open ('sample_HB.json') as HB:
            normal_rangesHB=json.load(HB)
        
        with open('sample_LC.json') as LC:
            normal_rangesLC=json.load(LC)
        
        with open ('sample_HK.json') as HK:
            normal_rangesHK=json.load(HK)
           
    
        st.title('LabData')
        
        st.write("LabData is an App to help you interpret your medical blood values. It is still in its trial phase",
                 " and more values and additional information will be added over time.")
        st.write("*:red[**Important Notice:**] The information provided in this app is for educational purposes only",
             " and should not be considered medical advice. This app is not intended to replace a doctor's visit.",
             " Always consult a healthcare professional for any concerns or questions regarding your health.*")
    
    # Get user input for age, sex, and value to compare
        input_Blood= st.sidebar.radio('Choose what Blood value you are interessted it:', ('Hemoglobin', 'Leukocytes/WBC', 'Hematocrit'))
        sex = st.sidebar.radio('Choose your biological sex:',('Male','Female'))
        age = st.sidebar.number_input('Enter your age', 0,120,0)
        st.sidebar.caption('For Children under 1, use 0')
        #input_extra= st.selectbox('Choose additional Information:', ('None','Pregnant', 'Diabetes'))
        

    #Choose if HB or LC/WBC
        if input_Blood == 'Hemoglobin' : 
            normal_ranges = normal_rangesHB
            critical_low = 7
            critical_high = 16
            unit = 'g/dL'
    
        if input_Blood == 'Leukocytes/WBC':
            normal_ranges = normal_rangesLC
            critical_low= 500
            critical_high = 30000
            unit = 'units/µL'
            
        if input_Blood == 'Hematocrit':
            normal_ranges=normal_rangesHK
            critical_low= 30
            critical_high= 50
            unit= '%'
          
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
                    
                fig, ax = plt.subplots()
                ax.plot(value, marker='o', color= 'blue', label='Your Value')
                ax.axhline(critical_high, color='red', linestyle='-', label='Critical High')
                ax.axhline(critical_low,color= 'red', linestyle='-', label='Critical Low')
                ax.axhline(age_range[1],color= 'green', linestyle='dotted', label='high Range')
                ax.axhline(age_range[0],color= 'green', linestyle='dotted', label='low Range')
                ax.set_title(f'{input_Blood} {unit }')
                ax.set_xticklabels([])
                ax.legend(loc='best' )
                plt.tight_layout()
                st.pyplot(fig)
                
        else:
                st.warning('Invalid age or sex selected')
                    
     #Display additional information about the velue of interesst        
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
                   
        if input_Blood =='Hematocrit' : 
             st.write ("""Hematocrit is the ratio of the volume of red blood cells to the total volume of blood. 
                       A low hematocrit value can indicate to few red blood cells, also called anemia. A level above the normal range means to many red blood cells,
                       this may indicate polycythemia or erythrocytosis""")

        st.caption('*published by F.Schindler & H.Alexander 2023*')
        
   
if __name__ == '__main__':
    app()
