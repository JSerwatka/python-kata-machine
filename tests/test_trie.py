"""Translated from `kata-machine-js/src/__tests__/Trie.ts`."""


def test_trie(import_algorithm):
    trie_cls = import_algorithm("Trie")
    trie = trie_cls()
    trie.insert("foo")
    trie.insert("fool")
    trie.insert("foolish")
    trie.insert("bar")
    assert sorted(trie.find("fo")) == ["foo", "fool", "foolish"]
    trie.delete("fool")
    assert sorted(trie.find("fo")) == ["foo", "foolish"]
