import sys
sys.path.append('../src/')
import os
import pytest
from src.articles import Articles

FIXTURE = 'test_data.fixture.json'

@pytest.fixture
def test_data():
    fixture = os.path.join(os.path.dirname(__file__), FIXTURE)
    return Articles(fixture)

def test_list_query_returns_full_lists(test_data):
    assert len(test_data.get_filtered_view()) == 4

def test_list_query_returns_no_body(test_data):
    articles = test_data.get_filtered_view()
    for article in articles:
        assert "body" not in article

def test_api_returns_detail_on_id(test_data):
        article = test_data.get_filtered_detail({'newid':'4'})
        print(article)
        assert article['newid'] == '4'

# def test_api_returns_body_in_detail(test_data):
#         article = test_data.get_filtered_detail({'newid': '4'})
#         assert "body" in article



# def test_obj_returns_id_and_detail(test_data):
#     assert test_data.get_filtered_detail({'newid': '4'})['newid'] == '4'

# def test_obj_returns_filter_by_place(test_data):
#     articles = test_data.find_all({'meta.people': 'dude1'})
#     for article in articles:
#         print(article['meta'])
#         assert 'dude1' in article['meta']['people']

# def test_logic_returns_fulltext(test_data):
#     articles = test_data.find_all({'meta.people': 'dude1'})
#     for article in articles:
#         print(article['meta'])
#         assert 'dude1' in article['meta']['people']
