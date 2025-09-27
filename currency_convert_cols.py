def currency_convert_cols(
    df: pd.DataFrame,
    cols: Sequence[str],
    fx: float,
    inverse: bool = False,
    round_to: Optional[int] = None,
) -> pd.DataFrame:
  
    if inverse:
        factor = 1.0 / float(fx)
    else:
        factor = float(fx)
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors="coerce") * factor
        if round_to is not None:
            df[c] = df[c].round(round_to)
    return df
