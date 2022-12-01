from util import *
from collections import *
import unittest

class Misc(unittest.TestCase):

    def test_flatmap(self):
        self.assertEqual([4, 1, 4, 2, 4, 3], flatmap(lambda x: [4, x], [1, 2, 3]))

    def test_isinit(self):
        self.assertTrue(isint("2"))
        self.assertTrue(isint("123"))
        self.assertTrue(isint("-2"))
        self.assertTrue(isint("+2"))
        self.assertFalse(isint(""))
        self.assertFalse(isint("abc"))

    def test_tokens(self):
        self.assertEqual(["abc", "123", "-345", "def"], tokens("> abc 123 => -345, def"))

    def test_ints(self):
        self.assertEqual([123, -345], ints("> abc 123 => -345, def"))

    def test_initify(self):
        self.assertEqual(["abc", 123, -345, "def"], intify(["abc", "123", "-345", "def"]))

    def test_chunks(self):
        self.assertEqual([["abc", "123"], ["-345", "def"]], chunks(["abc", "123", "-345", "def"], 2))

    def test_digit(self):
        self.assertEqual(4, digit(456, 2))
        self.assertEqual(5, digit(456, 1))
        self.assertEqual(6, digit(456, 0))

    def test_binary(self):
        self.assertEqual("1011", binary(11))
        self.assertEqual("1011", binary("11"))

        self.assertEqual("00001011", binary(11, 8))
        self.assertEqual("00001011", binary("11", 8))

    def test_sign(self):
        self.assertEqual(1, sign(2))
        self.assertEqual(0, sign(0))
        self.assertEqual(0, sign(-0))
        self.assertEqual(-1, sign(-2))

    def test_msplit(self):
        self.assertEqual(["1", "2", "3"], msplit("1-2 3", "- "))
        self.assertEqual(["1", "2 3"], msplit("1-2 3", "-"))
        self.assertEqual(["1", "3"], msplit("1: 3", ": "))  # do not include empty substrings
        self.assertEqual(["1", "3"], msplit("1 3:", ": "))  # do not include empty substrings at the end

    def test_flatten(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_safe_remove(self):
        self.assertEqual([1, 3], safe_remove(2, [1, 2, 3]))
        self.assertEqual([1, 3], safe_remove(2, [1, 3]))
        self.assertEqual(set([1, 3]), safe_remove(2, set([1, 2, 3])))
        self.assertEqual(set([1, 3]), safe_remove(2, set([1, 3])))

    def test_manhattan(self):
        self.assertEqual(13, manhattan((5, 8)))
        self.assertEqual(13, manhattan(5, 8))
        self.assertEqual(10, manhattan((1, 2), (5, 8)))
        self.assertEqual(10, manhattan(1, 2, 5, 8))

    def test_line_intersection(self):
        self.assertEqual((5, 5), line_intersection(((0, 0), (10, 10)), ((10, 0), (0, 10))))
        self.assertEqual((5, 5), line_intersection(((10, 0), (0, 10)), ((0, 0), (10, 10))))
        self.assertEqual((5, 5), line_intersection(((5, 0), (5, 10)), ((0, 5), (10, 5))))

        with self.assertRaises(Exception):
            line_intersection(((0, 0), (10, 0)), ((0, 5), (10, 5)))

    def test_topsort(self):
        g = {'A': ['ORE'], 'C': ['B', 'A'], 'B': ['ORE'], 'E': ['D', 'A'], 'D': ['C', 'A'], 'FUEL': ['E', 'A']}
        self.assertEqual(['FUEL', 'E', 'D', 'C', 'A', 'B', 'ORE'], top_sort(g, "FUEL"))
        self.assertEqual(['C', 'A', 'B', 'ORE'], top_sort(g, "C"))

    def test_bfs(self):
        g = {'A': ['ORE'], 'C': ['B', 'A'], 'B': ['ORE'], 'E': ['D', 'A'], 'D': ['C', 'A'], 'FUEL': ['E', 'A']}
        self.assertEqual(['FUEL', 'A', 'ORE'], bfs(g, "FUEL", lambda x: x == "ORE"))

    def test_bfs_all_paths(self):
        g = {'A': ['ORE'], 'C': ['B', 'A'], 'B': ['ORE'], 'E': ['D', 'A'], 'D': ['C', 'A'], 'FUEL': ['E', 'A']}
        self.assertEqual([
            ['FUEL', 'A', 'ORE'],
            ['FUEL', 'E', 'A', 'ORE'],
            ['FUEL', 'E', 'D', 'A', 'ORE'],
            ['FUEL', 'E', 'D', 'C', 'B', 'ORE'],
            ['FUEL', 'E', 'D', 'C', 'A', 'ORE']
            ],
                bfs_all_paths(g, "FUEL", lambda x: x == "ORE"))

    def test_dijkstra(self):
        graph = {
            "start": {"A": 2, "B": 1},
            "A": {"B": 1, "C": 2},
            "B": {"C": 5},
            "C": {"end": 1},
        }

        p, c = dijkstra(graph, "start", "end")

        self.assertEqual(['start', 'A', 'C', 'end'], p)
        self.assertEqual(5, c)

    def test_astar(self):
        maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        graph = maze_to_graph(maze, (0, 0), lambda _, __, ___, x: not x)

        self.assertEqual([(0, 0), (1, 1), (2, 2), (3, 3), (3, 4), (4, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0)], astar(graph, (0, 0), (5, 0)))

    def test_flood_fill(self):
        xs = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

        s = flood_fill(xs, 0, 0, lambda c: c == 1, 2)

        self.assertEqual(3, s)


    def test_transpose(self):
        self.assertEqual([[1, 4, 7], [2, 5, 8], [3, 6, 9]], transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_transpositions(self):
        self.assertEqual(set([("12", "34"),
                              ("21", "43"),
                              ("34", "12"),
                              ("43", "21"),
                              ("13", "24"),
                              ("24", "13"),
                              ("31", "42"),
                              ("42", "31")]), set(map(tuple, transpositions(["12", "34"]))))

        self.assertEqual(set([((1, 2), (3, 4)),
                              ((2, 1), (4, 3)),
                              ((3, 4), (1, 2)),
                              ((4, 3), (2, 1)),
                              ((1, 3), (2, 4)),
                              ((2, 4), (1, 3)),
                              ((3, 1), (4, 2)),
                              ((4, 2), (3, 1))]), set(map(tuple, transpositions([(1, 2), (3, 4)]))))

        self.assertEqual(set([("123", "456"),
                              ("321", "654"),
                              ("456", "123"),
                              ("654", "321"),
                              ("14", "25", "36"),
                              ("41", "52", "63"),
                              ("36", "25", "14"),
                              ("63", "52", "41")]), set(map(tuple, transpositions(["123", "456"]))))



    def test_in_grid(self):
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.assertTrue(in_grid(grid, 0, 0))
        self.assertTrue(in_grid(grid, 1, 1))
        self.assertTrue(in_grid(grid, 1, 1))
        self.assertTrue(in_grid(grid, 2, 2))

        self.assertFalse(in_grid(grid, 0, -1))
        self.assertFalse(in_grid(grid, -1, 0))
        self.assertFalse(in_grid(grid, 3, 0))
        self.assertFalse(in_grid(grid, 0, 3))

    def test_grid(self):
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        #self.assertEqual([(1, 0), (1, 2), (0, 1), (2, 1)], list(iter_grid(grid)))

    def test_iter_orthogonal(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        self.assertEqual([(1, 0), (1, 2), (0, 1), (2, 1)], list(iter_orthogonal(1, 1)))
        self.assertEqual([(1, 0, 2), (1, 2, 8), (0, 1, 4), (2, 1, 6)], list(iter_orthogonal(1, 1, grid)))

        self.assertEqual( [(0, -1), (0, 1), (-1, 0), (1, 0)], list(iter_orthogonal(0, 0)))
        self.assertEqual( [(0, 1, 4), (1, 0, 2)], list(iter_orthogonal(0, 0, grid)))

    def test_iter_adjacent(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        self.assertEqual([(1, 0), (1, 2), (0, 1), (2, 1), (0, 0), (0, 2), (2, 0), (2, 2)], list(iter_adjacent(1, 1)))
        self.assertEqual([(1, 0, 2), (1, 2, 8), (0, 1, 4), (2, 1, 6), (0, 0, 1), (0, 2, 7), (2, 0, 3), (2, 2, 9)], list(iter_adjacent(1, 1, grid)))

        self.assertEqual( [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)], list(iter_adjacent(0, 0)))
        self.assertEqual( [(0, 1, 4), (1, 0, 2), (1, 1, 5)], list(iter_adjacent(0, 0, grid)))

    def test_grid_to_dict(self):
        grid = [[1, 2], [3, 4]]

        self.assertEqual({(0, 0): 1, (0, 1): 3, (1, 0): 2, (1, 1): 4}, grid_to_dict(grid))

    def test_grid_get(self):
        grid = [[1, 2], [3, 4]]

        self.assertEqual(1, grid_get(grid, 0, 0))
        self.assertEqual(4, grid_get(grid, 1, 1))
        self.assertEqual(None, grid_get(grid, -1, 0))
        self.assertEqual("foo", grid_get(grid, -1, 0, "foo"))

    def test_maze_to_graph(self):
        maze = [".#.",
                "...",
                ".#."]

        self.assertEqual({
            (0, 1): [(0, 0), (0, 2), (1, 1)],
            (0, 0): [(0, 1), (1, 1)],
            (2, 1): [(2, 0), (2, 2), (1, 1)],
            (1, 1): [(0, 1), (2, 1), (0, 0), (0, 2), (2, 0), (2, 2)],
            (2, 0): [(2, 1), (1, 1)],
            (2, 2): [(2, 1), (1, 1)],
            (0, 2): [(0, 1), (1, 1)]},
            maze_to_graph(maze, (0, 0), lambda _, __, ___, x: x == "."))

    def test_binary_search(self):
        self.assertEqual((123455, 123456), binary_search(0, 10000000, lambda x: x >= 123456))

    def test_lcm(self):
        self.assertEqual(12, lcm(4, 6))

    def test_chinese_remainder(self):
        self.assertEqual(23, chinese_remainder([3, 5, 7], [2, 3, 2]))
        self.assertEqual(4, chinese_remainder([2, 3], [0, 1]))

    def test_mul_inv(self):
        self.assertEqual(2, mul_inv(8, 3))

    def test_reduce_unique_options(self):
        self.assertEqual({0: 1, 1: 2, 2: 3}, reduce_unique_options({0: [1, 2, 3], 1: [2], 2: [2, 3]}))
        self.assertEqual({0: 1, 1: 2, 2: 3}, reduce_unique_options({0: {1, 2, 3}, 1: {2}, 2: {2, 3}}))

    def test_max_bipartite_matching(self):

        self.assertEqual({0: 1, 2: 0, 3: 2, 4: 3, 5: 5}, max_bipartite_matching({0: [1, 2], 1: [], 2: [0, 3], 3: [2], 4: [3, 4], 5: [5]}))

        # trival example where not all applicants can be assigned a job
        self.assertEqual({0: 1}, max_bipartite_matching({0: [1], 1: [1]}))

        # for trivial cases, max_bipartite_matching and reduce_unique_options should give the same result
        graph = {0: [1, 2, 3], 1: [2], 2: [2, 3]}
        expected = {0: 1, 1: 2, 2: 3}
        self.assertEqual(expected, max_bipartite_matching(graph))
        self.assertEqual(expected, reduce_unique_options(graph))


if __name__ == '__main__':
    unittest.main()
