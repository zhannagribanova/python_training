*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  firstname1  middlename1  lastname1
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Edit contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact_edit}=  Get From List  ${old_list}  ${index}
    ${new_contact}=  New Contact  firstname2  middlename2  lastname2
    Edit Contact  ${contact_edit}  ${new_contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact_edit}
    Append To List  ${old_list}  ${new_contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}