from src.deep_search.deep_search import Graph


def test_linear():
    """1 - 2 - 3"""
    graph = Graph([1, 2, 3, 4], [(1, 2), (2, 3), (3, 4)])
    dfs_result = graph.dfs()
    assert set(dfs_result) == {1, 2, 3, 4}


def test_branched():
    graph = Graph([1, 2, 3, 4, 5], [(1, 2), (1, 3), (2, 4), (4, 5)])
    dfs_result = graph.dfs()
    assert set(dfs_result) == {1, 2, 3, 4, 5}


def test_disconnected():
    graph = Graph([1, 2, 3, 4], [(1, 2), (3, 4)])
    dfs_result = graph.dfs()
    assert set(dfs_result) == {1, 2, 3, 4}


def test_single():
    graph = Graph([1], [])
    dfs_result = graph.dfs()
    assert dfs_result == [1]


def test_empty():
    graph = Graph([], [])
    dfs_result = graph.dfs()
    assert dfs_result == []


def test_dfs_order():
    graph = Graph([1, 2, 3, 4], [(1, 2), (2, 3), (3, 4), (1, 4)])
    dfs_result = graph.dfs()
    assert set(dfs_result) == {1, 2, 3, 4}


def test_complex():
    graph = Graph([1, 2, 3, 4, 5], [(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)])
    dfs_result = graph.dfs()
    assert set(dfs_result) == {1, 2, 3, 4, 5}


def test_sun():
    graph = Graph([1, 2, 3, 4, 5, 6], [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)])
    dfs_result = graph.dfs()
    assert set(dfs_result) == {1, 2, 3, 4, 5, 6}
