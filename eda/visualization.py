import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def run_eda(data):

    # Churn distribution
    churn = data["Churn"].value_counts()
    sns.barplot(x=churn.index, y=churn.values)
    plt.title("Churn")
    plt.show()

    # Gender vs Churn
    sns.countplot(x=data["gender"], hue=data["Churn"])
    plt.title("Churn by Gender")
    plt.show()

    # Contract vs Churn
    sns.countplot(x=data["Contract"], hue=data["Churn"])
    plt.title("Churn by Contract")
    plt.show()

    # Tenure distribution
    sns.histplot(x=data["tenure"], hue=data["Churn"], bins=30)
    plt.title("Churn by Tenure")
    plt.show()

    # Payment Method
    sns.countplot(x=data["PaymentMethod"], hue=data["Churn"])
    plt.xticks(rotation=20)
    plt.title("Payment Method vs Churn")
    plt.show()

    # Monthly Charges
    sns.boxplot(x="Churn", y="MonthlyCharges", data=data)
    plt.title("Monthly Charges vs Churn")
    plt.show()

    # Tenure Group
    data["tenure_group"] = pd.cut(
        data["tenure"],
        bins=[0, 12, 24, 72],
        labels=["0-12", "12-24", "24+"]
    )

    sns.countplot(x=data["tenure_group"], hue=data["Churn"])
    plt.title("Tenure Group vs Churn")
    plt.show()

    return data  