def getPartOfday(h):
    return (
        "morning"
        if 1 <= h <= 11
        else "afternoon"
        if 12 <= h <= 17
        else "evening"
    )