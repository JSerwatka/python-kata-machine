"""Translated from `kata-machine-js/src/__tests__/Map.ts`."""


def test_map(import_algorithm):
    map_cls = import_algorithm("Map")
    map_instance = map_cls()
    map_instance.set("foo", 55)
    assert map_instance.size() == 1
    map_instance.set("fool", 75)
    assert map_instance.size() == 2
    map_instance.set("foolish", 105)
    assert map_instance.size() == 3
    map_instance.set("bar", 69)
    assert map_instance.size() == 4
    assert map_instance.get("bar") == 69
    assert map_instance.get("blaz") is None
    map_instance.delete("barblabr")
    assert map_instance.size() == 4
    map_instance.delete("bar")
    assert map_instance.size() == 3
    assert map_instance.get("bar") is None
