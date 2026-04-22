import subprocess

def scan_metadata(image_path):
    try:
        result = subprocess.run(
            ["exiftool", image_path],
            capture_output=True,
            text=True
        )

        output = result.stdout

        if "GPS Latitude" in output or "GPS Longitude" in output:
            print("GPS metadata detected!")
            return True

        print("No GPS metadata found.")
        return False

    except Exception as e:
        print("Metadata scan error:", e)
        return False