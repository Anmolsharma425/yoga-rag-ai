import nbformat

input_path = "yogaaillm.ipynb"
output_path = "yogaaillm.ipynb"

# Load the notebook
nb = nbformat.read(input_path, as_version=4)

# Remove widgets metadata
if "widgets" in nb.metadata:
    print("Removing widgets metadata...")
    del nb.metadata["widgets"]

# Save to a new file
nbformat.write(nb, output_path)
print(f"Cleaned notebook saved as: {output_path}")
