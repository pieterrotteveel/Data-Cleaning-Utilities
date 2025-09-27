
def ensure_utf8_file(src_path: str, dst_path: Optional[str] = None) -> str:
   
    if dst_path is None:
        if src_path.lower().endswith(".txt"):
            dst_path = src_path[:-4] + "_utf8.txt"
        else:
            dst_path = src_path + ".utf8"

    encodings_to_try = []
    try:
        import chardet  
        raw = open(src_path, "rb").read(204800)
        guess = chardet.detect(raw).get("encoding") or "utf-8"
        encodings_to_try.append(guess)
    except Exception:
        pass

    encodings_to_try.extend(["utf-8", "utf-8-sig", "cp1252", "latin1"])

    last_err = None
    for enc in encodings_to_try:
        try:
            with open(src_path, "r", encoding=enc, errors="strict") as f:
                text = f.read()
            with open(dst_path, "w", encoding="utf-8", newline="") as f:
                f.write(text)
            return dst_path
        except Exception as e:
            last_err = e
            continue
    raise last_err  
