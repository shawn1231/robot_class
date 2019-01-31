#!/usr/bin/env python

import random
import rospy
import time
import csv
import os
import datetime

def talker():

	# header for csv file
	myData = ["var1,var2"]

	fileNameBase = "./scripts/log_files/" + datetime.datetime.now().strftime("%b_%d_%H_%M")
	fileNameSuffix = ".csv"
	num = 1

	fileName = fileNameBase + fileNameSuffix

	while os.path.isfile(fileName):
		fileName = fileNameBase + "_" + str(num) + fileNameSuffix
		num = num + 1

	myFile = open(fileName, 'a')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerow(myData)

	while not rospy.is_shutdown():

		myData = [1,2]

		print "write to file"

		myFile = open(fileName, 'a')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerow(myData)

		print "write complete, waiting"

		time.sleep(2)


if __name__ == '__main__':

	time.sleep(1)

	try:
		talker()

	except rospy.ROSInterruptException:

		pass
