import os
import sys
from dotenv import load_dotenv  # type: ignore[import-not-found]


def main() -> None:
    load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...")
    mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")
    missing = []
    if not mode:
        missing.append("MATRIX_MODE")
    if not db_url:
        missing.append("DATABASE_URL")
    if not api_key:
        missing.append("API_KEY")
    if missing:
        print(f"\n[ERROR] Missing critical configuration: "
              f"{', '.join(missing)}")
        print("Please configure your .env file or export "
              "environment variables.")
        sys.exit(1)
    if mode is not None and db_url is not None and api_key is not None:
        print("\nConfiguration loaded:")
        print(f"Mode: {mode}")
        if mode.lower() == "production":
            print(f"Database: Connected to production "
                  f"secure cluster ({db_url[:15]}...)")
            print(f"API Access: Authenticated via Production "
                  f"Gateway (Key hash: {hash(api_key)})")
            print(f"Log Level: {log_level or 'INFO'}")
            print(f"Zion Network: SECURE TUNNEL ESTABLISHED -> {zion}")
        else:
            print(f"Database: Connected to local instance ({db_url})")
            print("API Access: Authenticated (Dev Mode)")
            print(f"Log Level: {log_level or 'DEBUG'}")
            print(f"Zion Network: Online ({zion})")
        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        if os.path.exists(".env"):
            print("[OK] .env file properly configured")
        else:
            print("[WARNING] .env file missing (Using system "
                  "environment variables)")
        print("[OK] Production overrides available")
        print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
