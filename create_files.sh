project=module5
directory=ex04
# name=Point
sources="parameters.py"
# includes="Animal.hpp Dog.hpp Cat.hpp"
mkdir $project
cd $project
mkdir $directory
cd $directory
# mkdir sources
# cd sources
touch $sources
chmod +x $sources
echo "#!usr/bin/env python3" > $sources
echo "" >> $sources
# cd ..
# mkdir includes
# cd includes
# touch $includes
# cd ..
# cp /home/goksu/Codam/CPP/Makefile .
# sed -i "s/NAME\s*=\s*Fixed/NAME = $name/" /home/goksu/Codam/CPP/$project/$directory/Makefile
# sed -i "s/SRC\s*=\s*main.cpp/SRC = $sources/" /home/goksu/Codam/CPP/$project/$directory/Makefile
# sed -i "s/HEADERS\s*=\s*Fixed.hpp/HEADERS = $includes/" /home/goksu/Codam/CPP/$project/$directory/Makefile