from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

# Load scaler and model saved with joblib
scaler = joblib.load('normalizer.pkl')
model = joblib.load('rf_acc_68.pkl')

app = Flask(__name__)

FEATURE_ORDER = [
    "Total Bilirubin (mg/dl)",
    "Duration of alcohol consumption(years)",
    "Direct (mg/dl)",
    "AL.Phosphatase (U/L)",
    "Platelet Count (lakhs/mm)",
    "Indirect (mg/dl)",
    "Polymorphs (%)",
    "Albumin (g/dl)",
    "PCV (%)",
    "SGOT/AST (U/L)",
    "Lymphocytes (%)",
    "Age",
    "Monocytes (%)",
    "BP_Systolic",
    "Hemoglobin (g/dl)",
    "Quantity of alcohol consumption (quarters/day)",
    "Diabetes Result",
    "Total Protein (g/dl)",
    "SGPT/ALT (U/L)",
    "Globulin (g/dl)"
]


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
         # Convert form data to dictionary
        raw_data = request.form.to_dict()

        # Convert 'Positive'/'Negative' to binary
        raw_data["diabetes_result"] = 1 if raw_data["diabetes_result"].lower() == "positive" else 0

                # Mapping keys to model's expected format
        cleaned_data = {
            "Total Bilirubin (mg/dl)": float(raw_data["total_bilirubin_mg_dl"]),
            "Duration of alcohol consumption(years)": float(raw_data["duration_of_alcohol_consumption_years"]),
            "Direct (mg/dl)": float(raw_data["direct_mg_dl"]),
            "AL.Phosphatase (U/L)": float(raw_data["al_phosphatase_u_l"]),
            "Platelet Count (lakhs/mm)": float(raw_data["platelet_count_lakhs_mm"]),
            "Indirect (mg/dl)": float(raw_data["indirect_mg_dl"]),
            "Polymorphs (%)": float(raw_data["polymorphs_percent"]),
            "Albumin (g/dl)": float(raw_data["albumin_g_dl"]),
            "PCV (%)": float(raw_data["pcv_percent"]),
            "SGOT/AST (U/L)": float(raw_data["sgot_ast_u_l"]),
            "Lymphocytes (%)": float(raw_data["lymphocytes_percent"]),
            "Age": float(raw_data["age"]),
            "Monocytes (%)": float(raw_data["monocytes_percent"]),
            "BP_Systolic": float(raw_data["bp_systolic"]),
            "Hemoglobin (g/dl)": float(raw_data["hemoglobin_g_dl"]),
            "Quantity of alcohol consumption (quarters/day)": float(raw_data["quantity_of_alcohol_consumption_quarters_day"]),
            "Diabetes Result": int(raw_data["diabetes_result"]),
            "Total Protein (g/dl)": float(raw_data["total_protein_g_dl"]),
            "SGPT/ALT (U/L)": float(raw_data["sgpt_alt_u_l"]),
            "Globulin (g/dl)": float(raw_data["globulin_g_dl"])
        }

        try:
             # Create DataFrame in correct order
            input_df = pd.DataFrame([cleaned_data])[FEATURE_ORDER]

            # Scale and predict
            scaled = scaler.transform(input_df)
            # predict
            probs = model.predict_proba(scaled)
            predict = model.predict(scaled)
            confidence_score = round(probs[0][int(predict[0])] * 100)


            return render_template("results.html", prediction=int(predict[0]), confidence_score=confidence_score)

        except KeyError as e:
            return f"Missing input: {e}", 400
        except ValueError:
            return "Invalid input: All values must be numeric", 400
    
    return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)