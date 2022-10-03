Feature: Register as a expert

    Scenario: An expert joins the eond
        Given Exp opens eond website
        When Exp fills username and password
        And Exp chooses engagement type
        And Exp uploads cv and fills skills
        And Exp fills experience
        And Exp chooses engagemend models
        And Exp fills personal data
        Then Exp sees the page profile created
