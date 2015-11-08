import sys
import unittest
import main


class Tester(unittest.TestCase):

	def test_condition1(self):
		self.assertEqual(main.condition("y"), True, "The condition test failed on 'y'")
	def test_condition2(self):
		self.assertEqual(main.condition("n"), False, "The condition test failed on 'n'")
	def test_condition3(self):
		self.assertEqual(main.condition("ynfj49 d"), False, "The condition test failed on 'ynfj49 d'")

	def test_old1(self):
		self.assertEqual(main.old(23), 23, "The old test failed on 23")
	def test_old2(self):
		self.assertEqual(main.old(2), 2, "The old test failed on 2")
	def test_old3(self):
		self.assertEqual(main.old(10), 10, "The old test failed on 10")


	def test_box1(self):
		self.assertEqual(main.box("y"), True, "The box test failed on 'y'")
	def test_box2(self):
		self.assertEqual(main.box("n"), False, "The box test failed on 'n'")
	def test_box3(self):
		self.assertEqual(main.box("ynfj49 d"), False, "The box test failed on 'ynfj49 d'")

	def test_frame1(self):
		self.assertEqual(main.frame(1), 1, "The frame test failed on 1")
	def test_frame2(self):
		self.assertEqual(main.frame(2), 2, "The frame test failed on 2")
	def test_frame3(self):
		self.assertEqual(main.frame(3), 3, "The frame test failed on 3")
	def test_frame4(self):
		self.assertEqual(main.frame(4), 4, "The frame test failed on 4")

	def test_insurance1(self):
		self.assertEqual(main.insurance("y"), True, "The insurance test failed on 'y'")
	def test_insurance2(self):
		self.assertEqual(main.insurance("n"), False, "The insurance test failed on 'n'")
	def test_insurance3(self):
		self.assertEqual(main.insurance("ynfj49 d"), False, "The insurance test failed on 'ynfj49 d'")

	def test_birds1(self):
		self.assertEqual(main.birds("y"), True, "The birds test failed on 'y'")
	def test_birds2(self):
		self.assertEqual(main.birds("n"), False, "The birds test failed on 'n'")
	def test_birds3(self):
		self.assertEqual(main.birds("ynfj49 d"), False, "The birds test failed on 'ynfj49 d'")

	def test_buttons(self):
		self.assertEqual(main.buttons(2), 2, "The buttons test failed on 2")

	def test_waterDamage1(self):
		self.assertEqual(main.waterDamage("y"), True, "The waterDamage test failed on 'y'")
	def test_waterDamage2(self):
		self.assertEqual(main.waterDamage("n"), False, "The waterDamage test failed on 'n'")
	def test_waterDamage3(self):
		self.assertEqual(main.waterDamage("ynfj49 d"), False, "The waterDamage test failed on 'ynfj49 d'")

	def test_screenDamage1(self):
		self.assertEqual(main.frame(1), 1, "The screenDamage test failed on 1")
	def test_screenDamage2(self):
		self.assertEqual(main.frame(2), 2, "The screenDamage test failed on 2")
	def test_screenDamage3(self):
		self.assertEqual(main.frame(3), 3, "The screenDamage test failed on 3")

	def test_power1(self):
		self.assertEqual(main.power("y"), True, "The power test failed on 'y'")
	def test_power2(self):
		self.assertEqual(main.power("n"), False, "The power test failed on 'n'")
	def test_power3(self):
		self.assertEqual(main.power("ynfj49 d"), False, "The power test failed on 'ynfj49 d'")

	def test_findCarrier(self):
		carrierList = main.build_carrierDic().keys()
		self.assertEqual(main.findCarrier(carrierList, 2), "Verizon", "The findCarrier test failed on 'Verizon'")

	def test_findPhone(self):
		phoneList = main.build_phoneDic().keys()
		self.assertEqual(main.findPhone(phoneList, 9), "iPhone 5c", "The findPhone test failed on 'Verizon'")


if __name__ == '__main__':
	#supress stdout
	f = open('/dev/null', 'w')
	sys.stdout = f

	#run the tests
	unittest.main()