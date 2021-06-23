import json
from linkedin_v2 import linkedin


cred = json.load(open('credentials.json'))

def main():
    application = linkedin.LinkedInApplication(token=cred['access_token'])
    profile = application.get_profile()
    print(profile)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[-] Error: {e}")
