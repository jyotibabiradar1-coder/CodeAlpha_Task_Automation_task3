"""
CodeAlpha Internship - Task 3: Task Automation with Python Scripts
Author: Intern
Description: A versatile Python script automating real-life repetitive tasks:
             1. File Organization: Moving .jpg files to an organized destination folder (os, shutil)
             2. Email Extraction: Extracting all email addresses from text files using Regex (re, file handling)
             3. Web Scraping: Fetching and saving page titles from websites (requests, re)
Key Concepts Used: os, shutil, re, requests, file handling.
"""

import os
import re
import shutil
import urllib.request
import requests


def move_jpg_files():
    """
    Automates moving all .jpg/.jpeg files from a source folder to a destination folder.
    Uses: os, shutil
    """
    print("\n" + "=" * 55)
    print("        1. AUTOMATE MOVING .JPG IMAGE FILES")
    print("=" * 55)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    default_src = os.path.join(base_dir, "source_folder")
    default_dest = os.path.join(base_dir, "jpg_destination_folder")

    print(f"Default source folder: {default_src}")
    print(f"Default destination folder: {default_dest}")

    use_default = input("Use default test folders? (y/n, default 'y'): ").strip().lower()
    if use_default in ("", "y", "yes"):
        src_folder = default_src
        dest_folder = default_dest
        # Create source directory with demo dummy files if empty
        os.makedirs(src_folder, exist_ok=True)
        demo_files = ["photo1.jpg", "vacation.jpg", "document.pdf", "notes.txt", "banner.jpeg"]
        for name in demo_files:
            file_path = os.path.join(src_folder, name)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"Sample content for {name}")
        print(f"[i] Initialized sample files in: {src_folder}")
    else:
        src_folder = input("Enter path to source folder: ").strip().strip('"').strip("'")
        dest_folder = input("Enter path to destination folder: ").strip().strip('"').strip("'")

    if not os.path.exists(src_folder):
        print(f"\n[!] Error: Source folder '{src_folder}' does not exist.\n")
        return

    os.makedirs(dest_folder, exist_ok=True)

    moved_count = 0
    valid_extensions = (".jpg", ".jpeg")

    print(f"\nScanning '{src_folder}' for .jpg files...")
    for filename in os.listdir(src_folder):
        file_path = os.path.join(src_folder, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(valid_extensions):
            dest_file_path = os.path.join(dest_folder, filename)
            # Handle filename collision if file already exists
            if os.path.exists(dest_file_path):
                base_name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(os.path.join(dest_folder, f"{base_name}_{counter}{ext}")):
                    counter += 1
                dest_file_path = os.path.join(dest_folder, f"{base_name}_{counter}{ext}")

            shutil.move(file_path, dest_file_path)
            print(f"  [->] Moved: {filename} -> {os.path.basename(dest_file_path)}")
            moved_count += 1

    print(f"\n[OK] Successfully moved {moved_count} image file(s) to '{dest_folder}'.\n")


def extract_email_addresses():
    """
    Automates extracting all email addresses from a text file using regular expressions
    and saving the unique list into an output file.
    Uses: re, file handling
    """
    print("\n" + "=" * 55)
    print("      2. EXTRACT EMAIL ADDRESSES FROM TEXT FILE")
    print("=" * 55)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    default_input = os.path.join(base_dir, "sample_text_with_emails.txt")
    default_output = os.path.join(base_dir, "extracted_emails.txt")

    # Create default input sample file if missing
    if not os.path.exists(default_input):
        sample_content = (
            "Contact our support team at support@codealpha.tech or services@codealpha.tech.\n"
            "For HR queries, write to careers@example.org or hr.department@company.co.in.\n"
            "You can also reach out to john.doe123@gmail.com or alice_smith@yahoo.com.\n"
            "Duplicate entry for testing: support@codealpha.tech\n"
        )
        with open(default_input, "w", encoding="utf-8") as f:
            f.write(sample_content)

    print(f"Default input file:  {default_input}")
    print(f"Default output file: {default_output}")

    use_default = input("Use default sample file? (y/n, default 'y'): ").strip().lower()
    if use_default in ("", "y", "yes"):
        input_file = default_input
        output_file = default_output
    else:
        input_file = input("Enter path to input .txt file: ").strip().strip('"').strip("'")
        output_file = input("Enter path for extracted emails output file: ").strip().strip('"').strip("'")

    if not os.path.isfile(input_file):
        print(f"\n[!] Error: Input file '{input_file}' not found.\n")
        return

    try:
        with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Regular expression pattern to match valid email addresses (requires valid alphabetic TLD)
        email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*[a-zA-Z]{2,}"
        found_emails = re.findall(email_pattern, content)

        # Remove duplicates while preserving alphabetical sorting
        unique_emails = sorted(list(set(email.lower() for email in found_emails)))

        if not unique_emails:
            print("\n[i] No email addresses found in the provided file.\n")
            return

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# Extracted Email Addresses ({len(unique_emails)} found)\n")
            f.write("=" * 45 + "\n")
            for email in unique_emails:
                f.write(email + "\n")

        print(f"\n[OK] Found {len(unique_emails)} unique email address(es):")
        for idx, email in enumerate(unique_emails, 1):
            print(f"    {idx}. {email}")
        print(f"\n[OK] Saved to: {output_file}\n")

    except IOError as e:
        print(f"\n[!] File I/O Error: {e}\n")


def scrape_webpage_title():
    """
    Automates scraping the <title> tag of a webpage and saving it to a text file.
    Uses: requests, re, file handling (with urllib fallback)
    """
    print("\n" + "=" * 55)
    print("         3. SCRAPE & SAVE WEBPAGE TITLE")
    print("=" * 55)

    default_url = "https://www.python.org"
    url_input = input(f"Enter webpage URL (default: {default_url}): ").strip()
    url = url_input if url_input else default_url

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print(f"\nFetching content from: {url} ...")
    html_content = ""

    # Try requests first, fallback to urllib
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) CodeAlphaBot/1.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        html_content = response.text
    except Exception as req_err:
        print(f"[i] Requests notice: {req_err}. Attempting fallback with urllib...")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                html_content = resp.read().decode("utf-8", errors="ignore")
        except Exception as url_err:
            print(f"\n[!] Failed to retrieve webpage: {url_err}\n")
            return

    # Extract title tag using regex
    match = re.search(r"<title[^>]*>(.*?)</title>", html_content, re.IGNORECASE | re.DOTALL)
    if match:
        title = match.group(1).strip()
        # Clean potential newlines or excessive whitespace in title
        title = " ".join(title.split())
        print(f"\n[OK] Scraped Page Title: \"{title}\"")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        output_file = os.path.join(base_dir, "scraped_title.txt")

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"URL: {url}\n")
                f.write(f"Page Title: {title}\n")
            print(f"[OK] Title saved to: {output_file}\n")
        except IOError as e:
            print(f"\n[!] Error saving title file: {e}\n")
    else:
        print("\n[!] Could not locate a <title> tag on the fetched page.\n")


def main():
    """Main CLI driver for Task Automation."""
    print("\n" + "=" * 55)
    print("      CODEALPHA - TASK AUTOMATION WITH PYTHON")
    print("=" * 55)

    while True:
        print("Choose an automation task to run:")
        print("  1. Move all .jpg files from a folder to a new folder")
        print("  2. Extract all email addresses from a .txt file")
        print("  3. Scrape and save the title of a webpage")
        print("  4. Run all three automation tasks in sequence")
        print("  5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_email_addresses()
        elif choice == "3":
            scrape_webpage_title()
        elif choice == "4":
            print("\n>>> Running Task 1: Move .jpg files...")
            move_jpg_files()
            print("\n>>> Running Task 2: Extract emails...")
            extract_email_addresses()
            print("\n>>> Running Task 3: Scrape webpage title...")
            scrape_webpage_title()
        elif choice == "5":
            print("\nExiting Task Automation Suite. Goodbye!\n")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
