# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：
# 1. 不得用于任何商业用途。
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。
# 3. 不得进行大规模爬取或对平台造成运营干扰。
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。
# 5. 不得用于任何非法或不当的用途。
#
# 详细许可条款请参阅项目根目录下的LICENSE文件。
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。


# 基础配置
PLATFORM = "xhs"
KEYWORDS = "南京"  # 关键词搜索配置，以英文逗号分隔
LOGIN_TYPE = "cookie"  # qrcode or phone or cookie
COOKIES = {
    "xhs":"abRequestId=ffe1a01b-6e54-56fb-872f-f1426b814c11; xsecappid=xhs-pc-web; a1=193d49d10ca2t7n42bqx7gd9exwyai4ktfxdz0t7j50000413772; webId=0e27f562e1e6826d14bc1dfded364005; gid=yjqf4jfyqS9Syjqf4jfy8i89S0J9WI4JDACWCWVkfjdCEf28v034Tu8884yqWWJ8q0y8YWDJ; web_session=040069b3b6996a34e8c86d3854354b0ae45b0c; acw_tc=0a00d7db17345220291936313e10d64203a5e3aa9ae2dba5c33f3e6b5aff2e; webBuild=4.47.1; unread={%22ub%22:%226742f793000000000800528e%22%2C%22ue%22:%22674d7b310000000002038888%22%2C%22uc%22:29}; websectiga=f47eda31ec99545da40c2f731f0630efd2b0959e1dd10d5fedac3dce0bd1e04d; sec_poison_id=0fdc6c6d-efda-4edf-82ba-64053e0460b7",
    "douyin":None, # 卸载了喵
    "kuaishou":None,
    "bilibili":"buvid3=6FCD6D0C-BB43-FE6A-8925-3C3A2CCB50A706977infoc; b_nut=1734353906; _uuid=45D832CD-81083-CEFB-5E96-3262F710710A8A08035infoc; enable_web_push=DISABLE; buvid4=3A41D3EF-D664-3595-202B-C7538649DDFF08055-024121612-GV3G1k2Ni8l%2BAor2%2Bw%2Bogg%3D%3D; buvid_fp=89c5f2c86420be6413449605756c6377; DedeUserID=544094474; DedeUserID__ckMd5=0da7f122077b2fdf; header_theme_version=CLOSE; rpdid=|(JJmY)YR~ml0J'u~JRJlJmmR; CURRENT_QUALITY=120; bmg_af_switch=1; LIVE_BUVID=AUTO3017344426405573; bsource=search_google; bmg_src_def_domain=i2.hdslb.com; home_feed_column=5; SESSDATA=6c8775ed%2C1750478423%2C5099d%2Ac2CjAnzNF075zhgx6oXv_Zf22lD9JNwhq4ELwIqLVE0nTImihNKA1bpuNH54Qjx2tut6YSVjBBU1JJNG9KNmFkMkVjbWdvY0w5MXBPbXJ4TF9lMGFMU01wMW53QVlWTUJRNWdOblJ4cGRacy1HY3F3UXEzMFpITnJOVjduZ3J6UHBJTFhvNmNlekJBIIEC; bili_jct=98651ba5904f0b6d92c3f6f883078971; sid=54m28u4x; hit-dyn-v2=1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzUxODU4ODAsImlhdCI6MTczNDkyNjYyMCwicGx0IjotMX0.Nv01VObmrmbOI9gn4SMwFaQynjgeJLQEoKhOICf-J68; bili_ticket_expires=1735185820; bp_t_offset_544094474=1013992906152738816; CURRENT_FNVAL=2000; b_lsid=B249258C_193F270BAE3; browser_resolution=1600-865; PVID=1",
    "weibo":"PC_TOKEN=4935c5d68d; XSRF-TOKEN=7fkzv8fsBOE5YgIzDfFwpDI8; SCF=Ah9YYBNM8oqy0hUg5i45Jde1XRmb2fWT5RAmB3zf-BRqK9r7Mwn9iVPQzVMcK1_KJbSJhb5LLbqLfHLJaAFAelM.; SUB=_2A25KbVoQDeRhGeRG7FsQ-CzNyDyIHXVpA9PYrDV8PUNbmtANLRn7kW9NTeVOYYqRi2mOM8iPjvoFWlePzEqjpJA8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWBZgioPso_yVLqOdL6Mkbr5NHD95QE1hM4eKnEeKe7Ws4Dqcj_i--ci-zEi-2pi--ciKLhiKn4i--ciK.Ni-24i--fiKnfi-8Fi--fiK.7iK.N; ALF=02_1737537344; WBPSESS=EIqcpKc6a_jnf_WnStAS-5QqX1x2gw2uExb5-Y0cXJpLvVo2XzwipcOAPfR48SNEl9HXxJGn90Dyun6p41OfTR70Re3LUNpme866OQxTKO7r3yi2RQtg658BRmlUn_uoZ1xWUNinneE3oQeb-5mLIA==",
    "tieba":None,
    "zhihu":"_xsrf=EfsLG16bVaeoZrZtdI95AmGuSYv16sWA; _zap=be4f3a79-537d-430d-af45-d12e3e579e4b; d_c0=AEAS3TE2tRmPTsD1IjK0OioOfbXWeieNWYg=|1734437640; gdxidpyhxdE=ROZ1R4t10xdmrjoUEWhqQqKLirp%2F30mpH%2FB3PaeWM86CE5AunX59v8lGYlR4YbL6b2r8YznC2e7RLgRojx2yoUQJ5D2qD4DutVJVoKbRgyArDahnMVVJuzaKWYPXsqoAcomVR%5CpOOxCPQqchEVM1lCQQL7nsiVTmexdSU871Di8PQCpm%3A1734438544713; captcha_ticket_v2=2|1:0|10:1734437712|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfNG1VYnFWLkFjX2VoX1VPNW9IWi5RU3R3SFhXcmhBODV5NTNZZ0pHX3NVcE15Wmp3SVBhaXlOQ2R1OXRLZHEyRFBZcWxiNkpwa0w2VlBpLjZVWkUzMi4uWjloVkZOd0tvdmUwZk1PQWdYUm9Kb3ZTb24yYTBxTUtndXJjSmhjaVpHazlVV1EyQkZVSCp1aFRaOF8zeUpicmVFRHhDLmtoRUVHRl8qbjNDaTliU0QqSWdQc3czVWxUSHVROVhsQzh5dFVwYWkzdVEwQU9DenZVQU15Ty41TU42c093KkRWU0FCQ0VjelJzbGtjbF9xUEc0NGF2dG0yX19WVWZPc0xrX2JKdks1aS5FMWprMHhTdnZUQTFIQmNTQnpUM1BQZlRGWkdHc0ZPSURhQ0tHNSpmVld5OHprSzhtUC5ZbDBXMUt5RmlwQldlSWlzLiouak9EYkNUQ2I2VDRzXzBVNm84cmpOcEpJekZIVzZZTExqWGlyTnpJalkxcjJJbmEuY09iWFpKKm1UdEExa0RyZipjU04uQ3UxS0Nnc0VrWkN6cWIyR25UaG9FamQwbDlZUFVlclEua2JTYkZxOTZJX3VfZkpKTXdqbkxtSHh3ejgqdl93ZS4uS3Z5T09RTWFBM3Y5WHJRMnplcUVVRktzMEhBMW8qR1k2dkZiV0MuMmx3TGVlNW9Hdk03N192X2lfMSJ9|0636e372bf5ffa599f99e174710433d60a72183c6949f944c270c1469c5e4d1e; z_c0=2|1:0|10:1734437766|4:z_c0|92:Mi4xQlY3Ykh3QUFBQUFBUUJMZE1UYTFHU1lBQUFCZ0FsVk5oYmxPYUFCTEZxS2Fzb0Vabk91WUlFOWd5UVRxOVJFYTR3|2e09f124f29220c9cd55514a856e1211376bc8f8836e74871b84b6d5fee6cdbf; __zse_ck=004_WBLDIUiBHDnZl9uAhQm7u1mAiTcuSs9fj2tkcIirfChqflpSlM5978BbgE9YSnoI46JMW=dvgfEHuwc/ntoQbKif2tdH5hmsV4/PplAK6B0JvY8dxoPi/rFjJPoPVlqs-V94GwldQDqpjSt8HkjlUUJe7LUG6/duApV0dw5DsVTacdrEM2FMRUBwVN+5iNHZkNZlsokcOM8wgN6ib3tZMYup6j/xXvXXu5OsuzjyWWoBkF5//LElpk+AA6KpwbkF7; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1734437644,1734533164; HMACCOUNT=B791579060F6A16A; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1734533197"
    }

# 具体值参见media_platform.xxx.field下的枚举值，暂时只支持小红书
SORT_TYPE = "popularity_descending"
# 具体值参见media_platform.xxx.field下的枚举值，暂时只支持抖音
PUBLISH_TIME_TYPE = 0
CRAWLER_TYPE = (
    "creator"  # 爬取类型，search(关键词搜索) | detail(帖子详情)| creator(创作者主页数据)
)
# 自定义User Agent（暂时仅对XHS有效）
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'

# 是否开启 IP 代理
ENABLE_IP_PROXY = False

# 未启用代理时的最大爬取间隔，单位秒（暂时仅对XHS有效）
CRAWLER_MAX_SLEEP_SEC = 2

# 代理IP池数量
IP_PROXY_POOL_COUNT = 2

# 代理IP提供商名称
IP_PROXY_PROVIDER_NAME = "kuaidaili"

# 设置为True不会打开浏览器（无头浏览器）
# 设置False会打开一个浏览器
# 小红书如果一直扫码登录不通过，打开浏览器手动过一下滑动验证码
# 抖音如果一直提示失败，打开浏览器看下是否扫码登录之后出现了手机号验证，如果出现了手动过一下再试。
HEADLESS = True

# 是否保存登录状态
SAVE_LOGIN_STATE = True

# 数据保存类型选项配置,支持三种类型：csv、db、json, 最好保存到DB，有排重的功能。
SAVE_DATA_OPTION = "json"  # csv or db or json

# 用户浏览器缓存的浏览器文件配置
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# 爬取开始页数 默认从第一页开始
START_PAGE = 1

# 爬取视频/帖子的数量控制
CRAWLER_MAX_NOTES_COUNT = 200

# 并发爬虫数量控制
MAX_CONCURRENCY_NUM = 1

# 是否开启爬图片模式, 默认不开启爬图片
ENABLE_GET_IMAGES = False

# 是否开启爬评论模式, 默认开启爬评论
ENABLE_GET_COMMENTS = True

# 爬取一级评论的数量控制(单视频/帖子)
CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES = 5


# 是否开启爬二级评论模式, 默认不开启爬二级评论
# 老版本项目使用了 db, 则需参考 schema/tables.sql line 287 增加表字段
ENABLE_GET_SUB_COMMENTS = False

# 已废弃⚠️⚠️⚠️指定小红书需要爬虫的笔记ID列表
# 已废弃⚠️⚠️⚠️ 指定笔记ID笔记列表会因为缺少xsec_token和xsec_source参数导致爬取失败
# XHS_SPECIFIED_ID_LIST = [
#     "66fad51c000000001b0224b8",
#     # ........................
# ]

# 指定小红书需要爬虫的笔记URL列表, 目前要携带xsec_token和xsec_source参数
XHS_SPECIFIED_NOTE_URL_LIST = [
    "https://www.xiaohongshu.com/explore/66fad51c000000001b0224b8?xsec_token=AB3rO-QopW5sgrJ41GwN01WCXh6yWPxjSoFI9D5JIMgKw=&xsec_source=pc_search"
    # ........................
]


# 指定抖音需要爬取的ID列表
DY_SPECIFIED_ID_LIST = [
    "7280854932641664319",
    "7202432992642387233",
    # ........................
]

# 指定快手平台需要爬取的ID列表
KS_SPECIFIED_ID_LIST = ["3xf8enb8dbj6uig", "3x6zz972bchmvqe"]

# 指定B站平台需要爬取的视频bvid列表
BILI_SPECIFIED_ID_LIST = [
    "BV1d54y1g7db",
    "BV1Sz4y1U77N",
    "BV14Q4y1n7jz",
    # ........................
]

# 指定微博平台需要爬取的帖子列表
WEIBO_SPECIFIED_ID_LIST = [
    "4982041758140155",
    # ........................
]

# 指定weibo创作者ID列表
WEIBO_CREATOR_ID_LIST = [
    "5533390220",
    # ........................
]

# 指定贴吧需要爬取的帖子列表
TIEBA_SPECIFIED_ID_LIST = []

# 指定贴吧名称列表，爬取该贴吧下的帖子
TIEBA_NAME_LIST = [
    # "盗墓笔记"
]

TIEBA_CREATOR_URL_LIST = [
    "https://tieba.baidu.com/home/main/?id=tb.1.7f139e2e.6CyEwxu3VJruH_-QqpCi6g&fr=frs",
    # ........................
]

# 指定小红书创作者ID列表
XHS_CREATOR_ID_LIST = [
    "63e36c9a000000002703502b",
    # ........................
]

# 指定Dy创作者ID列表(sec_id)
DY_CREATOR_ID_LIST = [
    "MS4wLjABAAAATJPY7LAlaa5X-c8uNdWkvz0jUGgpw4eeXIwu_8BhvqE",
    # ........................
]

# 指定bili创作者ID列表(sec_id)
BILI_CREATOR_ID_LIST = [
    "20813884",
    # ........................
]

# 指定快手创作者ID列表
KS_CREATOR_ID_LIST = [
    "3x4sm73aye7jq7i",
    # ........................
]


# 指定知乎创作者主页url列表
ZHIHU_CREATOR_URL_LIST = [
    "https://www.zhihu.com/people/yd1234567",
    # ........................
]

# 词云相关
# 是否开启生成评论词云图
ENABLE_GET_WORDCLOUD = False
# 自定义词语及其分组
# 添加规则：xx:yy 其中xx为自定义添加的词组，yy为将xx该词组分到的组名。
CUSTOM_WORDS = {
    "零几": "年份",  # 将“零几”识别为一个整体
    "高频词": "专业术语",  # 示例自定义词
}

# 停用(禁用)词文件路径
STOP_WORDS_FILE = "./docs/hit_stopwords.txt"

# 中文字体文件路径
FONT_PATH = "./docs/STZHONGS.TTF"
