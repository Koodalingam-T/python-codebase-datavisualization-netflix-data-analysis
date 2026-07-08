# Netflix Data Analysis & Streaming Insights Dashboard

A professional, modular data engineering and exploratory data analysis (EDA) pipeline designed to extract, clean, and visualize streaming insights from Netflix datasets. Built with Python, Pandas, and Plotly, this project transforms raw tabular data into functional, interactive visualization matrices.

## 📊 Business & Data Insights
This pipeline ingests streaming catalogs to deliver core operational insights:
* **Content Distribution Matrix**: Relative ratios of global Movies vs. TV Shows.
* **Geographical Production Hotspots**: Top 10 content-producing nations.
* **Historical Velocity Trends**: Temporal growth analysis of content releases over time.
* **Audience Segment Breakdown**: Interactive Treemaps evaluating content maturity rating distribution.

---

## 📁 Repository Structure

The architecture isolates configuration, logical steps, data parsing, and UI generation into distinct modules for optimal maintainability:

```text
netflix-data-analysis/
├── config/
│   └── settings.py          # Centralized global hyper-parameters, paths, and visualization themes
├── data/
│   └── .gitkeep             # Git landing anchor for local raw streaming data files
├── src/
│   ├── __init__.py          # Packaging structural initialization file
│   ├── data_loader.py       # Data extraction, duplicate identification, and sanitization engine
│   └── visualizer.py        # Chart generation pipeline utilizing Plotly Express and Graph Objects
├── .gitignore               # System cache and dataset isolation matrix
├── main.py                  # Main execution driver orchestrating the application lifestyle
├── README.md                # Structural project blueprint and technical operational manual
└── requirements.txt         # Pinned execution dependencies for environment alignment
```

---

## 🛠️ Architectural Engineering Highlights

* **Object-Oriented Structure**: Data parsing (`NetflixDataLoader`) and graphics presentation (`NetflixVisualizer`) logic flows are decoupling into dedicated Python classes.
* **Immutable Environment Isolation**: Configuration settings (like the trademark Netflix branding palette) are isolated in `config/settings.py` to prevent hard-coding errors.
* **Memory Safety Protocol**: Large local `.csv`/`.zip` source datasets are strictly isolated via `.gitignore` to prevent repository bloat and ensure fast deployment cycles.
* **Unified Dashboard Fabric**: Uses `plotly.subplots` to efficiently assemble discrete analytic nodes into a unified 2x2 presentation dashboard.

---

## ⚡ Technical Installation & Execution Guide

### 1. Clone the Workspace Ecosystem
```bash
git clone https://github.com
cd netflix-data-analysis
```

### 2. Configure Virtual Environment & Dependencies
```bash
# Initialize clean sandbox environment
python -m venv venv

# Activate sandbox across environment platforms
source venv/bin/activate       # Mac/Linux
.\venv\Scripts\activate       # Windows

# Sync required library dependencies
pip install -r requirements.txt
```

### 3. Deploy Local Datasets
Place your unzipped dataset file named exactly `netflix1.csv` directly into the placeholder data directory:
```bash
netflix-data-analysis/data/netflix1.csv
```

### 4. Execute the Application Pipeline
Run the orchestration engine to generate logs and launch the dashboards:
```bash
python main.py
```

---

## 🧰 Dependencies Matrix
* **Pandas**: Structural data indexing, grouping, and conversion.
* **Plotly & Cufflinks**: Declarative engine generating interactive, high-performance charting outputs.
* **NumPy**: Low-level vectorized floating-point adjustments.
