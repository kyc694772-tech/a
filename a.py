import subprocess
import sys

TOKEN = "eyJhIjoiZmZlZGI0YTg2ZDFiYzhiNzI2MmU0MDY4NDg3YWMzYmIiLCJ0IjoiOGZjNzQxYjItZTU5OC00MTZjLWE1YTMtYmY4MzUxZWQ4NDJhIiwicyI6Ik9HWXpNalV5TnpJdE9ERmtPUzAwWkdNekxUZ3pOVGN0WldOak5UbG1aVFJoTWpRMyJ9"

def install_cloudflared():
    try:
        subprocess.run(
            ["sudo", "cloudflared", "service", "install", TOKEN],
            check=True
        )
        print("✅ Cloudflared service installed successfully.")
    except subprocess.CalledProcessError as e:
        print("❌ Failed to install Cloudflared service.")
        sys.exit(e.returncode)

if __name__ == "__main__":
    install_cloudflared()
