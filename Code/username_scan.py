import subprocess

def scan_username(username):
    try:
        print("Running Sherlock scan...")

        result = subprocess.run(
            ["sherlock", username],
            capture_output=True,
            text=True
        )

        output = result.stdout

        sites_found = output.count("Found")

        print("Sites found:", sites_found)

        return sites_found

    except Exception as e:
        print("Error during username scan:", e)
        return 0