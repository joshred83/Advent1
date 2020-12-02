

with open("expense_report") as f:
    expense_entries = [int(entry.strip()) for entry in f.readlines()]

for idx, entry1 in zip(range(len(expense_entries)), expense_entries):
  for idx2, entry2 in zip(range(idx, len(expense_entries[idx + 1:])),expense_entries[idx + 1:]):
    for entry3 in expense_entries[idx2 + 1:]:
      if entry1 + entry2 + entry3 == 2020:
        print(entry1 * entry2 * entry3)
      
