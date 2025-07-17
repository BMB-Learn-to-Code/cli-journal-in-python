import datetime
entries = []


def add_items():
    new_story = input("Enter your entry for today:\n")
    new_date = datetime.datetime.now()
    entries.append({"content": new_story, "date": new_date })

def view_items():
    for entry in entries:
        print(f"{entry['date'].strftime('%Y-%m-%d')} - {entry['content']}\n")
