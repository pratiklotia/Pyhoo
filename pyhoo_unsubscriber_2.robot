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
    type    id=login-username    pratiklotia@yahoo.in
    click    id=login-signin
    type    name=code    KDEY
    click    name=verify
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='IRCTC SBI Platinum Card'])[1]/following::span[4]
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='View this email in your browser'])[1]/following::a[2]
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Kelly Handerhan'])[1]/following::span[4]
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='CAclubindia Newsletter'])[1]/following::span[4]
    click    link=UNSUBSCRIBE
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Reminder - Activation'])[1]/following::div[2]
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Ryan Corey'])[1]/following::span[4]
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='TED Talks Daily'])[2]/following::span[4]
    click    link=unsubscribe from this list
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Spam'])[2]/following::span[1]
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='New folder'])[1]/following::div[28]
    click    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Date: Oldest on top'])[1]/following::span[1]
    