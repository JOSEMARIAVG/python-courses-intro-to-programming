"""
Lesson: Python Lists
In this lesson, you'll learn how to work with Python lists.
"""

# -----------------------------
# Motivation
# -----------------------------
# Example: flower species names stored as a string
flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

print(type(flowers))  # Output: <class 'str'>
print(flowers)

# -----------------------------
# Storing data as a list
# -----------------------------
flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", 
                "sweet pea", "english marigold", "tiger lily", "moon orchid", 
                "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))  # Output: <class 'list'>
print(flowers_list)

# -----------------------------
# Length of a list
# -----------------------------
print("Number of flowers:", len(flowers_list))  # Output: 10

# -----------------------------
# Indexing
# -----------------------------
print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])
print("Last entry:", flowers_list[9])

# -----------------------------
# Slicing
# -----------------------------
print("First three entries:", flowers_list[:3])
print("Final two entries:", flowers_list[-2:])

# -----------------------------
# Removing items
# -----------------------------
flowers_list.remove("globe thistle")
print("After removal:", flowers_list)

# -----------------------------
# Adding items
# -----------------------------
flowers_list.append("snapdragon")
print("After adding:", flowers_list)

# -----------------------------
# Lists with other data types
# -----------------------------
# Example: hardcover book sales in the first week of April 2000
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]

print("Length of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))
print("Total books sold in one week:", sum(hardcover_sales))
print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)