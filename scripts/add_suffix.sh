#!/bin/bash

# function to add suffix to all files in a directory
rename_files() {
  local dir="$1"
  cd "$dir"
  # iterate through all files in directory
  for file in *; do
    # check if file is a directory
    if [[ -d "$file" ]]; then
      # if file is a directory, recurse into it
      rename_files "$file"
    else
      # if file is not a directory, add suffix to filename
      suffix=$(basename "$dir")
      mv "$file" "${suffix}_${file}"
    fi
  done
  cd ..
}

# start renaming files from the current directory
rename_files "."


