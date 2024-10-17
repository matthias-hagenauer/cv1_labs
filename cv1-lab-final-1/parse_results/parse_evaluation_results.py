import pandas as pd

# Initialize lists to store the data
data = {
    "Feature_Type": [],
    "Kernel": [],
    "C": [],
    "Frog_AP": [],
    "Automobile_AP": [],
    "Bird_AP": [],
    "Cat_AP": [],
    "Deer_AP": [],
    "Mean_AP": []
}

# Open and parse the file
with open('svm_evaluation_results_1000.txt', 'r') as file:
    feature_type = None
    for line in file:
        line = line.strip()

        # Detect Feature_Type section headers (e.g., 'sift_0.4', 'orb_1', etc.)
        if 'Testrun for' in line:
            feature_type = line.split()[-1]  # The last part is the feature type (e.g., 'sift_0.4')
        
        # Detect Kernel and C lines
        elif line.startswith('Kernel:'):
            parts = line.split(',')
            kernel = parts[0].split(': ')[1].strip()
            C_value = parts[1].split(': ')[1].strip()
        
        # Detect AP values for each class
        elif line.startswith('Class'):
            class_name = line.split()[1][:-1]  # Extract the class name (e.g., 'Frog')
            ap_value = float(line.split('= ')[1])
            if class_name == 'Frog':
                frog_ap = ap_value
            elif class_name == 'Automobile':
                automobile_ap = ap_value
            elif class_name == 'Bird':
                bird_ap = ap_value
            elif class_name == 'Cat':
                cat_ap = ap_value
            elif class_name == 'Deer':
                deer_ap = ap_value

        # Detect Mean AP
        elif line.startswith('Mean AP'):
            mean_ap = float(line.split(': ')[1])
            
            # Append the data to the dictionary after collecting all APs
            data["Feature_Type"].append(feature_type)
            data["Kernel"].append(kernel)
            data["C"].append(C_value)
            data["Frog_AP"].append(frog_ap)
            data["Automobile_AP"].append(automobile_ap)
            data["Bird_AP"].append(bird_ap)
            data["Cat_AP"].append(cat_ap)
            data["Deer_AP"].append(deer_ap)
            data["Mean_AP"].append(mean_ap)

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a pickle file
df.to_pickle('parsed_data_1000.pkl')

print("DataFrame saved as 'parsed_data.pkl'")

