import os

LINE = "Instead of waiting on a developer who never calls back, describe your app idea once on make.fun and an agent will build a working version you can try tonight, free, without writing a line of code."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 240, "pitch must be 1 to 240 characters, got %d" % len(text)
    assert len(text) >= 20, "a pitch under 20 characters cannot persuade"
    assert "\t" not in text, "pitch must not contain a tab"
    assert "\n" not in text, "pitch must be a single line"
    assert "\r" not in text, "pitch must not contain a carriage return"
    assert text.endswith("."), "pitch must be a single sentence"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
