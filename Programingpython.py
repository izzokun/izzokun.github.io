from flask import Flask, render_template

app = Flask(__name__)

####data lecture:
lecture_1 = {
    "name":"Bat dau voi python",
    "image":"http://www.ilearnitalian.net/wp-content/uploads/2013/09/lesson1-300x150.jpg",
    "content":"Bai hoc ve bat dau voi python"
}
lecture_2 = {
    "name":"Ung dung python",
    "image":"http://3.bp.blogspot.com/-LlO7sniK8Tw/UO1CQdTsACI/AAAAAAAAAdc/QF9C-PaWkWw/s1600/Startup-Lessons-2.png",
    "content":"Bai hoc ve ung dung cua python"
}
lecture_3 = {
    "name":"Ket thuc bai hoc",
    "image":"http://www.theamericanmonk.com/media/images/lessons/lesson3.gif",
    "content":"Bai hoc ket thuc"
}
########################
class Lecture:
    def __init__(self,name,image,content):
        self.name = name
        self.image = image
        self.content = content
List_Lecture = [lecture_1,lecture_2,lecture_3]
Object1 = Lecture(lecture_1["name"],lecture_1["image"],lecture_1["content"])
Object2 = Lecture(lecture_2["name"],lecture_2["image"],lecture_2["content"])
Object3 = Lecture(lecture_3["name"],lecture_3["image"],lecture_3["content"])
List_Object_Lecture = [Object1,Object2,Object3]

linkbai1 = "https://drive.google.com/uc?export=download&id=0B2zzJcGKr5B3S1FRY2xkcWNybVE"
print(Object1.name)
@app.route('/')
def home_page():
    return render_template("main.html")

@app.route('/Lecture1')
def lecture1():
    return render_template("lecture.html", list1 = Object1, link = linkbai1)

@app.route('/Lecture2')
def lecture2():
    return render_template("lecture.html", list1 = Object2)

@app.route('/Lecture3')
def lecture3():
    return render_template("lecture.html", list1 = Object3)


if __name__ == '__main__':
    app.run()
