#patient types
neonate = "Neonate"
infant = "Infant"
infant_child = "Infant/Child"
adult = "Adult"


#error check
def input_check(val, prompt):
    val = val.strip()
    while val ==  "" or not val.isnumeric():
        print("Enter a numeric value")
        val = input(prompt)
        val = val.strip()
    return float(val)

#age group determination
def age_determine():
    patient_age_y = (input("Enter age in years (Enter 0 if not applicable): "))
    patient_age_y = int(input_check(patient_age_y, "Enter age in years (Enter 0 if not applicable): "))

    if patient_age_y < 1:
        patient_age_m = (input("Enter age in months (Enter 0 is child is less than a month old): "))
        patient_age_m = int(input_check(patient_age_m, "Enter age in months (Enter 0 is child is less than a month old): "))
        if patient_age_m < 1:
            patient_type = neonate
        elif patient_age_m <= 3:
            patient_type = infant
        else:
            patient_type = infant_child
    elif patient_age_y <= 12:
        patient_type = infant_child
    else:
        patient_type = adult
    return patient_type
        
#recommended dosage computation
def dosage_calc_mg(patient_type, weight):
    if patient_type == neonate or patient_type == infant:
        max_dose_single = weight*10
        max_dose_day = max_dose_single * 4
        regular_dose = "10 mg/kg every 6 to 8 hrs"
    elif patient_type == infant_child:
        max_dose_single = weight*15
        max_dose_day = max_dose_single * 4
        regular_dose = "10-15 mg/kg every 6 to 8 hrs"
    else:
        regular_dose = "500-1000 mg every 4 to 6 hrs"
        if weight <= 50:
            max_dose_single = 750 
            max_dose_day = 3000
        elif weight > 50:
            max_dose_single = 1000
            max_dose_day = 4000
    return max_dose_single, max_dose_day, regular_dose

#commercially available formulations
conc =  [100, 50, 24, 250, 325, 500, 125, 250]
formulation = ['100 mg/ml', '250/5 mg/ml', '120/5 mg/ml', '250 mg', '325 mg', '500 mg', '125 mg', '250 mg']
form = ['drops', 'syrup/susp', 'syrup/susp', 'tablet','tablet', 'tablet', 'suppository', 'suppository']
unit = ['ml', 'ml', 'ml', 'tabs', 'tabs', 'tabs', 'suppository', 'suppository']

#output section
#introduction 
print("-----------------------------------------------------------")
print("PARACETAMOL DOSAGE CALCULATOR")
print("This calculator provides general guidance based on clinical practice guidelines\n"
      "and is intended for individuals without contraindications or elevated toxicity risk.\n"
      "Always consult your healthcare provider and refer to the package leaflet for full\n"
      "dosage instructions and safety information.")
print()

#main
patient_type = age_determine()
weight = input("Weight in kg: ")
weight = int(input_check(weight, "Weight in kg: "))
mg = dosage_calc_mg(patient_type, weight)


#Summary of recommendations
print()
print("-----------------------------------------------------------")
print("Patient age group: ", patient_type)
print("Weight: ", weight, "kg")
print("Recommended dose:", mg[2])
print("Maximum single dose:", mg[0], "mg")
print("Maximum daily dose: ", mg[1], "mg")
if patient_type == infant or patient_type == neonate:
    print("\nNote: Paracetamol use for children less than 3 months should always be consulted to a healthcare professional.")


#Dose per formulation in table form
print()
print("-----------------------------------------------------------")
print("Recommended dose based on Commercially available strengths: ")
print("{:<15} {:<15} {:<9} {:<15}".format("Dosage", "Form", "Qty", "Units/dose"))
for meds in list(zip(conc, formulation, form, unit)):  
    print("{:<15} {:<15} {:<9} {:<15}".format(meds[1], meds[2], round(mg[0]/meds[0], 2), format(meds[3], "<15")))
print()
print("For tablets and suppositories, exact strength is provided. Round up as necessary ")
print("-----------------------------------------------------------")
    
    











