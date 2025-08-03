# Define prototype structure
prototype_pages = [
    "Welcome Screen",
    "Lists (Home Page)",
    "Create New List",
    "View/Edit List",
    "Settings"
]

# Define flow as tuples (From Page -> To Page)
page_flow = [
    ("Welcome Screen", "Shopping Lists (Home Page)"),
    ("Lists (Home Page)", "Create New List"),
    ("Lists (Home Page)", "View/Edit List"),
    ("Lists (Home Page)", "Settings"),
    ("View/Edit List", "Add Item"),
    ("View/Edit List", "Edit/Delete Item")
]

# display page structure
print("=== Shopping List App Prototype ===\n")
print(f"Total Pages: {len(prototype_pages)}\n")
print("Page Names:")
for i, page in enumerate(prototype_pages, 1):
    print(f"{i}. {page}")

print("\nPage Flow:")
for start, end in page_flow:
    print(f"{start} -> {end}")