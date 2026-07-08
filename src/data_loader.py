import pandas as pd

class NetflixDataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def load_data(self) -> pd.DataFrame:
        """Loads dataset and logs initial metadata."""
        print(f"🚀 Loading dataset from: {self.file_path}")
        self.df = pd.read_csv(self.file_path)
        
        print(f"📈 Shape: {self.df.shape[0]} Rows, {self.df.shape[1]} Columns")
        return self.df

    def clean_data(self) -> pd.DataFrame:
        """Cleans formats and strips redundant data identifiers."""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        # Check and remove duplicates based on show_id
        duplicate_count = self.df["show_id"].duplicated().sum()
        print(f"🔍 Found {duplicate_count} duplicated Show IDs.")
        
        # Safely drop ID column
        if "show_id" in self.df.columns:
            self.df.drop(columns="show_id", inplace=True)

        # Standardize added date format
        if "date_added" in self.df.columns:
            self.df["date_added"] = pd.to_datetime(self.df["date_added"])
            print(f"📅 Date range: {self.df['date_added'].min()} to {self.df['date_added'].max()}")

        return self.df
