from model.db import DbConnection

class UserModel(DbConnection):
    def get_info_all(self):
        try:
            self.connect()
            sql='select * from user'
            self.cursor.execute(sql)
            self.close()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
class InfoModel(DbConnection):
    def get_info_all(self):
        try:
            self.connect()
            sql='select * from stu'
            self.cursor.execute(sql)
            self.close()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
    def get_info_by_id(self,id):
        try:
            self.connect()
            sql='select * from stu WHERE stuid=%s'
            self.cursor.execute(sql,id)
            self.close()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
    def del_info_by_id(self,id):
        try:
            self.connect()
            sql='delete from stu WHERE stuid=%s'
            self.cursor.execute(sql,id)
            self.close()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def update_info_by_id(self,**kwargs):
        try:
            self.connect()
            sql='update stu set s' \
                'name=%s,sdept=%s,sex=%s,birth=%s,message=%s where stuid=%s'
            self.cursor.execute(sql,(kwargs['sname'],kwargs['sdept'],kwargs['sex'],kwargs['birth'],kwargs['message'],kwargs['stuid']))
            self.close()
            return self.cursor.fetchall
        except Exception as e:
            print(e)
    def insert(self,**kwargs):
        try:
            self.connect()
            caozuo="选修"
            sql='insert into sc.stu VALUES (%s,%s,%s,%s,%s,%s,%s,%s,NULL )'
            self.cursor.execute(sql,(kwargs['stuid'],kwargs['sname'],kwargs['sex'],kwargs['sdept'],kwargs['sstate'],kwargs['birth'],kwargs['code'],kwargs['message']))
            self.close()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
class AdInfoModel(DbConnection):
    def get_info_by_id(self,id):
        try:
            self.connect()
            sql='select * from admin WHERE aid=%s'
            self.cursor.execute(sql,id)
            self.close()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def update_info_by_id(self,**kwargs):
        try:
            self.connect()
            sql='update admin set aname=%s,' \
                'sex=%s,birth=%s,message=%s where aid=%s'
            self.cursor.execute(sql,(kwargs['aname'],kwargs['sex'],kwargs['birth'],kwargs['message'],kwargs['aid']))
            self.close()
            return self.cursor.fetchall
        except Exception as e:
            print(e)
class ClassModel(DbConnection):
    def get_info_all(self,id):
        try:
            self.connect()
            sql1='select * from stu WHERE  stuid=%s'
            self.cursor.execute(sql1,(id))
            s = self.cursor.fetchall()
            state=s[0].get('sstate')
            dept=s[0].get('sdept')
            sql='select * from sc.class WHERE cstart>%s AND cdept=%s'
            self.cursor.execute(sql,(state,dept))
            self.close()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
    def del_info_by_id(self,id):
        try:
            self.connect()
            sql='delete from sc.class WHERE cid=%s'
            self.cursor.execute(sql,id)
            self.close()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
    def get_info(self):
        try:
            self.connect()
            sql='select * from sc.class'
            self.cursor.execute(sql)
            self.close()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
    def insert(self,**kwargs):
        try:
            self.connect()
            caozuo="选修"
            sql='insert into sc.class VALUES (%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql,(kwargs['cid'],kwargs['cname'],kwargs['cstart'],kwargs['ctaime'],kwargs['cdept'],kwargs['ccode'],caozuo))
            self.close()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
class ClaStuModel(DbConnection):
    def get_info_by_id(self,id):
        try:
            self.connect()
            sql='select * from classstu WHERE stuid=%s'
            self.cursor.execute(sql,id)
            self.close()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
    def get_by_id(self,id):
        try:
            self.connect()
            sql='select * from classstu WHERE stuid=%s'
            self.cursor.execute(sql,id)
            result1=self.cursor.fetchall()
            list=[]
            for i in range(0,len(result1)):
                sql2='select * from class WHERE cid=%s'
                self.cursor.execute(sql2,result1[i].get("cid"))
                result2=self.cursor.fetchall()
                list.append(result2[0])
            self.close()
            return list

        except Exception as e:
            print(e)
    def insert(self,**kwargs):
        try:
            self.connect()
            sql='insert into classstu VALUES (%s,%s)'
            self.cursor.execute(sql,(kwargs['stuid'],kwargs['cid']))
            self.close()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
    def dele(self,**kwargs):
        try:
            self.connect()
            sql='delete from classstu where stuid=%s AND cid=%s'
            self.cursor.execute(sql,(kwargs['stuid'],kwargs['cid']))
            self.close()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
    def dele_by_stu(self,id):
        try:
            self.connect()
            sql='delete from classstu where stuid=%s'
            self.cursor.execute(sql,(id))
            self.close()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
    def dele_by_c(self,id):
        try:
            self.connect()
            sql='delete from classstu where cid=%s'
            self.cursor.execute(sql,(id))
            self.close()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)

if __name__ == '__main__':
    m = InfoModel()
    # m.insert(stuid=150403,sname="璐璐",sex="女",sdept="计算机",sstate="3",birth="1996-03-14",code="40",message="璐璐的备注")
