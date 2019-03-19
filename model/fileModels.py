import time
class FileModel():
    def class_write(self,word):
        with open(r'E:\Code\PyCharmCode\xuanKe\file\class.txt', 'a') as f:
            # f.truncate(0)
            f.write("-------------"+time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime())+"-------------")
            f.write("\n")
            f.write("所有课程\n")
            for i in range(0,len(word)):
                f.write("第"+str(i+1)+"条    ")
                f.write("课程号："+word[i].get("cid")+" ")
                f.write("课程名：" + word[i].get("cname") + " ")
                f.write("开始学期：" + word[i].get("cstart") + " ")
                f.write("学时：" + word[i].get("ctaime") + " ")
                f.write("学分：" + word[i].get("ccode") + " ")
                f.write("\n")
        print("所有课程写入成功！")
    def cs_write(self,word):
        with open(r'E:\Code\PyCharmCode\xuanKe\file\cs.txt', 'a') as f:
            # f.truncate(0)
            f.write("-------------" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "-------------")
            f.write("\n")
            f.write("已选课程\n")
            for i in range(0,len(word)):
                f.write("第"+str(i+1)+"条    ")
                f.write("课程号："+word[i].get("cid")+" ")
                f.write("课程名：" + word[i].get("cname") + " ")
                f.write("开始学期：" + word[i].get("cstart") + " ")
                f.write("学时：" + word[i].get("ctaime") + " ")
                f.write("学分：" + word[i].get("ccode") + " ")
                f.write("\n")
        print("已选课程写入成功！")
    def stu_write(self,word):
        with open(r'E:\Code\PyCharmCode\xuanKe\file\stu.txt', 'a') as f:
            # f.truncate(0)
            f.write("-------------" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "-------------")
            f.write("\n")
            f.write("学生信息\n")
            f.write("学号："+word[0].get("stuid")+"\n")
            f.write("姓名：" +word[0].get("sname")+"\n")
            f.write("性别：" + word[0].get("sex")+"\n")
            f.write("所在系：" + word[0].get("sdept")+"\n")
            f.write("生日：" + word[0].get("birth")+"\n")
            f.write("学分：" + str(word[0].get("code")) + "\n")
        print("学生信息写入成功！")