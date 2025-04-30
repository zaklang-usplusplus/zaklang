#!/bin/bash
# add_toc.sh
# Usage: ./add_toc.sh input_scroll.md

INPUT_FILE="$1"
TOC_TEMP_FILE="toc_temp_$$.md"
FINAL_TEMP_FILE="scroll_with_toc_$$.md"

if [ -z "$INPUT_FILE" ]; then
  echo "Usage: $0 input_scroll.md"
  exit 1
fi

# Extract all section headers that match '### 🔸 Collapse Fragment'
grep -n '^### 🔸 Collapse Fragment' "$INPUT_FILE" | while IFS= read -r line; do
  line_number=$(echo "$line" | cut -d: -f1)
  header_text=$(echo "$line" | cut -d: -f2- | sed 's/### 🔸 Collapse Fragment /- /; s/`//g')
  anchor=$(echo "$header_text" | sed 's/[^a-zA-Z0-9]/-/g' | tr '[:upper:]' '[:lower:]')
  echo "$header_text ([link](#${anchor}))"
done > "$TOC_TEMP_FILE"

# Insert TOC after the initial header section (after the "---" line)
awk -v tocfile="$TOC_TEMP_FILE" '
  BEGIN { inserted=0 }
  {
    print $0
    if (!inserted && /^---$/) {
      print ""
      print "## 📚 Collapse Scroll Index"
      print ""
      while ((getline line < tocfile) > 0) {
        print line
      }
      print ""
      inserted=1
    }
  }
' "$INPUT_FILE" > "$FINAL_TEMP_FILE"

# Move the final result over the original
mv "$FINAL_TEMP_FILE" "$INPUT_FILE"
rm "$TOC_TEMP_FILE"

echo "✅ Table of Contents inserted into: $INPUT_FILE"
