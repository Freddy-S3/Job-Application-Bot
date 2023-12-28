browser = ["Chrome"]

#Login Credentials
credentialFile = open("D:\Programming\Credentials\LinkedinLogin.txt", "r")
email = credentialFile.readline() #potential newline
password = credentialFile.readline()
credentialFile.close()

#Job Filters
location = ["North America"]
keywords = ["cloud","cloud architect", "AWS", "Python", "Java"]
experienceLevels = []
datePosted = []
jobType = []
remote = []
salary = []
sort = []

#Job Application info
firstName = "Freddy"
lastName = "Shaikh"
email = "shaikhfh1@gmail.com"
Phone = "437-267-3291"

#
linkedinProfileURL = "https://www.linkedin.com/in/freddy-shaikh/"

