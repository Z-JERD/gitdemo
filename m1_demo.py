"""
提交新建m1文件测试

git branch -a

git branch

git branch iss20210430
git checkout iss20210430

等同于：git checkout -b iss20210430

git checkout master

git merge iss20210430

拉取远程仓库最新代码

git pull origin master

git push origin master

git commit 20210514144700

git commit 20210514150000 m1_demo

checkout mas20210517

def url__chain_regulate__seatmap_list(self, cinema_code: int, status: int = None) -> list:
       
     获取座位图模板
     :param  cinema_code
     :param status: 1： 模板未使用 2：模板已使用
     :return:
       
      assert status in [None, 1, 2], '类型值有误'

      chain_user, cinema_user = self.chain_cinema_user(cinema_code)

      response = self.ckt.get_seatmap_list(cinema_code, status)

       return response
"""
