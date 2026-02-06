# Disease Symptoms NLP Dataset Generator

This project converts a structured disease–symptoms dataset into natural language text suitable for **NLP and machine learning tasks**.

It processes a CSV file where symptoms are represented as binary columns (`0` / `1`) and generates human-readable medical sentences describing symptoms and diagnoses.

---

## 📌 What This Project Does

* Reads a disease–symptoms CSV dataset from the same folder
* Identifies active symptoms (columns with value `1`)
* Converts structured rows into NLP-friendly text
* Exports a new CSV file ready for:

  * NLP model training
  * Text classification
  * LLM fine-tuning
  * Medical AI experiments

---

## 🧠 Example

**Structured Input:**

```
fever = 1, cough = 1, headache = 0, diseases = Flu
```

**Generated Text:**

```
Symptoms: fever, cough. Diagnosis: Flu.
```

---

## 📂 Project Structure

All files are kept in **one folder**:

```
disease-symptoms-nlp/
├── script.py
├── Disease and symptoms dataset.csv
├── Disease symptoms NLP.csv
└── README.md
```

---

## 🛠 Requirements

* Python 3.7+
* pandas

Install dependencies:

```bash
pip install pandas
```

---

## 🚀 How to Run

No path configuration needed.

The script uses **relative paths**, so it automatically reads and writes files from the current folder.

### Steps

1. Place the dataset file in the same folder as the script:

```
Disease and symptoms dataset.csv
```

2. Run the script:

```bash
python script.py
```

3. Output file will be created in the same folder:

```
Disease symptoms NLP.csv
```


---

## 🧪 Output Columns

| Column Name | Description                         |
| ----------- | ----------------------------------- |
| `nlp_text`  | Generated natural language sentence |
| `diseases`  | Original disease label              |

---

## 💡 Use Cases

* Medical NLP preprocessing
* Dataset generation for ML
* LLM fine-tuning
* Healthcare AI research
* Data augmentation


