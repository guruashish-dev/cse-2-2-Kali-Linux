def generate_report(username, sites, gps, score, level):

    report = f"""
=========== ShadowPersona Report ===========

Username Checked: {username}

Sites Found With Username: {sites}

GPS Metadata Found: {gps}

Human Exploitability Score: {score}

Risk Level: {level}

============================================
"""

    with open("reports/report.txt", "w") as file:
        file.write(report)

    print("Report saved to reports/report.txt")