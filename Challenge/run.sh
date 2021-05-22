#! /bin/zsh

# python3 hc.py < ./test/in5.txt

for i in {0..18} ; do
	echo case${i}
	python3 hc.py < ./test/in${i}.txt > ./test/out${i}.txt
	diff ./test/out${i}.txt ./test/answer${i}.txt
	echo "---------------------"
done
