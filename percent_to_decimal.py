def percent_to_decimal(series: Union[pd.Series, Sequence[Union[str, float, int]]]) -> pd.Series:
   
    s = pd.Series(series)

    def _one(x):
        if pd.isna(x):
            return np.nan
        if isinstance(x, str):
            xs = x.strip()
            if xs.endswith("%"):
                try:
                    return float(xs[:-1].replace(",", ".").replace(" ", "")) / 100.0
                except Exception:
                    return np.nan
            try:
                val = float(xs.replace(",", ".").replace(" ", ""))
                return val / 100.0 if val >= 1.0 else val
            except Exception:
                return np.nan
        try:
            val = float(x)
            return val / 100.0 if val >= 1.0 else val
        except Exception:
            return np.nan
    return s.map(_one).astype(float)
