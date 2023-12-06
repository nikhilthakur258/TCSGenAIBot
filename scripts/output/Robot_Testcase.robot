*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${url}            https://www.example.com
${browser}        Chrome
${username}       testuser123
${password}       $Pass123
${file1}          500kb-sheet.xlsx
${file2}          1mb-sheet.xlsx

*** Test Cases ***
Signed-in users get larger capacity
    Open Browser To Example.com
    User Clicks On Upload Files
    Page Reloads
    User Clicks On Spreadsheet Formats
    Buttons XLS And XLSX Show
    User Clicks On XLSX
    User Selects File ${file1}
    Upload Completes
    Table Uploaded Files Contains Cell ${file1}
    User Clicks On XLSX
    User Selects File ${file2}
    Upload Fails
    Table Uploaded Files Does Not Contain Cell ${file2}
    User Clicks On Login
    User Enters Username ${username}
    User Enters Password ${password}
    User Clicks On Sign In
    Page Reloads
    Table Uploaded Files Contains Cell ${file1}
    Table Uploaded Files Does Not Contain Cell ${file2}
    User Clicks On Spreadsheet Formats
    Buttons XLS And XLSX Show
    User Clicks On XLSX
    User Selects File ${file2}
    Upload Completes
    Table Uploaded Files Contains Cell ${file2}
    Table Uploaded Files Contains Cell ${file1}
    User Clicks On Sign Out
    Page Reloads
    Table Uploaded Files Does Not Contain Cell ${file2}
    Table Uploaded Files Contains Cell ${file1}

*** Keywords ***
Open Browser To Example.com
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Set Browser Implicit Wait    10s
    ${title}    Get Title
    Should Be Equal    ${title}    Example Domain
    Log    Browser title is: ${title}

User Clicks On Upload Files
    Click Element    xpath://a[@href='/upload']
    Wait Until Element Is Visible    xpath://h1[text()='Upload Files']

Page Reloads
    Reload Page

User Clicks On Spreadsheet Formats
    Click Element    xpath://a[@href='/formats']
    Wait Until Element Is Visible    xpath://h1[text()='Spreadsheet Formats']

Buttons XLS And XLSX Show
    Wait Until Element Is Visible    xpath://button[text()='XLS']
    Wait Until Element Is Visible    xpath://button[text()='XLSX']

User Clicks On XLSX
    Click Element    xpath://button[text()='XLSX']

User Selects File
    [Arguments]    ${file}
    Choose File    xpath://input[@type='file']    ${file}

Upload Completes
    Wait Until Element Is Visible    xpath://div[text()='Upload completed.']

Table Uploaded Files Contains Cell
    [Arguments]    ${file}
    Wait Until Element Is Visible    xpath://td[text()='${file}']

Upload Fails
    Wait Until Element Is Visible    xpath://div[text()='Upload failed.']

Table Uploaded Files Does Not Contain Cell
    [Arguments]    ${file}
    Wait Until Element Is Not Visible    xpath://td[text()='${file}']

User Clicks On Login
    Click Element    xpath://a[@href='/login']
    Wait Until Element Is Visible    xpath://h1[text()='Login']

User Enters Username
    [Arguments]    ${username}
    Input Text    xpath://input[@name='username']    ${username}

User Enters Password
    [Arguments]    ${password}
    Input Text    xpath://input[@name='password']    ${password}

User Clicks On Sign In
    Click Element    xpath://button[text()='Sign in']
    Wait Until Element Is Visible    xpath://h1[text()='Example Domain']

User Clicks On Sign Out
    Click Element    xpath://a[@href='/logout']
    Wait Until Element Is Visible    xpath://h1[text()='Example Domain']