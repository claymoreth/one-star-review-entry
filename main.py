# Output contract: write one single-line one-star review of at most 160 characters
# to entry.txt, with no trailing newline.
import os

LINE = "One star. Sleep takes eight hours a night and gives nothing back. Would not recommend."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
