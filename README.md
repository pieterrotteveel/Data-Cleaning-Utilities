# DataFrame Helper Functions

A collection of utility functions for cleaning, reshaping, and transforming Pandas DataFrames.  
This document describes each function, what it does, and its inputs.

---

## 1. `standardize_colnames(df, case="snake", strip=True, dedup=True, extra_transforms=None)`
**Description:** Cleans and standardizes column names (consistent casing, removes spaces, ensures uniqueness).  
- **df** → DataFrame to update  
- **case** → `"snake"`, `"lower"`, `"upper"`, `"title"`, `"none"` (naming style)  
- **strip** → `True/False`, trim whitespace  
- **dedup** → `True/False`, append `_1`, `_2` for duplicate names  
- **extra_transforms** → list of `(pattern, replacement)` before casing  

---

## 2. `rename_columns(df, mapping)`
**Description:** Renames columns with validation (safe wrapper for `df.rename`).  
- **df** → DataFrame  
- **mapping** → dict `{old_name: new_name}`  

---

## 3. `drop_fields(df, cols)`
**Description:** Safely drops unwanted columns.  
- **df** → DataFrame  
- **cols** → list of column names to remove  

---

## 4. `to_long(df, id_vars, value_vars)`
**Description:** Converts wide → long format (wrapper over `pd.melt`).  
- **df** → DataFrame  
- **id_vars** → columns to keep as identifiers  
- **value_vars** → columns to unpivot into rows  

---

## 5. `to_wide(df, index, names_from, values_from)`
**Description:** Converts long → wide format (wrapper over `pivot_table`).  
- **df** → DataFrame  
- **index** → columns to use as row index  
- **names_from** → column whose values become column names  
- **values_from** → column whose values fill the table  

---

## 6. `split_column(df, col, into, sep=" ")`
**Description:** Splits a text column into multiple new columns.  
- **df** → DataFrame  
- **col** → column to split  
- **into** → list of new column names  
- **sep** → string or regex used for splitting  

---

## 7. `merge_columns(df, cols, new_col, sep=", ", how="join", drop=True)`
**Description:** Merges multiple columns into one.  
- **df** → DataFrame  
- **cols** → list of columns to combine  
- **new_col** → name of new merged column  
- **sep** → separator string when joining  
- **how** → `"first_nonnull"` (first non-empty value) or `"join"` (string join)  
- **drop** → `True/False`, remove original columns  

---

## 8. `to_bool_cols(df, cols)`
**Description:** Converts truthy/falsey values (like "yes", "no", 1, 0) to boolean. Unknown/blank → `NaN`.  
- **df** → DataFrame  
- **cols** → list of columns to convert  

---

## 9. `infer_number_format(samples)`
**Description:** Guesses decimal and thousands separators from number strings.  
- **samples** → list/Series of example strings  
- **Returns** → `(decimal_separator, thousands_separator_or_None)`  

---

## 10. `to_numeric_cols(df, cols, locale="auto", percent="ignore", errors="coerce")`
**Description:** Cleans messy numeric text and converts to float. Handles `%`, decimal, and thousands separators.  
- **df** → DataFrame  
- **cols** → list of columns to convert  
- **locale** → `"auto"`, `"eu"`, `"us"` (decimal format style)  
- **percent** → `"to_decimal"` (convert %) or `"ignore"`  
- **errors** → `"coerce"` (set bad values to NaN) or `"raise"`  

---

## 11. `to_datetime_cols(df, cols, dayfirst=False, fmt=None, utc=False)`
**Description:** Robustly parses date/time columns.  
- **df** → DataFrame  
- **cols** → list of columns to convert  
- **dayfirst** → `True` for EU-style dates (31/12/2024)  
- **fmt** → strftime format string (faster if known)  
- **utc** → `True/False`, convert to UTC  

---

## 12. `read_csv_utf8(path, **kwargs)`
**Description:** Reads a CSV file, auto-detects encoding, outputs UTF-8 DataFrame.  
- **path** → file path to CSV  
- **kwargs** → extra options for `pd.read_csv`  

---

## 13. `rewrite_utf8(path)`
**Description:** Rewrites a text file as UTF-8, best effort.  
- **path** → input file path  
- **Returns** → output file path in UTF-8  

---

## 14. `percent_to_decimal(series)`
**Description:** Converts percentages into decimals.  
- `"5%"` → `0.05`  
- `5` → `0.05`  
- `0.05` → `0.05`  
- **series** → Series/column to convert  

---

## 15. `bps_to_decimal(series)`
**Description:** Converts basis points to decimals.  
- `100` or `"100bps"` → `0.01`  
- **series** → Series/column to convert  

---

## 16. `decimal_to_bps(series)`
**Description:** Converts decimals to basis points.  
- `0.01` → `100`  
- **series** → Series/column to convert  

---

## 17. `currency_convert_cols(df, cols, fx, inverse=False, round_to=None)`
**Description:** Converts currency columns using exchange rates.  
- **df** → DataFrame  
- **cols** → list of columns to convert  
- **fx** → exchange rate (target_per_source, e.g. EUR/USD=0.92)  
- **inverse** → `False`: multiply; `True`: divide  
- **round_to** → decimals to round result  

---
