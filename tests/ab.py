import sys
import os

# Add the root directory (where app.py is) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

  # imports app instance from app.py

from app import le_warehouse, le_shipment, le_importance, le_gender

def test_label_encoders():
    assert le_warehouse.transform(["A"])[0] in range(5)
    assert le_shipment.transform(["Ship"])[0] in range(3)
    assert le_importance.transform(["low"])[0] in range(3)
    assert le_gender.transform(["F"])[0] in [0, 1]