def to_numeric_cols(
    df: pd.DataFrame,
    cols: Sequence[str],
    locale: str = "auto", 
    percent: str = "leave",
    errors: str = "coerce",
) -> pd.DataFrame:
    for c in cols:
        s = df[c]
        if pd.api.types.is_numeric_dtype(s):
            continue

        ser = s.astype("string")
        if locale == "us":
            decimal, thousands = ".", ","
        elif locale == "eu":
            decimal, thousands = ",", "."
        elif locale == "auto":
            sample_vals = [str(x) for x in ser.dropna().head(200).tolist()]
            decimal, thousands = _infer_decimal_thousands(sample_vals) if sample_vals else (".", ",")
        else:
            raise ValueError("locale must be 'auto', 'us', or 'eu'")

        ser = ser.str.replace("\u00A0", "", regex=False).str.replace(" ", "", regex=False)

        ser = ser.str.replace(r"^\((.+)\)$", r"-\1", regex=True)

        if thousands:
            ser = ser.str.replace(thousands, "", regex=False)
        if decimal != ".":
            ser = ser.str.replace(decimal, ".", regex=False)

        had_percent = ser.str.contains("%", na=False)
        ser = ser.str.replace("%", "", regex=False)

        ser = ser.str.replace(r"[^0-9eE+\-\.]", "", regex=True)

        nums = pd.to_numeric(ser, errors=errors)

        if percent == "to_decimal":
            nums = nums.where(~had_percent, nums / 100.0)

        df[c] = nums
    return df
