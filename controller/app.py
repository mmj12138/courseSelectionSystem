from tornado import web,ioloop,httpserver
from model.models import UserModel
from model.models import InfoModel
from model.models import ClassModel
from model.models import AdInfoModel
from model.models import ClaStuModel
from model.fileModels import FileModel
from model.print import prin
# web.Application
id
class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("../web/login/login.html")
    def post(self, *args, **kwargs):
        username=self.get_argument("username")
        password=self.get_argument("password")
        user = UserModel()
        user_list=user.get_info_all()
        global  flag
        flag=0
        for i in range(0,len(user_list)):
            if(user_list[i].get("username")==username and user_list[i].get("password")==password):
                if(user_list[i].get("num")=='1'):
                    flag=1
                else:
                    flag=2
                global id
                id=username
        if flag==1:
            self.render("../web/login/welcome.html")
            # self.render("../web/test.html")
        elif flag==0:
            self.render("../web/login/error.html")
        else:
            self.render("../web/login/welcom2.html")

class Info1PageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        model=InfoModel()
        global id
        if id:
            stu_list = model.get_info_by_id(id=id)
            # print(stu_list[0])
            file = FileModel()
            file.stu_write(stu_list)
            self.render("../web/message/info1.html",stu_list=stu_list)
        else:
            self.render("../web/login/error.html")

class Info2PageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        model = InfoModel()
        global id
        stu_list = model.get_info_by_id(id=id)
        # print(stu_list[0])
        self.render("../web/message/info2.html", stu_list=stu_list)
    def post(self, *args, **kwargs):
        # stuid=self.get_argument("stuid")
        sname=self.get_argument("sname")
        sdept=self.get_argument("sdept")
        sex=self.get_argument("sex")
        message=self.get_argument("message")
        birth=self.get_argument("birth")
        # code=self.get_argument("code")
        model = InfoModel()
        Lid=model.update_info_by_id(stuid=id,sname=sname,sdept=sdept,sex=sex,message=message,birth=birth)
        if Lid:
            self.render("../web/message/success.html")
        # print(stuid,sname,sex,sdept,message,birth,code)
class XuanPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        model = ClaStuModel()
        global id
        c_list = model.get_by_id(id=id)
        # print(c_list[0])
        file = FileModel()
        file.cs_write(c_list)
        self.render("../web/message/xuanXiu.html", c_list=c_list)
    def post(self, *args, **kwargs):
        global id
        cid = self.get_argument("cid")
        model=ClaStuModel()
        lid=model.dele(stuid=id,cid=cid)
        # self.render("../web/message/success.html")
        self.render("../web/message/success.html")

class BiPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        model = ClassModel()
        global id
        c_list = model.get_info_all(id=id)
        # print(c_list[0])
        file = FileModel()
        file.class_write(c_list)
        with open(r'E:\Code\PyCharmCode\xuanKe\file\p.txt', 'a') as f:
            f.truncate(0)
        p = prin()
        p.run(c_list)
        self.render("../web/message/biXiu.html", c_list=c_list)
    def post(self, *args, **kwargs):
        global id
        cid = self.get_argument("cid")
        model=ClaStuModel()
        class_list = model.get_info_by_id(id=id)
        global flag2
        flag2=0
        for i in range(len(class_list)):
            if(class_list[i].get("cid")==cid):
                flag2=1
                self.render("../web/message/error.html")
        if flag2==0:
            s=model.insert(stuid=id,cid=cid)
            self.render("../web/message/success.html")
        # print(cid)

class testPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("../web/test.html")

class welPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("../web/login/welcome.html")
settings = {
    "static_path": '../static',
}
class adinfo1PageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        model = AdInfoModel()
        global id
        if id:
            ad_list = model.get_info_by_id(id=id)
            self.render("../web/message2/info1.html", ad_list=ad_list)
        else:
            self.render("../web/login/error.html")
class adinfo2PageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        model = AdInfoModel()
        global id
        if id:
            ad_list = model.get_info_by_id(id=id)
            self.render("../web/message2/info2.html", ad_list=ad_list)
    def post(self, *args, **kwargs):
            # stuid=self.get_argument("stuid")
            aname = self.get_argument("aname")
            sex = self.get_argument("sex")
            message = self.get_argument("message")
            birth = self.get_argument("birth")
            model = AdInfoModel()
            Lid = model.update_info_by_id(aid=id, aname=aname,sex=sex, message=message, birth=birth)
            if Lid:
                self.render("../web/message2/success.html")
class stu1PageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        model = InfoModel()
        stu_list=model.get_info_all()
        self.render("../web/message2/stuInfo1.html",stu_list=stu_list)
    def post(self, *args, **kwargs):
        stuid=self.get_argument("stuid")
        print(stuid)
        model1 = ClaStuModel()
        cs = model1.dele_by_stu(stuid)
        moddel2 = InfoModel()
        stu = moddel2.del_info_by_id(stuid)
        self.render("../web/message2/success.html")
class cla1PageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        model= ClassModel()
        c_list = model.get_info()
        self.render("../web/message2/clasInfo.html",c_list=c_list)
    def post(self, *args, **kwargs):
        cid = self.get_argument("cid")
        print(cid)
        model1 = ClaStuModel()
        cs = model1.dele_by_c(cid)
        moddel2 = ClassModel()
        c = moddel2.del_info_by_id(cid)
        self.render("../web/message2/success.html")
class upstuPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("../web/message2/upstu.html")
    def post(self, *args, **kwargs):
        stuid=self.get_argument("stuid")
        sname=self.get_argument("sname")
        sex=self.get_argument("sex")
        sdept=self.get_argument("sdept")
        sstate=self.get_argument("sstate")
        birth=self.get_argument("birth")
        code=self.get_argument("code")
        message=self.get_argument("message")
        print(stuid,sname,sex,sdept,sstate,birth,code,message)
        if(stuid=='' or sname=='' or sex=='' or sdept=='' or sstate=='' or birth=='' or code=='' or message ==''):
            self.render("../web/message2/error.html")
        else:
            model = InfoModel()
            model.insert(stuid=stuid,sname=sname,sex=sex,sdept=sdept,sstate=sstate,birth=birth,code=code,message=message)
            self.render("../web/message2/success.html")
class upclaPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("../web/message2/upcla.html")
    def post(self, *args, **kwargs):
        cid=self.get_argument("cid")
        cname=self.get_argument("cname")
        cstart=self.get_argument("cstart")
        ctaime=self.get_argument("ctaime")
        cdept=self.get_argument("cdept")
        ccode=self.get_argument("ccode")
        print(cid,cname,cstart,ctaime,cdept,ccode)
        if(cid=='' or cname=='' or cstart=='' or ctaime=='' or cdept=='' or cdept==''):
            self.render("../web/message2/error.html")
        else:
            model = ClassModel()
            model.insert(cid=cid,cname=cname,cstart=cstart,ctaime=ctaime,cdept=cdept,ccode=ccode)
            # model.insert(stuid=stuid,sname=sname,sex=sex,sdept=sdept,sstate=sstate,birth=birth,code=code,message=message)
            self.render("../web/message2/success.html")

application = web.Application([
            (r"/", MainPageHandler),
            (r"/info1", Info1PageHandler),
            (r"/info2", Info2PageHandler),
            (r"/xuan", XuanPageHandler),
            (r"/bi", BiPageHandler),
            (r"/test", testPageHandler),
            (r"/wel", welPageHandler),
            (r"/adinfo1", adinfo1PageHandler),
            (r"/adinfo2", adinfo2PageHandler),
(r"/stu", stu1PageHandler),
(r"/cla", cla1PageHandler),
(r"/upstu", upstuPageHandler),
(r"/upcla", upclaPageHandler),
        ],**settings)
if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()
