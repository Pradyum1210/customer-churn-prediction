from preprocessing.preprocessing import preprocess_data
from eda.visualization import run_eda
from segmentation.segmentation import run_segmentation
from model.train_model import model

def main():
    path = "data/Telco_Customer_Churn_Dataset.csv"

    # Step 1: Preprocessing
    data = preprocess_data(path)

    # Step 2: EDA
    data = run_eda(data)

    # Step 3: Segmentation
    run_segmentation(data)

    # Step 4: Model
    model(data)

if __name__ == "__main__":
    main()