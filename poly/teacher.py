class Teacher:
    def teach(self):
        print("Teacher is teaching in the classroom.")
class YouTubeInstructor: 
    def teach(self):
        print("YouTube Instructor is teaching online.")
def start_teaching(obj):
    obj.teach()
t=Teacher()
y=YouTubeInstructor()
start_teaching()
start_teaching()