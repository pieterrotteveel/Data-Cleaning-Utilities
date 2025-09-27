def standardize_column_names(
    df: pd.DataFrame,
    case: str = "snake",
    strip: bool = True,
    dedup: bool = True,
    extra_transforms: Optional[Mapping[str, str]] = None,
) -> pd.DataFrame:
    cols = list(df.columns)

    def _apply_extra(s: str) -> str:
        if extra_transforms:
            for pat, repl in extra_transforms.items():
                s = re.sub(pat, repl, s)
        return s

    def _to_snake(s: str) -> str:
        s = re.sub(r"[^0-9A-Za-z]+", "_", s)
        s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)  
        s = re.sub(r"__+", "_", s)
        s = s.strip("_").lower()
        return s

    new_cols = []
    for c in cols:
        s = str(c)
        if strip:
            s = s.strip()
        s = _apply_extra(s)

        if case == "snake":
            s = _to_snake(s)
        elif case == "lower":
            s = s.lower()
        elif case == "upper":
            s = s.upper()
        elif case == "title":
            s = s.title()
        elif case == "none":
            s = s
        else:
            raise ValueError("case must be one of: snake, lower, upper, title, none")

        new_cols.append(s)

    if dedup:
        seen: Dict[str, int] = {}
        deduped = []
        for s in new_cols:
            if s not in seen:
                seen[s] = 0
                deduped.append(s)
            else:
                seen[s] += 1
                deduped.append(f"{s}_{seen[s]}")
        new_cols = deduped

    df.columns = new_cols
    return df

