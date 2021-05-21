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

def url__chain_regulate__save_seatmap(self, cinema_code: int, map_info: list) -> bool:

    chain_user, cinema_user = self.chain_cinema_user(cinema_code)

    self.ckt.save_seatmap_template(cinema_code, map_info)

    return True

def load_path(file_code, catalog):
        """通过file_code获取filepath"""
        try:
            file_path = hxsto.StoFile.load_from_filename(catalog, file_code).make_filepath('orignal')
        except Exception as e:
            file_path = None
        return file_path

def url__cinema_regulate__update_template(self, maptemplate) -> bool:
    将模板修改为使用状态
    uid = self.session.uid
    msg += '该文件的类型无法识别'
    msg += '上传的文件未查询到,请检查文件编码'
     y_coord, row_num = v.get("y_coord") or "", v.get("row_num") or ""
            x_coord, column_num = v.get("x_coord") or "", v.get("column_num") or ""
            status, group_code = v.get("status"), v.get("group_code")

    return True

def save_seatmap_template(self, cinema_code, map_data):
      
       保存影院手绘的座位图
        状态标记已使用
       :param cinema_code:
       :param map_data:
       :return:
       pass
def get_template_info(self, template_id, cinema_code):
        
        检查所选座位图模板是否存在
        :param template_id:
        :param cinema_code:
        :return:

        seatmap{
            "seatmapdata":"xxx"
            "seatnum": "xxx"
            "seatmapmodify": "",
            "mapsource": ""
        }
       
        seat_map, map_hash = "", ""

        return seat_map, map_hash
"""
