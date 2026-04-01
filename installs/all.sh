#!/bin/sh


for d in "ux" "sh"; do
	cd $d
	echo installing for $d
	brew bundle install
	cd ..
done
