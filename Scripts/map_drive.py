import os
import json

# Load the drive map
with open('/Volumes/akron/bear_projects/data/output/drive_map.json', 'r') as f:
    drive_map = json.load(f)

# Log file to store inaccessible paths
log_file = '/Volumes/akron/bear_projects/data/output/inaccessible_paths.log'

# Function to verify paths
def verify_paths(drive_map):
    with open(log_file, 'w') as log:
        for directory, contents in drive_map.items():
            for subdir, files in contents.items():
                for file in files:
                    filepath = os.path.join(directory, subdir, file)
                    if not os.path.exists(filepath):
                        log.write(f"Missing: {filepath}\n")
    print(f"Verification complete. Check the log at {log_file} for missing paths.")

# Run the verification
verify_paths(drive_map)
