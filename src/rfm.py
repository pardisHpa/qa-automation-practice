"""Customer segment rules based on recency (R) and frequency (F)."""


def segment(recency_days: int, frequency: int) -> str:
    if recency_days < 0 or frequency < 0:
        raise ValueError("recency_days and frequency must not be negative")

    if recency_days <= 30 and frequency >= 5:
        return "Champion"
    if recency_days <= 60 and frequency >= 3:
        return "Loyal"
    if recency_days <= 180:
        return "At risk"
    return "Lost"


# (recency_days, frequency, expected segment), shared by unit and browser tests
CASES = [
    (10, 8, "Champion"),
    (30, 5, "Champion"),
    (31, 5, "Loyal"),
    (45, 3, "Loyal"),
    (61, 3, "At risk"),
    (120, 1, "At risk"),
    (180, 0, "At risk"),
    (181, 9, "Lost"),
]
