def process_file():
    try:
        filename = input("Enter the filename to read: ")

        with open(filename, "r") as f:
            text = f.read()

        word_count = len(text.split())
        modified_text = text.upper()

        output_file = "output.txt"
        with open(output_file, "w") as f:
            f.write("Processed Text:\n")
            f.write(modified_text + "\n\n")
            f.write(f"Word Count: {word_count}\n")

        print(f"Successfully processed {filename} and wrote to {output_file}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


process_file()
