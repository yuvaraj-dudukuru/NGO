"""Tests for the ShopVerse cleaning pipeline."""

import sys
from pathlib import Path

import pandas as pd

# Make src/ importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from clean_orders import clean, make_raw_orders  # noqa: E402


def test_raw_has_known_issues():
    raw = make_raw_orders()
    assert raw.shape == (7, 6)
    assert not pd.api.types.is_numeric_dtype(raw["Amount"])   # text, not numeric
    assert raw.duplicated(subset=["OrderID"]).sum() == 1


def test_no_duplicates_after_clean():
    df = clean(make_raw_orders())
    assert df.duplicated(subset=["OrderID"]).sum() == 0


def test_no_missing_after_clean():
    df = clean(make_raw_orders())
    assert df.isnull().sum().sum() == 0


def test_no_negative_amounts():
    df = clean(make_raw_orders())
    assert (df["Amount"] < 0).sum() == 0


def test_correct_types():
    df = clean(make_raw_orders())
    assert pd.api.types.is_numeric_dtype(df["Amount"])
    assert pd.api.types.is_datetime64_any_dtype(df["OrderDate"])


def test_text_standardized():
    df = clean(make_raw_orders())
    assert set(df["City"]).issubset({"Pune", "Mumbai", "Delhi"})
    # No leading/trailing whitespace remains
    assert (df["Customer"] == df["Customer"].str.strip()).all()


def test_expected_row_count():
    # 7 raw - 1 duplicate - 1 negative amount = 5
    df = clean(make_raw_orders())
    assert len(df) == 5


def test_total_column():
    df = clean(make_raw_orders())
    assert (df["Total"] == df["Amount"] * df["Quantity"]).all()
