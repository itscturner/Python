#!/usr/bin/env python

# Splash Screen Python Project

import os
import time

def splash_screen(seconds):
  print("\n")
  print(" *********************************")
  print(" *                               *")
  print(" *         SPLASH SCREEN         *")
  print(" *             v1.0              *")
  print(" *                               *")
  print(" *********************************")
  time.sleep(seconds)
  os.system('clear')

# Main Program Starts Here
splash_screen(5)
