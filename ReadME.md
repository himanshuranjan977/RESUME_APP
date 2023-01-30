# Tables in resume app

User 
    - id
    -username

PersonalDetails
    -id
    -name
    -phone
    -email
    -address
    -linkedin_url
    -ForeignKey('user.id')

projects
    -id
    -name
    -desc
    -start_date
    -end_date
    -ForeignKey('user.id')

experience
    -id
    -company_name
    -role
    -role_desc
    -start_date
    -end_date
    -ForeignKey('user.id')

education
    -id
    -school_name
    -degeree_name
    -start_date
    -end_date
    -ForeignKey('user.id')

certificates
    -id
    -title
    -start_date
    -end_date
    -ForeignKey('user.id')
Skills
    -id
    -title
    -confidence_score
    -ForeignKey('user.id')
