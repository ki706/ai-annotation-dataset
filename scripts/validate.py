
import json

VALID_SENTIMENTS = {"positive", "negative", "neutral"}
REQUIRED_FIELDS = {"id", "text", "sentiment", "category"}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_dataset(data):
    errors = []
    seen_ids = set()

    for item in data:
        item_id = item.get("id")

        # Check duplicate IDs
        if item_id in seen_ids:
            errors.append(f"Duplicate ID found: {item_id}")
        seen_ids.add(item_id)

        # Check required fields
        missing = REQUIRED_FIELDS - item.keys()
        if missing:
            errors.append(f"ID {item_id}: missing fields {missing}")

        # Check sentiment validity
        if "sentiment" in item and item["sentiment"] not in VALID_SENTIMENTS:
            errors.append(f"ID {item_id}: invalid sentiment '{item['sentiment']}'")

        # Check empty text
        if "text" in item and not item["text"].strip():
            errors.append(f"ID {item_id}: empty text field")

    return errors


def main():
    try:
        data = load_json("data/labeled.json")
    except FileNotFoundError:
        print("Error: labeled.json not found")
        return

    errors = validate_dataset(data)

    if not errors:
        print("Dataset validation passed. No issues found.")
    else:
        print(f"Found {len(errors)} issues:\n")
        for e in errors:
            print("-", e)


if __name__ == "__main__":
    main()
