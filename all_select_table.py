# 内部資材
import query

###########################################################
# t_post参照
###########################################################
t_post = query.select_t_post()
print("###########################################################")
print("# t_post参照")
print("###########################################################")
for p in t_post:
    print("post_date = {}, post_seconds = {}, post_milli_seconds = {}, post_name = {}, post_text = {}".\
            format(p.post_date, p.post_seconds, p.post_milli_seconds, p.post_name, p.post_text))
###########################################################
# t_post_bk参照
###########################################################
t_post_bk = query.select_t_post_bk()
print("###########################################################")
print("# t_post_bk参照")
print("###########################################################")
for p in t_post_bk:
    print("post_date = {}, post_seconds = {}, post_milli_seconds = {}, post_name = {}, post_text = {}".\
            format(p.post_date, p.post_seconds, p.post_milli_seconds, p.post_name, p.post_text))