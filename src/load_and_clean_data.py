
import pandas as pd

# INPUT: the Excel file you downloaded and placed in the local data/ folder
RAW_XLSX_PATH = "data/online_retail.xlsx"

# OUTPUT: cleaned CSV that we will later load into PostgreSQL
CLEAN_CSV_PATH = "data/online_retail_clean.csv"


def load_data(path: str) -> pd.DataFrame:
    """Load the raw dataset from an Excel file."""
    return pd.read_excel(path)


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning + create revenue metric for analysis."""
    df = df.dropna(subset=["CustomerID"]).copy()

    # Ensure correct datetime format
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Remove invalid rows (returns/cancellations or bad data)
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)].copy()

    # Business metric: revenue per row
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    # Avoid float-looking IDs (e.g., 12345.0)
    df["CustomerID"] = df["CustomerID"].astype(int).astype(str)

    return df


def save_clean_data(df: pd.DataFrame, path: str) -> None:
    """Save cleaned dataset to CSV."""
    df.to_csv(path, index=False)


if __name__ == "__main__":
    df = load_data(RAW_XLSX_PATH)
    clean_df = basic_cleaning(df)
    save_clean_data(clean_df, CLEAN_CSV_PATH)

    print("Clean data saved to:", CLEAN_CSV_PATH)
    print("Number of rows:", len(clean_df))
    print(clean_df.head())

