# -*- coding: utf-8 -*-
"""ROI Calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C4f8OtVf4-yORPDYNO2tw5HQR3jhnFRv
"""
import streamlit as st

# Function to calculate simulated values
def calculate_simulated_values(aht, non_talk_time, asa, wrap_up_time, reduction_percent):
    aht_reduction = aht * reduction_percent / 100
    non_talk_time_reduction = non_talk_time * reduction_percent / 100
    asa_reduction = asa * reduction_percent / 100
    wrap_up_reduction = wrap_up_time * reduction_percent / 100
    
    simulated_aht = round(aht - aht_reduction, 2)
    simulated_non_talk_time = round(non_talk_time - non_talk_time_reduction, 2)
    simulated_asa = round(asa - asa_reduction, 2)
    simulated_wrap_up_time = round(wrap_up_time - wrap_up_reduction, 2)
    simulated_call_duration = round(simulated_aht + simulated_non_talk_time + simulated_asa + simulated_wrap_up_time, 2)
    
    return simulated_aht, simulated_non_talk_time, simulated_asa, simulated_wrap_up_time, simulated_call_duration

# Main function
def main():
    st.title("Key Metric Reduction Simulation & ROI Realization")
    
    # Add logo on the top right-hand side
    st.image("https://humach.com/wp-content/uploads/2023/01/HuMach_logo-bold.png", width=80, use_column_width=False, caption=None, output_format='auto')
    
    # User input section
    st.sidebar.title("Input Metrics")
    aht = st.sidebar.number_input("AHT", value=450.00, format="%.2f")
    non_talk_time = st.sidebar.number_input("Non-Talk Time", value=90.00, format="%.2f")
    asa = st.sidebar.number_input("ASA", value=31.00, format="%.2f")
    wrap_up_time = st.sidebar.number_input("Wrap Up Time", value=31.00, format="%.2f")
    
    cost_per_call = st.sidebar.number_input("Cost per Call (Fully loaded)", value=15.0, format="%.2f")
    cost_per_second = cost_per_call / aht
    
    calls_per_day = st.sidebar.number_input("Calls per Day", value=10000)
    
    # Slider section
    reduction_percent = st.slider("Reduction Percentage", min_value=1, max_value=100, step=1, value=1)
    
    # Calculation section
    simulated_aht, simulated_non_talk_time, simulated_asa, simulated_wrap_up_time, simulated_call_duration = calculate_simulated_values(aht, non_talk_time, asa, wrap_up_time, reduction_percent)
    
    total_seconds_saved = (aht + non_talk_time + asa + wrap_up_time - simulated_call_duration) * calls_per_day
    value_realised = total_seconds_saved * cost_per_second
    
    # Display section
    st.write("## Original Metrics")
    st.write("- AHT:", aht)
    st.write("- Non-Talk Time:", non_talk_time)
    st.write("- ASA:", asa)
    st.write("- Wrap Up Time:", wrap_up_time)
    
    st.write("## Simulated Metrics")
    st.write("- AHT:", simulated_aht)
    st.write("- Non-Talk Time:", simulated_non_talk_time)
    st.write("- ASA:", simulated_asa)
    st.write("- Wrap Up Time:", simulated_wrap_up_time)
    st.write("- Simulated Call Duration:", simulated_call_duration)
    
    # Cost analysis section
    st.write("## Cost Analysis")
    st.write(f"- Total Cost per Day: ${cost_per_call:.2f}")
    st.write(f"- Cost per Second: ${cost_per_second:.5f}")
    
    # ROI realization section
    st.write("## ROI Realization")
    st.write(f"- Total Seconds Saved: {total_seconds_saved:.2f}")
    st.write(f"- Value Realised: ${value_realised:.2f}")

if __name__ == "__main__":
    main()
