from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title must be a non-empty string.")
    if len(title.strip()) > 100:
        raise ValueError("Title must be 100 characters or fewer.")
    return title.strip()


def validate_task_description(description):
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")
    if len(description.strip()) > 500:
        raise ValueError("Description must be 500 characters or fewer.")
    return description.strip()


def validate_due_date(due_date):
    try:
        parsed = datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
    if parsed.date() < datetime.today().date():
        raise ValueError("Due date cannot be in the past.")
    return due_date
