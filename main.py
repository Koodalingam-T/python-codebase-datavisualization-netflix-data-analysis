import os
import sys
from config import settings
from src.data_loader import NetflixDataLoader
from src.visualizer import NetflixVisualizer

def main():
    # 1. Setup Global Configurations
    settings.apply_pandas_settings()

    # 2. Identify Target Data Path
    # Pull path from environment or drop back to config defaults
    data_path = os.getenv("NETFLIX_DATA_PATH", settings.DEFAULT_DATA_PATH)
    
    if not os.path.exists(data_path):
        print(f" Error: Data file not found at '{data_path}'.")
        print("Please place 'netflix1.csv' into the 'data/' folder before running.")
        sys.exit(1)

    # 3. Data Extraction Pipeline
    loader = NetflixDataLoader(data_path)
    loader.load_data()
    clean_df = loader.clean_data()

    # 4. Reporting Pipeline
    visualizer = NetflixVisualizer(clean_df)
    
    print("\nCompiling individual analytics views...")
    visualizer.plot_show_type_frequency()
    visualizer.plot_content_distribution_pie()
    visualizer.plot_top_countries()
    visualizer.plot_release_trends()
    visualizer.plot_maturity_ratings()
    
    print("\nAssembling composite master dashboard...")
    visualizer.generate_unified_dashboard()
    print("✨ Execution successfully completed!")

if __name__ == "__main__":
    main()
