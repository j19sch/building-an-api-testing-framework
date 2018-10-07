*** Settings ***
Library	Collections
Library	RequestsLibrary


*** Variables ***
${user}=    bob


*** Test Cases ***
Delete book
    Create Session              ApiApp                  http://localhost:8000

    ${resp}=                    Get Request             ApiApp                        /books
    Should Be Equal As Strings  ${resp.status_code}     200
    Set Test Variable           ${book_id}              ${resp.json()[0]['id']}


    ${resp}=                    POST Request            ApiApp                        /token/${user}       data=None
    Set Test Variable           ${token}                ${resp.json()['token']}
    Should Be Equal As Strings  ${resp.status_code}     201

    ${headers}=                 Create Dictionary       user=${user}  token=${token}
    ${resp}=                    DELETE Request          ApiApp                          /books/${book_id}  headers=${headers}
    Should Be Equal As Strings  ${resp.status_code}     200

    ${resp}=                    GET Request             ApiApp                          /books/${book_id}
    Should Be Equal As Strings  ${resp.status_code}     404