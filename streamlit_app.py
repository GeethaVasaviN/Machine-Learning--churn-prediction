{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "51da36a4-746f-4105-aa1e-968e20d1d83d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\ASUS\\OneDrive\\Desktop\\Desktop\\churn-prediction\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "print(os.getcwd())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "58b2fdac-a177-4cdd-bf3d-3b117e567c0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overwriting streamlit_app.py\n"
     ]
    }
   ],
   "source": [
    "\n",
    "%%writefile streamlit_app.py\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import joblib\n",
    "\n",
    "# Load trained model and features\n",
    "model = joblib.load(\"churn_model.pkl\")\n",
    "model_features = joblib.load(\"model_features.pkl\")\n",
    "\n",
    "st.title(\"📊 Customer Churn Prediction App\")\n",
    "st.write(\"Enter customer details to predict churn probability.\")\n",
    "\n",
    "# Input fields\n",
    "gender = st.selectbox(\"Gender\", [\"Male\", \"Female\"])\n",
    "senior = st.selectbox(\"Senior Citizen\", [0, 1])\n",
    "partner = st.selectbox(\"Partner\", [\"Yes\", \"No\"])\n",
    "dependents = st.selectbox(\"Dependents\", [\"Yes\", \"No\"])\n",
    "tenure = st.number_input(\"Tenure (months)\", min_value=0, max_value=72, value=12)\n",
    "monthly_charges = st.number_input(\"Monthly Charges\", min_value=0.0, max_value=200.0, value=50.0)\n",
    "total_charges = st.number_input(\"Total Charges\", min_value=0.0, value=1000.0)\n",
    "contract = st.selectbox(\"Contract\", [\"Month-to-month\", \"One year\", \"Two year\"])\n",
    "\n",
    "# Create DataFrame\n",
    "input_data = pd.DataFrame({\n",
    "    \"gender\": [1 if gender == \"Male\" else 0],\n",
    "    \"SeniorCitizen\": [senior],\n",
    "    \"Partner\": [1 if partner == \"Yes\" else 0],\n",
    "    \"Dependents\": [1 if dependents == \"Yes\" else 0],\n",
    "    \"tenure\": [tenure],\n",
    "    \"MonthlyCharges\": [monthly_charges],\n",
    "    \"TotalCharges\": [total_charges],\n",
    "    \"Contract\": [contract]\n",
    "})\n",
    "\n",
    "# One-hot encode categorical fields\n",
    "input_data = pd.get_dummies(input_data)\n",
    "input_data = input_data.reindex(columns=model_features, fill_value=0)\n",
    "\n",
    "# Predict button\n",
    "if st.button(\"Predict Churn\"):\n",
    "    prediction = model.predict(input_data)[0]\n",
    "    probability = model.predict_proba(input_data)[0][1]\n",
    "    \n",
    "    if prediction == 1:\n",
    "        st.error(f\"⚠️ Customer is likely to churn. Probability: {probability:.2f}\")\n",
    "    else:\n",
    "        st.success(f\"✅ Customer is not likely to churn. Probability: {probability:.2f}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ddb1ad0-66ed-40d4-bdf6-a8ed6a0f1dfe",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
