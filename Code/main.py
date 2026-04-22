from username_scan import scan_username
from metadata_scan import scan_metadata
from risk_score import calculate_risk
from report import generate_report

print("=== ShadowPersona Digital Exposure Scanner ===")

username = input("Enter username to scan: ")
image_path = input("Enter image path (press Enter to skip): ")

print("\n[+] Scanning username exposure...")
sites = scan_username(username)

gps_found = False
if image_path:
    print("\n[+] Scanning image metadata...")
    gps_found = scan_metadata(image_path)

print("\n[+] Calculating risk score...")
score, level = calculate_risk(sites, gps_found)

print("\n[+] Generating report...")
generate_report(username, sites, gps_found, score, level)

print("\n✔ Scan completed. Check reports/report.txt")