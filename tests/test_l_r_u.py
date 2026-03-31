"""Translated from `kata-machine-js/src/__tests__/LRU.ts`."""


def test_lru(import_algorithm):
    lru_cls = import_algorithm("LRU")
    lru = lru_cls(3)
    assert lru.get("foo") is None
    lru.update("foo", 69)
    assert lru.get("foo") == 69

    lru.update("bar", 420)
    assert lru.get("bar") == 420

    lru.update("baz", 1337)
    assert lru.get("baz") == 1337

    lru.update("ball", 69420)
    assert lru.get("ball") == 69420
    assert lru.get("foo") is None
    assert lru.get("bar") == 420
    lru.update("foo", 69)
    assert lru.get("bar") == 420
    assert lru.get("foo") == 69
    assert lru.get("baz") is None
