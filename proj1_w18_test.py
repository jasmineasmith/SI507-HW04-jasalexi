import unittest
import proj1_w18 as proj1

class TestMedia(unittest.TestCase):

    def testConstructor(self):
        m1 = proj1.Media()
        m2 = proj1.Media(trackName="1999", artistName="Prince")

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
class TestSong(unittest.TestCase):
	def testSongconst(self):
		s1 = proj1.Song()
		s2 = proj1.Song(primaryGenreName="Rock")

		self.assertEqual(s1.title, "No Title")
		self.assertEqual(s1.author, "No Author")
		self.assertEqual(s1.album, "No Album")
		self.assertEqual(s1.t_len, "No track length")
		self.assertEqual(s2.gen, "Rock")


class TestMethods(unittest.TestCase):
	def test_str(self):
		e1=proj1.Song()
		e2=proj1.Movie()
		e3=proj1.Media()
		self.assertIn(e1.title, e1.__str__())
		self.assertIn(e1.author, e1.__str__())
		self.assertIn(e3.year, e3.__str__())
		self.assertIn(e1.gen, e1.__str__())
		self.assertIn(e2.rating, e2.__str__())

	def test_len(self):
		d1=proj1.Media()
		self.assertEqual(d1.__len__(), 0)

class TestInstVar(unittest.TestCase):
	def test_inst(self):
		r1=proj1.Song()
		r2=proj1.Movie()
		r3=proj1.Media()
		
		try:
			r1.rating
			r3.rating
			r3.album
			r2.gen
			self.fail()
		except:
			pass
		
class TestObjects(unittest.TestCase):
	def testSongObj(self):
		inst1=proj1.Song(trackName="Stand Still", artistName="Mary Mary", releaseDate="2007", collectionName="Heaven", trackTimeMillis=100000, primaryGenreName="Gospel")
		self.assertEqual(inst1.title, "Stand Still")
		self.assertEqual(inst1.author, "Mary Mary")
		self.assertEqual(inst1.year, "2007")
		self.assertEqual(inst1.album, "Heaven")
		self.assertEqual(inst1.t_len, 100000)
		self.assertEqual(inst1.gen, "Gospel")
		self.assertEqual(inst1.__len__(), 100)

	def testMovieObj(self):
		inst2=proj1.Movie(trackName="Prince of Egypt", artistName="Dreamworks", releaseDate="1998", trackTimeMillis=600000, contentAdvisoryRating="PG")
		self.assertEqual(inst2.title, "Prince of Egypt")
		self.assertEqual(inst2.author, "Dreamworks")
		self.assertEqual(inst2.year, "1998")
		self.assertEqual(inst2.rating, "PG")
		self.assertEqual(inst2.movie_len, 600000)

	def testMediaObj(self):
		inst3=proj1.Media(trackName="Prince of Egypt", artistName="Dreamworks", releaseDate="1998")
		self.assertEqual(inst3.title, "Prince of Egypt")
		self.assertEqual(inst3.author, "Dreamworks")
		self.assertEqual(inst3.year, "1998")

class TestQuery(unittest.TestCase):
	def testbaby(self):
		ex1=proj1.get_itudata("baby")
		ex2=proj1.get_itudata("#@%$$#")
		ex3=proj1.get_itudata("")
		ex4=proj1.get_itudata("Moana")
		self.assertRaises(Exception, ex1, "baby")
		self.assertRaises(Exception, ex2, "#@%$$#")
		self.assertRaises(Exception, ex3, "")
		self.assertRaises(Exception, ex4, "Moana")


unittest.main()
