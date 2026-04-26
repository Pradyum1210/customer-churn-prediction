
def run_segmentation(data):

    # Churn Rate by tenure group
    seg_tenure_group = data.groupby("tenure_group", observed=False)['Churn'].value_counts().unstack()

    seg_tenure_group["Total"] = seg_tenure_group["Yes"] + seg_tenure_group["No"]
    seg_tenure_group["Churn Rate(%)"] = (seg_tenure_group["Yes"] / seg_tenure_group["Total"]) * 100
    seg_tenure_group["Churn Rate(%)"] = seg_tenure_group["Churn Rate(%)"].round(2)
    print("\nSegmentation by Tenure Group:\n")
    print(seg_tenure_group)

    # Churn Rate by Contract 
    seg_contract = data.groupby("Contract")["Churn"].value_counts().unstack()
    seg_contract["Total"] = seg_contract["Yes"] + seg_contract["No"]
    seg_contract["Churn Rate(%)"] = (seg_contract["Yes"] / seg_contract["Total"]) * 100 
    seg_contract["Churn Rate(%)"] = seg_contract["Churn Rate(%)"].round(2)
    print("\nSegmentation by Contract:\n")
    print(seg_contract)

    # Churn Rate by Monthly Charges
    seg_monthly_charges = data.groupby("charges_group")["Churn"].value_counts().unstack()
    seg_monthly_charges["Total"] = seg_monthly_charges["Yes"] + seg_monthly_charges["No"]
    seg_monthly_charges['Churn Rate(%)'] = (seg_monthly_charges["Yes"] / seg_monthly_charges["Total"]) * 100
    seg_monthly_charges['Churn Rate(%)'] = seg_monthly_charges['Churn Rate(%)'].round(2)
    print("\nSegmentation by Monthly Contract:\n")
    print(seg_monthly_charges)

    