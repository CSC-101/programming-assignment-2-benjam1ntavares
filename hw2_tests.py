import data
import hw2
import unittest
from data import *
from hw2 import shorter_duration_than


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1


    # test in quadrant II
    def test_create_rectangle1(self):
        point1 = Point(-5,5)
        point2 = Point(0,0)
        expected = Rectangle(Point(-5,5),Point(0,0))
        actual = hw2.create_rectangle(point1,point2)
        self.assertEqual(expected,actual)

    # test triangle crossing from quadrant II to quadrant 4
    # test if function can create rectangle without making assumptions about points.
    def test_create_rectangle2(self):
        point1 = Point(5,5)
        point2 = Point(-5,-5)
        expected = Rectangle(Point(-5,5),Point(5,-5))
        actual = hw2.create_rectangle(point1,point2)
        self.assertEqual(expected,actual)

    # test single point rectangle
    # test same x-points
    # test same y-points
    def test_create_rectangle3(self):
        point1 = Point(5,5)
        point2 = Point(5,5)
        expected = Rectangle(Point(5,5),Point(5,5))
        actual = hw2.create_rectangle(point1,point2)
        self.assertEqual(expected,actual)



    # Part 2



    # test shorter_duration_than True
    def test_shorter_duration_than1(self):
        duration1 = Duration(1, 20)
        duration2 = Duration(4, 19)
        expected = True
        actual = shorter_duration_than(duration1,duration2)
        self.assertEqual(expected,actual)



    # test shorter_duration_than = & False
    def test_shorter_duration_than2(self):
        duration1 = Duration(1, 20)
        duration2 = Duration(1, 20)
        expected = False
        actual = shorter_duration_than(duration1,duration2)
        self.assertEqual(expected,actual)



    # Part 3


    # test arbitrary values
    def test_song_shorter_than1(self):
        songs = [data.Song('Artist1', 'Title1', data.Duration(3, 21)),
                 data.Song('Artist2', 'Title2', data.Duration(1, 20)),
                 data.Song('Artist3', 'Title3', data.Duration(2, 21))]

        duration = data.Duration(2, 30)

        expected = [data.Song('Artist2', 'Title2', data.Duration(1, 20)),
                    data.Song('Artist3', 'Title3', data.Duration(2, 21))]

        actual = hw2.song_shorter_than(songs, duration)
        self.assertEqual(expected,actual)

    # test empty input list
    def test_song_shorter_than2(self):
        songs = []

        duration = data.Duration(2, 30)

        expected = []

        actual = hw2.song_shorter_than(songs, duration)
        self.assertEqual(expected,actual)




    # Part 4


    # arbitrary test of running_time
    def test_running_time1(self):
        songs = [data.Song('Artist1', 'Title1', data.Duration(3, 21)),
                 data.Song('Artist2', 'Title2', data.Duration(1, 20)),
                 data.Song('Artist3', 'Title3', data.Duration(2, 21)),
                 data.Song('Artist4', 'Title4', data.Duration(1, 20))]

        playlist = [0,1,2,3]

        expected = data.Duration(8, 22)
        actual = hw2.running_time(songs,playlist)

        self.assertEqual(actual,expected)

    # test empty list of song and or empty playlist
    def test_running_time2(self):
        songs = []
        playlist = []
        expected = data.Duration(0,0)
        actual = hw2.running_time(songs,playlist)
        self.assertEqual(actual,expected)

    # test list when all time values are given in seconds
    def test_running_time3(self):
        songs =[data.Song('Artist1', 'Title1', data.Duration(0, 100)),
                 data.Song('Artist2', 'Title2', data.Duration(0, 200)),
                 data.Song('Artist3', 'Title3', data.Duration(0, 300)),
                 data.Song('Artist4', 'Title4', data.Duration(0, 400))]

        playlist = [0,1,2,3]

        expected = data.Duration(16,39.6)
        actual = hw2.running_time(songs,playlist)
        self.assertEqual(actual.minutes,expected.minutes)
        self.assertAlmostEqual(actual.seconds,expected.seconds , places = -1) # approximate to 1s place


    # Part 5

    # arbitrarily test validate_route
    def test_validate_route1(self):
        city_links = [['san luis obispo', 'santa margarita'],
                      ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'],
                      ['atascadero', 'creston']]

        route = ['atascadero','santa margarita','pismo beach']

        expected = True
        actual = hw2.validate_route(city_links,route)
        self.assertEqual(expected,actual)

    # test validate route with one city in route
    def test_validate_route2(self):
        city_links = [['san luis obispo', 'santa margarita'],
                      ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'],
                      ['atascadero', 'creston']]

        route = ['san luis obispo']
        expected = True
        actual = hw2.validate_route(city_links,route)
        self.assertEqual(expected,actual)

    # test validate route with no cities in route
    def test_validate_route3(self):
        city_links = [['san luis obispo', 'santa margarita'],
                      ['san luis obispo', 'pismo beach'],
                      ['atascadero', 'santa margarita'],
                      ['atascadero', 'creston']]

        route = []
        expected = False
        actual = hw2.validate_route(city_links,route)
        self.assertEqual(expected,actual)
        

    # Part 6

    # arbitrary test
    def test_longest_repetition1(self):
        list_of_ints = [1,1,1,1,2,3,4,4,4,4,4]
        expected = 6
        actual = hw2.longest_repetition(list_of_ints)
        self.assertEqual(expected,actual)

    # test if there are no repetitions, or equal maximum repetitions
    def test_longest_repetition2(self):
        list_of_ints = [1,2,3,4,5]
        expected = None
        actual = hw2.longest_repetition(list_of_ints)
        self.assertEqual(expected,actual)


    # arbitrary test with two random, equal maximum repetitions
    def test_longest_repetition3(self):
        list_of_ints = [12,34,44,3,3,3,7,9,9,9,1]
        expected = None
        actual = hw2.longest_repetition(list_of_ints)
        self.assertEqual(expected,actual)









if __name__ == '__main__':
    unittest.main()
