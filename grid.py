import os
import subprocess
import time
from datetime import datetime

# ITTIHAD in 5:4 ratio (5 weeks wide, 4 days high)
commit_dates = [
    '2025-06-01', '2025-06-04', '2025-06-08', '2025-06-11', '2025-06-15', '2025-06-16', 
    '2025-06-17', '2025-06-18', '2025-06-22', '2025-06-25', '2025-06-29', '2025-07-02', 
    '2025-07-13', '2025-07-20', '2025-07-27', '2025-07-28', '2025-07-29', '2025-07-30', 
    '2025-08-03', '2025-08-10', '2025-08-24', '2025-08-31', '2025-09-07', '2025-09-08', 
    '2025-09-09', '2025-09-10', '2025-09-14', '2025-09-21', '2025-10-05', '2025-10-08', 
    '2025-10-12', '2025-10-15', '2025-10-19', '2025-10-20', '2025-10-21', '2025-10-22', 
    '2025-10-26', '2025-10-29', '2025-11-02', '2025-11-05', '2025-11-16', '2025-11-17', 
    '2025-11-18', '2025-11-19', '2025-11-25', '2025-12-02', '2025-12-09', '2025-12-14', 
    '2025-12-15', '2025-12-16', '2025-12-17', '2025-12-29', '2025-12-30', '2025-12-31', 
    '2026-01-04', '2026-01-06', '2026-01-11', '2026-01-13', '2026-01-18', '2026-01-20', 
    '2026-01-26', '2026-01-27', '2026-01-28', '2026-02-08', '2026-02-09', '2026-02-10', 
    '2026-02-11', '2026-02-15', '2026-02-18', '2026-02-22', '2026-02-25', '2026-03-01', 
    '2026-03-04', '2026-03-09', '2026-03-10'
]

# Set up your Git name and email
GIT_AUTHOR_NAME = "tayesh"
GIT_AUTHOR_EMAIL = "tayesh32@gmail.com"

def run_cmd(command, env=None):
    result = subprocess.run(command, shell=True, env=env, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error:", result.stderr)
    return result.stdout.strip()

def make_commit_on_date(date_str):
    full_datetime = f"{date_str}T12:00:00"
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = full_datetime
    env["GIT_COMMITTER_DATE"] = full_datetime
    env["GIT_AUTHOR_NAME"] = GIT_AUTHOR_NAME
    env["GIT_AUTHOR_EMAIL"] = GIT_AUTHOR_EMAIL
    env["GIT_COMMITTER_NAME"] = GIT_AUTHOR_NAME
    env["GIT_COMMITTER_EMAIL"] = GIT_AUTHOR_EMAIL

    run_cmd('git commit --allow-empty -m "Commit on {}"'.format(date_str), env=env)

# Loop through all dates and commit
for date in commit_dates:
    print(f"Committing on {date}...")
    make_commit_on_date(date)

print("\n✅ All commits done! You can now push with:")
print("   git push origin main --force")
