import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define input variables
frequency_change = ctrl.Antecedent(np.arange(-1, 1.1, 0.1), 'frequency_change')
consumption = ctrl.Antecedent(np.arange(-1, 1.1, 0.1), 'consumption')

# Define output variable
electricity_tariff = ctrl.Consequent(np.arange(-1, 1.1, 0.1), 'electricity_tariff')

# Define linguistic variables for frequency_change and consumption
frequency_change['N'] = fuzz.trimf(frequency_change.universe, [-2, -1, 0])
frequency_change['Z'] = fuzz.trimf(frequency_change.universe, [-1, 0, 1])
frequency_change['P'] = fuzz.trimf(frequency_change.universe, [0, 1, 2])
consumption['N'] = fuzz.trimf(consumption.universe, [-2, -1, 0])
consumption['Z'] = fuzz.trimf(consumption.universe, [-1, 0, 1])
consumption['P'] = fuzz.trimf(consumption.universe, [0, 1, 2])

# Define linguistic variables for electricity_tariff
electricity_tariff['L'] = fuzz.trimf(electricity_tariff.universe, [-2, -1, 0])
electricity_tariff['M'] = fuzz.trimf(electricity_tariff.universe, [-1, 0, 1])
electricity_tariff['H'] = fuzz.trimf(electricity_tariff.universe, [0, 1, 2])

# Define rules
rule1 = ctrl.Rule(antecedent=(frequency_change['P'] & consumption['P']), consequent=electricity_tariff['L'])
rule2 = ctrl.Rule(antecedent=(frequency_change['Z'] & consumption['P']), consequent=electricity_tariff['H'])
rule3 = ctrl.Rule(antecedent=(frequency_change['N'] & consumption['P']), consequent=electricity_tariff['H'])
rule4 = ctrl.Rule(antecedent=(frequency_change['P'] & consumption['Z']), consequent=electricity_tariff['M'])
rule5 = ctrl.Rule(antecedent=(frequency_change['Z'] & consumption['Z']), consequent=electricity_tariff['M'])
rule6 = ctrl.Rule(antecedent=(frequency_change['N'] & consumption['Z']), consequent=electricity_tariff['M'])
rule7 = ctrl.Rule(antecedent=(frequency_change['P'] & consumption['N']), consequent=electricity_tariff['M'])
rule8 = ctrl.Rule(antecedent=(frequency_change['Z'] & consumption['N']), consequent=electricity_tariff['M'])
rule9 = ctrl.Rule(antecedent=(frequency_change['N'] & consumption['N']), consequent=electricity_tariff['L'])

# Create and simulate the control system
electricity_tariff_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
electricity_tariff_simulation = ctrl.ControlSystemSimulation(electricity_tariff_ctrl)

# Pass inputs to the simulation
frequency = float(input("Enter Frequncy Change: "))  # Example input values
consumed = float(input("Enter Consumption rate: "))  # Example input values

electricity_tariff_simulation.input['frequency_change'] = frequency
electricity_tariff_simulation.input['consumption'] = consumed

# Compute the result
electricity_tariff_simulation.compute()

# Get the computed output

tariff_output = electricity_tariff_simulation.output['electricity_tariff']
print(f"Tariff Change: {tariff_output*100: .2f} %")

# Electricity Tariff Updation
base = 4.5
change = base * tariff_output
final = base + change
print(f"Actual Base Charge: ₹{base}/-")
print(f"Updated Charge Per-Unit: ₹{final:.2f}/-")
