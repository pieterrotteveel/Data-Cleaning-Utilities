# Data-Cleaning-Utilities

Make column names consistent.
- case: 'snake' | 'lower' | 'upper' | 'title' | 'none'
- strip: trim whitespace
- dedup: ensure unique names by appending _1, _2, ...
- extra_transforms: pattern replacements applied BEFORE casing
Returns df with updated columns (in-place friendly).
Example:
  df = standardize_colnames(df)


Thin wrapper around DataFrame.rename with validation.
Example:
    df = rename_columns(df, {"old": "new"})



