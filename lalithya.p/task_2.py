import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("\n===== TASK 2 : EXPLORATORY DATA ANALYSIS (Column 4) =====\n")

# -------------------------------------------------------
# LOAD THE CLEANED DATASET FROM TASK–1
# -------------------------------------------------------
df = pd.read_csv("cleaned_dataset.csv")

print("Dataset Loaded Successfully!")
print("Shape:", df.shape)
print("\nColumns:", list(df.columns))


# -------------------------------------------------------
# 1. BAR PLOT WITH ERROR BARS – CLASS COUNTS
# -------------------------------------------------------
print("\nGenerating Bar Plot with Error Bars...")

plt.figure(figsize=(8,5))
class_counts = df["class_type"].value_counts()

# simple approximation of error = sqrt(n)
class_errors = class_counts ** 0.5

plt.bar(class_counts.index, class_counts.values, 
        yerr=class_errors, capsize=5)
plt.title("Class Counts with Error Bars")
plt.xlabel("Class Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


# -------------------------------------------------------
# 2. HEXBIN PLOT – TWO CONTINUOUS FEATURES
#    (legs vs catsize)
# -------------------------------------------------------
print("\nGenerating Hexbin Plot...")

plt.figure(figsize=(7,6))
plt.hexbin(df["legs"], df["catsize"], gridsize=20, cmap="Blues")
plt.xlabel("Legs")
plt.ylabel("Catsize")
plt.title("Hexbin Plot: Legs vs Catsize")
plt.colorbar(label="Count")
plt.tight_layout()
plt.show()


# -------------------------------------------------------
# 3. SWARM PLOT – CONSERVATION STATUS ACROSS CLASSES
# -------------------------------------------------------
print("\nGenerating Swarm Plot...")

plt.figure(figsize=(10,6))
sns.swarmplot(data=df, x="class_type", y="conservation_priority")
plt.title("Swarm Plot: Conservation Priority Across Classes")
plt.xlabel("Class Type")
plt.ylabel("Conservation Priority")
plt.tight_layout()
plt.show()


# -------------------------------------------------------
# 4. CLUSTERMAP – NUMERICAL FEATURES CORRELATION
# -------------------------------------------------------
print("\nGenerating Clustermap...")

numeric_df = df.select_dtypes(include=["int64", "float64"])

sns.clustermap(numeric_df.corr(), cmap="coolwarm")
plt.title("Numerical Features Clustermap", pad=80)
plt.show()

print("\n===== TASK 2 COMPLETED SUCCESSFULLY =====\n")
