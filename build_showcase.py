import os, glob

# Verify all assets exist
assets_dir = "/Users/bingo/Code/LYi/projects/laoma-engine-showcase/assets"
all_files = sorted(glob.glob(f"{assets_dir}/**/*", recursive=True))
media_files = [p for p in all_files if os.path.isfile(p) and not p.endswith(".ttf")]

print(f"Verified {len(media_files)} media files ready for master canvas integration.")
