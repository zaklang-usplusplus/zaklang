#!/bin/bash
# split_git_log_by_commit_numbered.sh
# Usage: ./split_git_log_by_commit_numbered.sh full_git_log.txt output_directory/

INPUT_FILE="$1"
OUTPUT_DIR="$2"

if [ -z "$INPUT_FILE" ] || [ -z "$OUTPUT_DIR" ]; then
  echo "Usage: $0 full_git_log.txt output_directory/"
  exit 1
fi

# Get absolute path to input before cd
ABS_INPUT_FILE=$(readlink -f "$INPUT_FILE")

mkdir -p "$OUTPUT_DIR"
cd "$OUTPUT_DIR" || exit 1

# Split by 'commit ' line; number sequentially starting from 001
csplit -s -f raw_commit_ -b "%03d.txt" "$ABS_INPUT_FILE" '/^commit /' '{*}'

# Rename raw files with prefix commit_###.txt
count=1
for file in raw_commit_*.txt; do
  newname=$(printf "commit_%03d.txt" "$count")
  mv "$file" "$newname"
  count=$((count + 1))
done

echo "✅ Git log split and renamed from oldest to newest in $(pwd)"
