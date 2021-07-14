def ChequeScope():
    def DoLocal():
        test = "from Do local test"
    def DoNonLocal():
        nonlocal test
        test = "from Do non local test"
    def DoGlobal():
        global test
        test = "from Do global test"


    test = "defalt"
    DoLocal()
    print( "result is " +test )
    DoNonLocal()
    print( "result is " +test )
    DoGlobal()
    print( "result is: "+test )






ChequeScope()
