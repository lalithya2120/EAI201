import pandas as pd
import json


# -----------------------------------------------------
# TASK A: Load & Integrate Datasets
# -----------------------------------------------------
def gamma_load_and_integrate():
    try:
        zoo_df = pd.read_csv("zoo.csv", encoding="utf-8")
    except UnicodeDecodeError:
        zoo_df = pd.read_csv("zoo.csv", encoding="latin-1")

    class_df = pd.read_csv("class.csv")

    with open("auxiliary_metadata.json", "r") as f:
        metadata = json.load(f)

    cleaned_metadata = []
    for entry in metadata:
        fixed = {}

        # Standardize base attributes
        fixed["animal_name"] = entry.get("animal_name", "").strip().lower()
        fixed["habitat"] = (entry.get("habitat") or entry.get("habitats") or "unknown").strip().lower()

        diet = entry.get("diet") or entry.get("diet_type") or "unknown"
        diet = diet.strip().lower()
        if diet == "omnivor":
            diet = "omnivore"
        fixed["diet"] = diet

        fixed["conservation_status"] = (
            entry.get("conservation_status")
            or entry.get("conservation")
            or entry.get("status")
            or "unknown"
        ).strip().lower()

        cleaned_metadata.append(fixed)

    metadata_df = pd.DataFrame(cleaned_metadata)
    return zoo_df, class_df, metadata_df



# -----------------------------------------------------
# TASK B: Name Normalization (Roll number last digit = 6)
# -----------------------------------------------------
def gamma_normalize_names(df):
    df["_lower_name"] = df["animal_name"].str.lower()
    df = df.drop_duplicates(subset="_lower_name", keep="first")
    df = df.drop(columns=["_lower_name"])
    return df



# -----------------------------------------------------
# TASK C: Fix JSON Data Inconsistencies
# -----------------------------------------------------
def gamma_fix_json(metadata_df):
    metadata_df = metadata_df.rename(columns={
        "habitat": "habitat_type",
        "habitats": "habitat_type",
        "diet_type": "diet",
        "conservation": "conservation_status",
        "status": "conservation_status"
    })

    metadata_df["diet"] = metadata_df["diet"].str.lower().str.strip()
    metadata_df["diet"] = metadata_df["diet"].replace({"omnivor": "omnivore"})

    metadata_df["habitat_type"] = (
        metadata_df["habitat_type"]
        .str.lower()
        .str.strip()
        .replace({
            "fresh water": "freshwater",
            "freshwater ": "freshwater",
            "freshwater\n": "freshwater",
            "freshwater\r": "freshwater"
        })
    )

    return metadata_df



# -----------------------------------------------------
# TASK D: Merge on animal_name with NO DATA LOSS (LEFT JOIN)
# -----------------------------------------------------
def gamma_merge_datasets(zoo_df, metadata_df):
    merged = pd.merge(
        zoo_df,
        metadata_df,
        on="animal_name",
        how="left"
    )

    # Fill missing auxiliary metadata with "unknown"
    merged["habitat_type"] = merged["habitat_type"].fillna("unknown")
    merged["diet"] = merged["diet"].fillna("unknown")
    merged["conservation_status"] = merged["conservation_status"].fillna("unknown")

    return merged



# -----------------------------------------------------
# TASK E: Handle Missing Values (Second last digit = 3)
# Drop rows with ANY missing auxiliary metadata
# -----------------------------------------------------
def gamma_handle_missing(df):
    df = df[
        (df["habitat_type"] != "unknown") &
        (df["diet"] != "unknown") &
        (df["conservation_status"] != "unknown")
    ]
    return df



# -----------------------------------------------------
# RUN BLOCK
# -----------------------------------------------------
if __name__ == "__main__":
    print("\nLoading data...")
    zoo_df, class_df, metadata_df = gamma_load_and_integrate()

    print("Normalizing names (Task B)...")
    metadata_df = gamma_normalize_names(metadata_df)

    print("Fixing JSON inconsistencies (Task C)...")
    metadata_df = gamma_fix_json(metadata_df)

    print("Merging datasets (Task D)...")
    final_df = gamma_merge_datasets(zoo_df, metadata_df)

    print("Handling missing values (Task E)...")
    final_df = gamma_handle_missing(final_df)

    print("\n--- FINAL CLEANED DATASET (AFTER TASK E) ---")
    print(final_df.head(20))
