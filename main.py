import pandas as pd

file_path = "Disease and symptoms dataset.csv"
df = pd.read_csv(file_path)

symptoms_columns = df.columns[1:]

def convert_to_nlp(row):
    active_symptoms = [col for col in symptoms_columns if row[col] == 1]
    symptoms_text = ", ".join(active_symptoms)
    disease = row['diseases']
    return f"Symptoms: {symptoms_text}. Diagnosis: {disease}."

df['nlp_text'] = df.apply(convert_to_nlp, axis=1)

output_path = "Disease symptoms NLP.csv"
df[['nlp_text', 'diseases']].to_csv(output_path, index=False)

print(f"Donee: {output_path}")
