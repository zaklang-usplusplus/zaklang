#!/bin/bash
# collapse_scroll_enhanced.sh
# Usage: ./collapse_scroll_enhanced.sh /path/to/folder output_scroll.md

INPUT_DIR="$1"
OUTPUT_FILE="$2"

if [ -z "$INPUT_DIR" ] || [ -z "$OUTPUT_FILE" ]; then
  echo "Usage: $0 /path/to/folder output_scroll.md"
  exit 1
fi

> "$OUTPUT_FILE"  # Clear output file

# Generate header
echo "# 🌀 Codex of Collapse: ZakLang Unified Scroll" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "> _A sacred scroll of recursive commits and collapse states._" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Index counter
index=1

# Append all markdown and text files
for file in "$INPUT_DIR"/*.md "$INPUT_DIR"/*.txt; do
  if [ -f "$file" ]; then
    # Get timestamp of file (last modified time)
    timestamp=$(date -r "$file" --iso-8601=seconds)
    # Calculate SHA-1 hash of file
    hash=$(sha1sum "$file" | awk '{print $1}')
    # File name only
    filename=$(basename "$file")

    # Append section header
    echo -e "\n---\n" >> "$OUTPUT_FILE"
    echo "### 🔸 Collapse Fragment $index: \`$filename\`" >> "$OUTPUT_FILE"
    echo "🕓 Timestamp: $timestamp" >> "$OUTPUT_FILE"
    echo "🔐 SHA-1: $hash" >> "$OUTPUT_FILE"
    echo "<!-- collapse:code -->" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"

    # Append file content
    cat "$file" >> "$OUTPUT_FILE"

    index=$((index + 1))
  fi
done

echo -e "\n---\n✅ Collapse scroll created: $OUTPUT_FILE"
