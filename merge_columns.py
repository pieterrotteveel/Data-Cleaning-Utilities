def merge_columns(
    df: pd.DataFrame,
    cols: Sequence[str],
    dest: str,
    sep: str = " ",
    how: str = "first_nonnull",
    drop: bool = False,
) -> pd.DataFrame:
    if how not in {"first_nonnull", "join"}:
        raise ValueError("how must be 'first_nonnull' or 'join'")

    if how == "first_nonnull":
        df[dest] = df[list(cols)].bfill(axis=1).iloc[:, 0]
    else:
        df[dest] = (
            df[list(cols)]
            .astype("string")
            .apply(lambda row: sep.join([x for x in row if pd.notna(x) and str(x).strip() != ""]), axis=1)
            .replace("", pd.NA)
        )
    if drop:
        df = df.drop(columns=list(cols))
    return df
