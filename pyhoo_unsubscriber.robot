*** Settings ***
Suite Setup    Open Browser    https://www.katalon.com/    firefox
Suite Teardown    Close Browser
Resource    seleniumLibrary.robot

*** Variables ***
${undefined}    https://www.katalon.com/

*** Test Cases ***
Test Case
    open    https://mail.yahoo.com/
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Sign up'])[1]/following::span[1]
    click    id=login-username
    type    id=login-username    pratiklotia@yahoo.in
    click    id=login-signin
    type    name=code    KTQE
    click    name=verify
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Nikita'])[1]/following::span[4]
    doubleClick    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Nikita'])[1]/following::span[4]
    click    link=Click here
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Catch up on the most popular videos on Yahoo'])[1]/following::span[1]
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Club Oxygen'])[1]/following::span[4]
    doubleClick    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Club Oxygen'])[1]/following::span[4]
    click    link=To Stop It Click Here
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Catch up on the most popular videos on Yahoo'])[1]/following::span[2]
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Kalyan Matrimony'])[1]/following::span[4]
    doubleClick    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Kalyan Matrimony'])[1]/following::span[4]
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='View this email in your browser'])[1]/following::a[2]
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Catch up on the most popular videos on Yahoo'])[1]/following::span[2]
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='A.O. Smith'])[1]/following::span[4]
    doubleClick    xpath=(.//*[normalize-space(text()) and normalize-space(.)='A.O. Smith'])[1]/following::span[4]
    click    link=Unsubscribe me from this mailing list
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Catch up on the most popular videos on Yahoo'])[1]/following::span[2]
    