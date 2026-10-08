"""
Automated Git Push Utility for SalaryScope India to GitHub.
Uses pure-Python Dulwich Git engine (no git.exe required).
Target: https://github.com/cherlapallyvivekvardhan-ai/gemzz
"""

import sys
import os
import getpass
from dulwich import porcelain

REPO_PATH = os.path.dirname(os.path.abspath(__file__))
GITHUB_REPO_URL = "github.com/cherlapallyvivekvardhan-ai/gemzz.git"


def push_repo(token=None):
    if not token:
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        
    if not token and len(sys.argv) > 1:
        token = sys.argv[1].strip()
        
    if not token:
        print("\n" + "="*60)
        print("GitHub Authentication Required")
        print("="*60)
        print("To push to https://github.com/cherlapallyvivekvardhan-ai/gemzz,")
        print("please generate a GitHub Personal Access Token (classic or fine-grained)")
        print("with 'repo' permissions at: https://github.com/settings/tokens\n")
        try:
            token = input("Enter your GitHub Personal Access Token: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nPush cancelled.")
            return False

    if not token:
        print("Error: Token cannot be empty.")
        return False

    auth_url = f"https://{token}@{GITHUB_REPO_URL}"
    print(f"\nPushing to https://github.com/cherlapallyvivekvardhan-ai/gemzz...")
    
    try:
        # Push to remote main branch
        porcelain.push(REPO_PATH, auth_url, b"refs/heads/master:refs/heads/main")
        print("Push succeeded on refs/heads/main!")
        return True
    except Exception as e_master:
        try:
            porcelain.push(REPO_PATH, auth_url, b"refs/heads/main:refs/heads/main")
            print("Push succeeded on main branch!")
            return True
        except Exception as e_main:
            print("\nPush Failed:")
            print("Error details:", str(e_main))
            print("\nTroubleshooting tips:")
            print("1. Ensure your GitHub Personal Access Token has 'repo' (full control of private repositories) permissions.")
            print("2. Ensure the repository cherlapallyvivekvardhan-ai/gemzz is owned by or accessible to your token.")
            return False


if __name__ == "__main__":
    success = push_repo()
    if success:
        print("\nRepository successfully uploaded to GitHub:")
        print("https://github.com/cherlapallyvivekvardhan-ai/gemzz")
    sys.exit(0 if success else 1)
