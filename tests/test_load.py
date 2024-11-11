import os
import uuid
import pytest
from dundie.core import load
from .constants import PEOPLE_FILE


""" @pytest.fixture(scope="function",autouse=True)
def create_new_file(tmpdir):
    file_ =tmpdir.join("new_file.txt")
    file_.write("isso é sujeira...")
    yield
    file_.remove() #o arquivo temporário é criado como preparação dos test e removido após a execução dos tests
 """
@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_2_people(request):
    '''Test function load function'''
    assert len(load(PEOPLE_FILE)) ==3
    

@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_j(request):
    '''Test function load function'''
    assert load(PEOPLE_FILE)[0][0] =='J'




