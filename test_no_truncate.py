import re

with open("/Users/bingo/Code/LYi/projects/laoma-engine-showcase/index.html") as f:
    text = f.read()

# Verify how many truncate classes exist
print("Occurrences of truncate:", len(re.findall(r"\btruncate\b", text)))
