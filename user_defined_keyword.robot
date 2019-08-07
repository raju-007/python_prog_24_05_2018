*** settings ***
Library  SeleniumLibrary

*** variables ***

${Browser}  Firefox

${URL}  https://en-gb.facebook.com/login

*** test cases ***

TC_002 Browser to insert the element in login page
    Open Browser  ${URL}  ${Browser}
    maximize browser window
    Enter username password email


*** keywords ***
Enter username password email
    input text  name:email  rajsh.2012@gmail.com
    input text  xpath://input[@name='pass']  ajtaj
    clear element text  name:email
    input text  name:email  rajsh.2012@gmail.com
    Click Button  //button[.//text() = 'Log In']


