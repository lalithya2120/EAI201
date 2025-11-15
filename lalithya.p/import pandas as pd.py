import pandas as pd
import json

def gamma_load_and_integrate():
    """
    Loads zoo.csv, class.csv, and auxiliary_metadata.json
    Handles encoding issues, corrupted JSON fields, and normalizes metadata.
    Returns: zoo_df, class_df, metadata_df
    """

    # --------------------------
    # 1. Load zoo.csv safely
    # --------------------------
    try:
        zoo_df = pd.read_csv("/mnt/data/zoo.csv", encoding="utf-8")
    except UnicodeDecodeError:
        zoo_df = pd.read_csv("/mnt/data/zoo.csv", encoding="latin-1")

    # --------------------------
    # 2. Load class.csv
    # --------------------------
    class_df = pd.read_csv("/mnt/data/class.csv")

    # --------------------------
    # 3. Load & clean JSON metadata
    # --------------------------
    with open("/mnt/data/auxiliary_metadata.json", "r") as f:
        metadata = json.load(f)

    cleaned_metadata = []

    for entry in metadata:
        fixed = {}

        # Animal name
        fixed["animal_name"] = entry.get("animal_name", "").strip().lower()

        # Habitat (handle multiple inconsistent keys)
        fixed["habitat"] = (
            entry.get("habitat")
            or entry.get("habitats")
            or "unknown"
        )
        fixed["habitat"] = fixed["habitat"].strip().lower()

        # Diet field (fix misspellings, alternate keys)
        diet = entry.get("diet") or entry.get("diet_type") or "unknown"
        diet = diet.strip().lower()

        # Fix common typos
        if diet == "omnivor":
            diet = "omnivore"
        fixed["diet"] = diet

        # Conservation status (multiple possible key names)
        fixed["conservation_status"] = (
            entry.get("conservation_status")
            or entry.get("conservation")
            or entry.get("status")
            or "unknown"
        )
        fixed["conservation_status"] = fixed["conservation_status"].strip().lower()

        cleaned_metadata.append(fixed)

    metadata_df = pd.DataFrame(cleaned_metadata)

    # --------------------------
    # Return all cleaned DataFrames
    # --------------------------
    return zoo_df, class_df, metadata_df
