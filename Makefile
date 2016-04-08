# This makefile just contains an installation script
INSTALL_DIR="/usr/local/bin/"

default:	all
all:

install:
	install --mode=0755 -p isitopen.py $(INSTALL_DIR)/isITopen

