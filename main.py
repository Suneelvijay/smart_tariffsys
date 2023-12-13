import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import streamlit as st

def main():
    st.title("Electricity Tariff Calculator")

    # Define input variables
    frequency_change = ctrl.Antecedent(np.arange(-1, 1.1, 0.1), 'frequency_change')
    consumption = ctrl.Antecedent(np.arange(-1, 1.1, 0.1), 'consumption')

    # Define output variable
    electricity_tariff = ctrl.Consequent(np.arange(-1, 1.1, 0.1), 'electricity_tariff')

    # Define linguistic variables and rules (same as before)

    # Create control system and simulation
    electricity_tariff_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
    electricity_tariff_simulation = ctrl.ControlSystemSimulation(electricity_tariff_ctrl)

    # Streamlit sidebar input fields
    with st.sidebar:
        st.subheader("Enter Input Values")
        frequency = st.slider("Frequency Change", -1.0, 1.0, step=0.1)
        consumed = st.slider("Consumption rate", -1.0, 1.0, step=0.1)
        calculate = st.button("Calculate")

    # Calculate and display the result
    if calculate:
        electricity_tariff_simulation.input['frequency_change'] = frequency
        electricity_tariff_simulation.input['consumption'] = consumed
        electricity_tariff_simulation.compute()

        tariff_output = electricity_tariff_simulation.output['electricity_tariff']
        base = 4.5
        change = base * tariff_output
        final = base + change

        st.subheader("Result")
        st.write(f"Tariff Change: {tariff_output*100: .2f} %")
        st.write(f"Actual Base Charge: ₹{base}/-")
        st.write(f"Updated Charge Per-Unit: ₹{final:.2f}/-")

if __name__ == "__main__":
    main()
