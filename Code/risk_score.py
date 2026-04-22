def calculate_risk(username_sites, gps_found):

    score = 0

    if username_sites > 10:
        score += 3

    if gps_found:
        score += 4

    if score >= 7:
        level = "HIGH"
    elif score >= 3:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level