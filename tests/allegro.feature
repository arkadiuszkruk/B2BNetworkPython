Feature: Allegro pricing
    As a Allegro user
    User want to search for black iPhone 11
    So User can see amount of results, highest price and highest price with tax

    Scenario: Find highest price of Iphone 11 black
        Given User open the allegro site
        When User type Iphone 11 in search box and click search
        And User choose black color from the color list
        Then User can see number of results, highest price with and without tax