shopping_list = []

def show_hints():
  print("What should we pick up at the store today?")
  print("""
        Enter 'DONE' to stop adding items.
        Enter 'HELP' to re-show these hints.
        Enter 'SHOW' to see your current list.
        """)


def add_to_list(item):
  shopping_list.append(item)
  print(f"Added! List has {len(shopping_list)} items.")


def show_list():
  print("Here's your list:")
  for item in shopping_list:
    print(item)

show_hints()

while True:
  new_item = input(">  ")

  if new_item == "DONE":
    break
  elif new_item == "HELP":
    show_hints()
    continue
  elif new_item == 'SHOW':
    show_list()
    continue

  add_to_list(new_item)

show_list()