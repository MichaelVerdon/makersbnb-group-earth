from lib.space import Space


"""
test the space class is initialized
"""
def test_space_initialization():
    space = Space(1,'Beach House', 'A beautiful beach house with ocean view.', 150, '2024-09-15', '2024-09-30', 3)
    assert space.id == 1
    assert space.name == 'Beach House'
    assert space.description == 'A beautiful beach house with ocean view.'
    assert space.price_per_night == 150
    assert space.availability_start == '2024-09-15'
    assert space.availability_end == '2024-09-30'
    assert space.user_id == 3

"""
test if there are two identical spaces 
"""
def test_spaces_equal():
    space_1=Space(1,'Beach House', 'A beautiful beach house with ocean view.', 150, '2024-09-15', '2024-09-30', 3)
    space_2=Space(1,'Beach House', 'A beautiful beach house with ocean view.', 150, '2024-09-15', '2024-09-30', 3)
    assert space_1==space_2


"""
test the space class is formatted nicely 
"""

def test_to_format_nicely():
    space=Space(1,'Beach House', 'A beautiful beach house with ocean view.', 150, '2024-09-15', '2024-09-30', 3)
    assert str(space) == "Space(1, Beach House, A beautiful beach house with ocean view., 150, 2024-09-15, 2024-09-30, 3)"
    # f"Space({self.id}, {self.name}, {self.description}, {self.price_per_night}, {self.availability_start}, {self.availability_end}, {self.user_id})"
