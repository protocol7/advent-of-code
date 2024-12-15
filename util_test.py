from util import *
from collections import *
import unittest

class Utils(unittest.TestCase):

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
        self.assertEqual([123, 345], ints("> abc 123 => -345, def", negatives=False))

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

    def test_window(self):
        self.assertEqual([(1, 2), (2, 3), (3, 4), (4, 5)], window([1, 2, 3, 4, 5]))

    def test_takeuntil(self):
        self.assertEqual([0, 1, 2, 3], takeuntil(lambda x: x == 3, [0, 1, 2, 3, 3, 4]))

    def test_item(self):
        self.assertEqual(1, item([1]))
        self.assertEqual(1, item({1}))

        with self.assertRaises(Exception):
            item([1, 2])
        with self.assertRaises(Exception):
            item([])

        self.assertEqual(1, item(iter([1])))

        with self.assertRaises(Exception):
            item(iter([1, 2]))
        with self.assertRaises(Exception):
            item(iter([]))

    def test_agg_each(self):
        self.assertEqual([4, 3], agg_each([[1, 2], [3, 1]], lambda a, b: a + b))
        self.assertEqual([4, 3], max_each([[1, 1], [2, 3], [4, 2]]))
        self.assertEqual([1, 1, 0], min_each([[1, 1, 2], [2, 3, 0], [4, 2, 1]]))

    def test_diffrange(self):
        self.assertEqual([1, 2, 3], diffrange(1, 3))
        self.assertEqual([3, 2, 1], diffrange(3, 1))
        self.assertEqual([1], diffrange(1, 1))

    def test_safe_remove(self):
        self.assertEqual([1, 3], safe_remove(2, [1, 2, 3]))
        self.assertEqual([1, 3], safe_remove(2, [1, 3]))
        self.assertEqual(set([1, 3]), safe_remove(2, set([1, 2, 3])))
        self.assertEqual(set([1, 3]), safe_remove(2, set([1, 3])))

    def test_circular_list(self):
        xx = CircularList([0, 1, 2, 3])

        self.assertEqual(xx[0], 0)
        self.assertEqual(xx[4], 0)
        self.assertEqual(xx[5], 1)
        self.assertEqual(xx[-1], 3)

        self.assertEqual(xx.pop(0), 0)
        self.assertEqual(xx.xs, [1, 2, 3])

        xx.insert(0, 4)
        self.assertEqual(xx.xs, [4, 1, 2, 3])

        xx.insert(4, 5)
        self.assertEqual(xx.xs, [5, 4, 1, 2, 3])

        xx.move_by(1, 2)
        self.assertEqual(xx.xs, [5, 1, 2, 4, 3])

        xx.move_by(3, 2)
        self.assertEqual(xx.xs, [5, 4, 1, 2, 3])

        xx.move_by(1, -2)
        self.assertEqual(xx.xs, [5, 1, 2, 4, 3])

        xx.move_by(1, 0)
        self.assertEqual(xx.xs, [5, 1, 2, 4, 3])

        # move_to
        xx.move_to(0, 2)
        self.assertEqual(xx.xs, [1, 2, 5, 4, 3])

        xx.move_to(3, 0)
        self.assertEqual(xx.xs, [4, 1, 2, 5, 3])

        xx.move_to(3, 3)
        self.assertEqual(xx.xs, [4, 1, 2, 5, 3])

        xx.move_to(1, -1)
        self.assertEqual(xx.xs, [4, 2, 5, 1, 3])

        xx.move_to(1, -2)
        self.assertEqual(xx.xs, [4, 5, 2, 1, 3])

        xx = CircularList([0, 1, 2, 3, 4])
        xx.rotate(1)
        self.assertEqual(xx.xs, [1, 2, 3, 4, 0])

        xx.rotate(2)
        self.assertEqual(xx.xs, [3, 4, 0, 1, 2])

        xx.rotate(7)
        self.assertEqual(xx.xs, [0, 1, 2, 3, 4])

        xx.rotate(-2)
        self.assertEqual(xx.xs, [3, 4, 0, 1, 2])

    def test_manhattan(self):
        self.assertEqual(13, manhattan((5, 8)))
        self.assertEqual(13, manhattan(5, 8))
        self.assertEqual(10, manhattan((1, 2), (5, 8)))
        self.assertEqual(10, manhattan(1, 2, 5, 8))

    def test_topo_sort(self):
        g = {'A': ['ORE'], 'C': ['B', 'A'], 'B': ['ORE'], 'E': ['D', 'A'], 'D': ['C', 'A'], 'FUEL': ['E', 'A']}
        self.assertEqual(['FUEL', 'E', 'D', 'C', 'A', 'B', 'ORE'], topo_sort(g, "FUEL"))
        self.assertEqual(['C', 'A', 'B', 'ORE'], topo_sort(g, "C"))

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
        graph = Grid(maze).to_graph((0, 0), lambda _, __, ___, x: x == 0, neighbours=ADJACENT)

        self.assertEqual([(0, 0), (1, 1), (2, 2), (3, 3), (3, 4), (4, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0)], astar(graph, (0, 0), (5, 0)))

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

    def test_binary_search(self):
        self.assertEqual((123455, 123456), binary_search(0, 10000000, lambda x: x >= 123456))

    def test_bit_functions(self):
        b = 0
        self.assertFalse(bit_test(b, 3))

        b = bit_set(b, 3)
        self.assertTrue(bit_test(b, 3))

        b = bit_unset(b, 3)
        self.assertFalse(bit_test(b, 3))

        b = bit_flip(b, 3)
        self.assertTrue(bit_test(b, 3))

        self.assertFalse(bit_test(b, 2))
        b = bit_flip_all(b)
        self.assertTrue(bit_test(b, 2))
        self.assertFalse(bit_test(b, 3))

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

    def test_interval(self):
        interval = Interval(1, 12)

        with self.assertRaises(Exception):
            Interval(2, 1)

        self.assertIn(1, interval)
        self.assertIn(12, interval)
        self.assertIn(6, interval)
        self.assertNotIn(0, interval)
        self.assertNotIn(13, interval)

        interval2 = Interval(2, 11)
        self.assertIn(interval2, interval)
        self.assertIn(interval, interval)
        self.assertNotIn(interval, interval2)

        self.assertEqual(interval & Interval(0, 3), Interval(1, 3))
        self.assertEqual(interval & Interval(10, 13), Interval(10, 12))

        self.assertTrue(interval.intersects(interval))
        self.assertTrue(interval.intersects(Interval(3, 4)))
        self.assertTrue(Interval(3, 4).intersects(interval))
        self.assertTrue(interval.intersects(Interval(1, 1)))
        self.assertTrue(Interval(1, 1).intersects(interval))
        self.assertTrue(interval.intersects(Interval(12, 12)))
        self.assertTrue(Interval(12, 12).intersects(interval))
        self.assertFalse(Interval(13, 15).intersects(interval))
        self.assertFalse(interval.intersects(Interval(13, 15)))

        self.assertEqual(interval & Interval(3, 4), Interval(3, 4))
        self.assertEqual(interval & Interval(0, 14), Interval(1, 12))
        self.assertEqual(interval & Interval(0, 1), Interval(1, 1))
        self.assertEqual(interval & Interval(1, 1), Interval(1, 1))
        self.assertEqual(interval & Interval(12, 14), Interval(12, 12))
        self.assertEqual(interval & Interval(12, 12), Interval(12, 12))
        self.assertIsNone(interval & Interval(13, 15))

        self.assertEqual(interval | Interval(0, 3), Interval(0, 12))
        self.assertEqual(interval | Interval(0, 1), Interval(0, 12))
        self.assertEqual(interval | Interval(11, 13), Interval(1, 13))
        self.assertEqual(interval | Interval(12, 13), Interval(1, 13))
        self.assertEqual(interval | Interval(13, 15), Interval(1, 15)) # union with adjacent
        self.assertIsNone(interval | Interval(14, 15))

        self.assertEqual(interval.range(), range(1, 13))
        self.assertEqual(interval.set(), {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12})

        self.assertTrue(interval)
        self.assertTrue(Interval(1, 1))

        self.assertEqual(len(Interval(1, 1)), 1)
        self.assertEqual(len(interval), 12)

        self.assertEqual(str(interval), "1..12")

        self.assertLess(Interval(1, 2), Interval(4, 5))
        self.assertLess(Interval(1, 7), Interval(4, 5))

        self.assertEqual([4, 5, 6], list(iter(Interval(4, 6))))

    def test_intervals(self):
        intervals = Intervals([Interval(1, 2)])
        intervals.add(Interval(4, 5))

        self.assertEqual([Interval(1, 2), Interval(4, 5)], intervals.intervals)

        intervals.add(Interval(2, 4))
        self.assertEqual([Interval(1, 5)], intervals.intervals)

        intervals.add(Interval(6, 7)) # adjacent
        self.assertEqual([Interval(1, 7)], intervals.intervals)

        intervals.add(Interval(-2, -1)) # adjacent
        self.assertEqual([Interval(-2, -1), Interval(1, 7)], intervals.intervals) # ensure intervals are sorted

        self.assertEqual((intervals & Interval(-1, 4)).intervals, [Interval(-1, -1), Interval(1, 4)])
        self.assertEqual((intervals & Interval(2, 4)).intervals, [Interval(2, 4)])

    def test_point(self):
        self.assertTrue(Point(1, 0) < Point(0, 1))
        self.assertTrue(Point(1, 0) < Point(0, 2))
        self.assertFalse(Point(0, 2) < Point(1, 0))

    def test_line(self):
        self.assertEqual((5, 5), Line((0, 0), (10, 10)).intersection(Line((10, 0), (0, 10))))
        self.assertEqual((5, 5), Line((10, 0), (0, 10)).intersection(Line((0, 0), (10, 10))))
        self.assertEqual((5, 5), Line((5, 0), (5, 10)).intersection(Line((0, 5), (10, 5))))

        self.assertIsNone(Line((0, 0), (10, 0)).intersection(Line((0, 5), (10, 5))))

    def test_grid(self):
        g = Grid(
            [
                [1, 2],
                [3, 4],
                [5, 6],
            ]
        )

        self.assertEqual([(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)], [p for p, _ in g.points()])
        self.assertEqual([0,0], g.min())
        self.assertEqual([1, 2], g.max())
        self.assertEqual(6, len(g.points()))
        self.assertEqual((Point(0, 0), 1), g.points()[0])
        self.assertEqual((Point(1, 2), 6), g.points()[-1])

        self.assertIn((0, 0), g)
        self.assertIn(Point(0, 0), g)
        self.assertIn((1, 2), g)
        self.assertNotIn((2, 2), g)
        self.assertNotIn((1, 3), g)

        self.assertEqual([((0, -1), None), ((0, 1), 3), ((-1, 0), None), ((1, 0), 2)], g.orthogonal((0, 0)))

        self.assertEqual({(0, 0): 1, (1, 0): 2, (0, 1): 3, (1, 1): 4, (0, 2): 5, (1, 2): 6}, g.to_dict())
        self.assertEqual([[1, 2], [3, 4], [5, 6]], g.to_grid())

    def test_maze_to_graph(self):
        maze = [".#.",
                "...",
                ".#."]

        g = Grid(maze)

        self.assertEqual({
                (0, 0): [(0, 1)],
                (2, 0): [(2, 1)],

                (0, 1): [(0, 0), (0, 2), (1, 1)],
                (1, 1): [(0, 1), (2, 1)],
                (2, 1): [(2, 0), (2, 2), (1, 1)],

                (0, 2): [(0, 1)],
                (2, 2): [(2, 1)],
            },
            g.to_graph((0, 0), lambda _, __, ___, x: x == "."))

    def test_flood_fill(self):
        g = Grid([[0, 0, 1], [0, 1, 0], [1, 0, 0]])

        s = g.flood_fill((0, 0), lambda c: c == 1, 2)

        self.assertEqual(3, s)
        self.assertEqual(2, g[(0, 0)])
        self.assertEqual(2, g[(0, 1)])
        self.assertEqual(2, g[(1, 0)])
        self.assertEqual(0, g[(2, 2)])


if __name__ == '__main__':
    unittest.main()
