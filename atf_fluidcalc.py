# ******************************************************************************
# Name:  Transmission Fluid %
# Author:  Vadim Korotkikh
# Email:   va.korotki@gmail.com
# Date:    February 2017
# Version:
#
# Description:
#
# ******************************************************************************
# Libraries

import sys
import math
import numpy as np


def main(flush_num):

	atf_capacity_qt		= 11.5
	new_fluid_qt		= 2

	atf_breakdown(new_fluid_qt, atf_capacity_qt,flush_num)


def atf_breakdown(new_fluid_qt, atf_capacity_qt, flush_num):

	old_fluid	= atf_capacity_qt - new_fluid_qt
	new_fluid	= 0 + new_fluid_qt

	quart_cnt	= [i for i in range(1,int(flush_num))]

	for i in quart_cnt:
		print("Flush count #:", i)
		new_fluid, old_fluid = calculate_content(new_fluid_qt, new_fluid, atf_capacity_qt)


def calculate_content(add_size, new_size, total_size):
	"""Calculate content after draining x quarts of fluid where x is = add_size"""

	old_fluid_size	= total_size - new_size
	old_fluid_size	= np.float64(old_fluid_size - add_size * (old_fluid_size / total_size))
	new_fluid_size	= np.float64(new_size - add_size * (new_size / total_size) + add_size)
	print("New ATF fluid in quarts:", new_fluid_size)
	print("Old ATF fluid in quarts:", old_fluid_size)

	old_new_prsnt	= np.float64(np.divide(new_fluid_size, total_size))
	print("New ATF fluid percentage:", old_new_prsnt)
	return new_fluid_size, old_fluid_size

def atf_fluid_percent():
	pass



if __name__ == "__main__":
	flush_count	= 11
	try:
		main(sys.argv[1])
	except IndexError:
		main(flush_count)
