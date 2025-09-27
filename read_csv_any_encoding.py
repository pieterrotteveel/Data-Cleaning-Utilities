def read_csv_any_encoding(path: str, **kwargs) -> pd.DataFrame:
   
    encodings_to_try = []
    try:
        import chardet  
        raw = open(path, "rb").read(204800)
        guess = chardet.detect(raw).get("encoding") or "utf-8"
        encodings_to_try.append(guess)
    except Exception:
        pass

    encodings_to_try.extend(["utf-8", "utf-8-sig", "cp1252", "latin1"])

    last_err = None
    for enc in encodings_to_try:
        try:
            return pd.read_csv(path, encoding=enc, **kwargs)
        except Exception as e:
            last_err = e
            continue
    raise last_err  
