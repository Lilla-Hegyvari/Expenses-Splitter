import pandas as pd
import pytest
from tempfile import NamedTemporaryFile
from splitter_final import filter_expenses_by_date, split_expenses

sample_data = {
    "Date": ["2024-07-01", "2024-07-15", "2024-08-10", "2024-09-01"],
    "Description": ["Dinner", "Coffee", "Drinks", "Concert"],
    "cost": [20, 5, 30, 80],
    "Paid by": ["Anna", "Emma", "Lily", "Bob"],
    "Anna": [1, 0, 1, 1],
    "Emma": [1, 1, 1, 0],
    "Lily": [0, 1, 0, 1],
}

@pytest.fixture
def temp_excel_file():
    # Convert sample data to DataFrame and write to a temporary Excel file
    df = pd.DataFrame(sample_data)
    df["Date"] = pd.to_datetime(df["Date"])  # Convert Date column to datetime
    with NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
        df.to_excel(tmp.name, index=False)
        yield tmp.name

def test_filter_expenses_by_date(temp_excel_file):
    filtered = filter_expenses_by_date(temp_excel_file, "2024-07-01", "2024-08-21")
    assert len(filtered) == 3
    assert all(filtered["Date"] <= pd.to_datetime("2024-08-21"))
    assert all(filtered["Date"] >= pd.to_datetime("2024-07-01"))

def test_split_expenses_full(temp_excel_file):
    balances = split_expenses(temp_excel_file)
    assert isinstance(balances, dict)
    assert "Anna" in balances
    assert round(sum(balances.values()), 2) == 0

def test_split_expenses_filtered(temp_excel_file):
    balances = split_expenses(temp_excel_file, "2024-07-01", "2024-08-21")
    assert isinstance(balances, dict)
    assert "Emma" in balances
    assert round(sum(balances.values()), 2) == 0
