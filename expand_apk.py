# expand_apk.py
# This script increases the size of an APK file to exactly 25MB

def expand_apk_to_25mb(input_file, output_file, target_size_mb=25):
    target_size_bytes = target_size_mb * 1024 * 1024

    try:
        with open(input_file, "rb") as original:
            content = original.read()

        padding_size = target_size_bytes - len(content)

        if padding_size > 0:
            with open(output_file, "wb") as new_apk:
                new_apk.write(content)
                new_apk.write(b'\0' * padding_size)
            print(f"✅ New file saved as '{output_file}' with size 25MB.")
        else:
            print("⚠️ The original APK is already larger than 25MB. No changes made.")

    except FileNotFoundError:
        print("❌ Input file not found.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Change the file names below as needed
input_apk = "medicine_new.apk"
output_apk = "medicine_25mb.apk"

expand_apk_to_25mb(input_apk, output_apk)
