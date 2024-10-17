import pandas as pd

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

with open('svm_evaluation_results_1000.txt', 'r') as file:
    feature_type = None
    for line in file:
        line = line.strip()

        if 'Testrun for' in line:
            feature_type = line.split()[-1]  
        
        elif line.startswith('Kernel:'):
            parts = line.split(',')
            kernel = parts[0].split(': ')[1].strip()
            C_value = parts[1].split(': ')[1].strip()
        
        elif line.startswith('Class'):
            class_name = line.split()[1][:-1]  
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

        elif line.startswith('Mean AP'):
            mean_ap = float(line.split(': ')[1])
            
            data["Feature_Type"].append(feature_type)
            data["Kernel"].append(kernel)
            data["C"].append(C_value)
            data["Frog_AP"].append(frog_ap)
            data["Automobile_AP"].append(automobile_ap)
            data["Bird_AP"].append(bird_ap)
            data["Cat_AP"].append(cat_ap)
            data["Deer_AP"].append(deer_ap)
            data["Mean_AP"].append(mean_ap)

df = pd.DataFrame(data)

df.to_pickle('parsed_data_1000.pkl')

print("DataFrame saved as 'parsed_data.pkl'")

