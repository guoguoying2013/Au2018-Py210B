#uint test?

from donor_models import *
import pytest

def test_donor_class():
    d = Donor("Bill Gates", 1000)
    assert d.name == "Bill Gates"
    assert d.donation == [1000]

def test_donorCollection_class():
    dc = DonorCollection()
    dc.add_new_donor("Bill Gates")
    with pytest.raises(ValueError):
        dc.add_new_donor("Bill Gates")
    
    dc.add_donation("Bill Gates", 1234)
    d = dc.get_donor("Bill Gates")
    assert d.num_donations == 1
    assert d.total_donations == 1234
    assert d.name == "Bill Gates"
