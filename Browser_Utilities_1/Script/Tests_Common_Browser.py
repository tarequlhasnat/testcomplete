def Open_and_Close_All_Browsers():
    #Open and Close All Installed Browsers 
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Begin All Installed Browsers Loop", "")
    #Iterates through the specified browsers.
    i = 0
    while i < Browsers.Count:
        Log.Message(i)
        Browsers.Item[i].Run()
        #The beginning of the Iterate Through Browsers group
        #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
        Log.AppendFolder(Aliases.browser.ProcessName, "", pmNormal, Project.Variables.LogAtrribInformation)
        #Delays the test execution for the specified time period.
        Delay(5000, "Generic 5 Second Delay")
        #Maximizes the specified Window object.
        Aliases.browser.BrowserWindow.Maximize()
        #Posts an information message to the test log.
        Log.Message("Browser Name = " + Aliases.browser.Name + " :Version = " + aqConvert.VarToStr(Aliases.browser.FileVersionInfo) + " :Process Type = " + Aliases.browser.ProcessType, "")
        #Delays the test execution for the specified time period.
        Delay(5000, "Generic 5 Second Delay")
        #Closes the specified Window object.
        Aliases.browser.BrowserWindow.Close()
        #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
        Log.PopLogFolder()
        #The end of the Iterate Through Browsers group
        i = i + 1
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
