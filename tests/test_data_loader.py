import numpy as np
import pandas as pd
import pytest
import sys #TODO fix path
sys.path.append('src/text_loader')
from loader import DataLoader

@pytest.fixture
def stub_df() -> pd.DataFrame:
    data = {
        "Party": ['Republican', 'Democrat', 'Republican'],
        "Tweet": ['blah!23564 https://hello.com', 'bloh@123skdjfps', 1234567]
    }
    return pd.DataFrame(data=data, index=[0,1, 2])

@pytest.fixture
def data_loader(mocker, stub_df):
    mocker.patch('pandas.read_csv', return_value=stub_df)
    return DataLoader()

def test_load_data(mocker, stub_df):
    data_loader = DataLoader()
    mocker.patch.object(data_loader, 'data',  stub_df)
    data_loader.load_data()
    assert not data_loader.data.empty, "Data should not be empty after loading."

def test_remove_characters(stub_df):
    text = stub_df['Tweet'].iloc[1]
    cleaned_text = DataLoader.remove_characters(text)
    assert cleaned_text == "blohskdjfps"

def test_clean_text(data_loader, stub_df):
    text = stub_df['Tweet'].iloc[0]
    cleaned_text = data_loader.clean_text(text)
    assert cleaned_text == "blah"

    text = stub_df['Tweet'].iloc[2]
    cleaned_text = data_loader.clean_text(text)
    assert cleaned_text == ""
