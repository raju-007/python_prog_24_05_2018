*** settings ***
Library  OperatingSystem


*** variables ***

${message}  hello google
*** test cases ***

my first test
    log to console  ${message}

my second test
    should be equal  ${message}  hello google

my thirst test
    #Create Directory    /home/raju/stuff
    #Create File  /home/raju/stiff/empty.txt  hi himanshi
    #Copy File    ${CURDIR}/file.txt    ${TEMPDIR}/stuff
    log  abc

my fourth test
    #Run Program  /home/raju/PycharmProjects/robot_automation/robot_auto/first_tc1.robot
    log  abc

