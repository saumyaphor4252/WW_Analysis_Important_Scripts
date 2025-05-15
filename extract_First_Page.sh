#!/bin/bash

# Define output folder
OUTPUT_DIR="first_pages"

# Check if qpdf is installed
if ! command -v qpdf &> /dev/null; then
    echo "Error: qpdf is not installed. Install it using: sudo apt install qpdf (Linux) or brew install qpdf (Mac)."
    exit 1
fi

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Process all PDF files in the current directory
for pdf in *.pdf; do
    # Skip if no PDF files are found
    [ -e "$pdf" ] || continue
   
    #filename="${pdf%.pdf}"

    # Extract the first page and save to output folder
    #output_file="$OUTPUT_DIR/${filename}_page1.pdf"
    output_file="$OUTPUT_DIR/${pdf%.pdf}_page1.pdf"
    qpdf "$pdf" --pages . 1 -- "$output_file"

    echo "Extracted first page of '$pdf' -> '$output_file'"
done

echo "Extraction complete. Check the '$OUTPUT_DIR' folder."
