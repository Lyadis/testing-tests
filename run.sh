#!/bin/bash

EXP_DIR='.'
EXP_PROJECT_LIST=$EXP_DIR/project_list
EXP_PROJECT_DONE=$EXP_DIR/project_list_done

function run_case {
	#go to exp home dir
	#cd $EXP_DIR
	echo $1
	git clone $1
	PROJECT_NAME=`echo $1 | cut -f 5 -d '/' | cut -f1 -d '.'`
	cd $PROJECT_NAME
	python ../transform-pom-cobertura.py pom.xml
	mvn cobertura:cobertura-integration-test
	if [ $? -neq 0 ]; then
		echo "$1 [Failed]" >> ../$EXP_PROJECT_DONE
	else
		echo "$1 [OK]" >> ../$EXP_PROJECT_DONE
	fi
	cd ..
}

for p in `cat $EXP_PROJECT_LIST`
do
	run_case $p
done
