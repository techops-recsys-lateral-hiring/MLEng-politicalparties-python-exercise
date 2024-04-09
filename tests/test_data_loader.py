import numpy as np
import pandas as pd
import pytest
import sys #TODO fix path
sys.path.append('src/text_loader')
from loader import DataLoader

@pytest.fixture
def mock_df() -> pd.DataFrame:
    data = {
        "Party": ['Republican', 'Democrat', 'Republican'],
        "Tweet": ['blah!23564 https://hello.com', 'bloh@123skdjfps', 1234567]
    }
    df = pd.DataFrame(data=data, index=[0,1, 2])
    return df

@pytest.fixture
def data_loader(mocker, mock_df):
    mocker.patch('pandas.read_csv', return_value=mock_df)
    return DataLoader()

def test_load_data(mocker, mock_df):
    data_loader = DataLoader()
    mocker.patch.object(data_loader, 'data',  mock_df)
    data_loader.load_data()
    assert not data_loader.data.empty, "Data should not be empty after loading."

def test_remove_characters(mock_df):
    text = mock_df['Tweet'].iloc[1]
    cleaned_text = DataLoader.remove_characters(text)
    assert cleaned_text == "blohskdjfps"

def test_clean_text(data_loader, mock_df):
    text = mock_df['Tweet'].iloc[0]
    cleaned_text = data_loader.clean_text(text)
    assert cleaned_text == "blah"

    text = mock_df['Tweet'].iloc[2]
    cleaned_text = data_loader.clean_text(text)
    assert cleaned_text == ""
    

