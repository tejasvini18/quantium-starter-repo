import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

def test_header_present():
    layout = app.layout
    header = layout.children[0]
    assert header.children == "Pink Morsels Sales Dashboard"

def test_visualisation_present():
    layout = app.layout
    graph = layout.children[2]
    assert graph.id == "sales-chart"

def test_region_picker_present():
    layout = app.layout
    radio_container = layout.children[1]
    radio = radio_container.children[1]
    assert radio.id == "region-filter"
