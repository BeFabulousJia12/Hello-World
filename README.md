# Hello-World
1. Click [GithubSimpleGuide](https://guides.github.com/activities/hello-world), and read this guide to create/manage your repository.
2. Download [GitHubClient](https://desktop.github.com), GitHub Client is a way to contribute to projects on GitHub.

## How to use GitHub Client
1. You can clone your repository which has been created on GitHub.
2. Manuiplate your code/script/project on your local machine, and then sync it to GitHub.

	#####2.1 *Update Files*
    For instant, you've updated README file,then:   
    On GitHub GUI Client,   
    1). You will receive the notification in Change icon.  
    2). Click the change icon, you will see what changed in README.
    3). If you agree with this change, you need write some info in 'summary' field.  
    4). Click 'Commit to Master'button.  
		Or, use the git command:   
        `git commit -am "update sth"`  
    5). Click 'Sync'button to Sync your commit change to GitHub Web.  
    Or, use the git command:  
    `git push` 

    #####2.2 *Add New Files*
       e.g. added the new folder (ImageProcessingPython) including your code under your local repository.It has the same steps with 2.1, the change notification will tell you what happened, the difference is the git command, you need one extra command before commit:  
       ***`git add .`***  
       `git commit -am "add new files"`

    #####2.3 *Git Diff Command*  
       `git diff HEAD`
 
    #####2.4 *Logs Commands*  
    `git log`  
     `git log -p`
   
 
*Other git commands are on-going...*

## Something about ImageProcessingPython Folder

1. I'm trying to process the picutre which only has one character. The character may be in different color, but currently, the background of this pic must be white, and without any hot pixel. Such as, A.jpg, M.jpg under this folder.

2. 'imagetest.py'can recognize which character on the current pic.For example,in script, A.jpg is the input pic:  

	`imgcode = Image.open("A.jpg")` 

	...

	Then,after comparison with Alib.jpg and Mlib.jpg pictures, the test result should tell you the correct character:

	`print("this is A character!!")`

    You can also change the "A.jpg" as "M.jpg" in script, to make the another test! Then the result must be:

    `print("this is M character!!")`


####To Do List:
1. In fact, I should create 26 characters library.
2. Get picture's name dynamically instead of updating the pic name manually in imagetest.py.Or,each input picture must be converted into the same file name before being recognized!!!

####Mix
1. ***Markdown Editor:*** [MarkdownPad](http://www.markdownpad.com/) which is used to edit a better README file. ;)
 




       
       