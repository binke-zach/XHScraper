# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：  
# 1. 不得用于任何商业用途。  
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。  
# 3. 不得进行大规模爬取或对平台造成运营干扰。  
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。   
# 5. 不得用于任何非法或不当的用途。
#   
# 详细许可条款请参阅项目根目录下的LICENSE文件。  
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。  


import asyncio
import sys

import cmd_arg
import config
import db
from base.base_crawler import AbstractCrawler
from media_platform.bilibili import BilibiliCrawler
from media_platform.douyin import DouYinCrawler
from media_platform.kuaishou import KuaishouCrawler
from media_platform.tieba import TieBaCrawler
from media_platform.weibo import WeiboCrawler
from media_platform.xhs import XiaoHongShuCrawler
from media_platform.zhihu import ZhihuCrawler


class CrawlerFactory:
    CRAWLERS = {
        "xhs": XiaoHongShuCrawler,
        "dy": DouYinCrawler,
        "ks": KuaishouCrawler,
        "bili": BilibiliCrawler,
        "wb": WeiboCrawler,
        "tieba": TieBaCrawler,
        "zhihu": ZhihuCrawler
    }

    @staticmethod
    def create_crawler(platform: str) -> AbstractCrawler:
        crawler_class = CrawlerFactory.CRAWLERS.get(platform)
        if not crawler_class:
            raise ValueError("Invalid Media Platform Currently only supported xhs or dy or ks or bili ...")
        return crawler_class()


async def main(platform:str,type="search",keywords=None,id=None):
    # parse cmd
    await cmd_arg.parse_cmd()

    # init db
    if config.SAVE_DATA_OPTION == "db":
        await db.init_db()

    if platform not in ["xhs","dy","ks","bili","wb","tieba","zhihu"]:
         platform = config.PLATFORM
    crawler = CrawlerFactory.create_crawler(platform=platform)
    await crawler.start(type,keywords,id)

    if config.SAVE_DATA_OPTION == "db":
        await db.close()

def run_main_task(platform:str,type: str,keywords:str, id: list):
    try:
        result = asyncio.get_event_loop().run_until_complete(main(platform=platform,type=type, keywords= keywords,id=id))
        return result
    except KeyboardInterrupt:
        sys.exit()
    
if __name__ == '__main__':
    run_main_task("xhs","search",None,None)
    # search "keyword1" None 
    # creator None ["xxx","xxx"]

    # paltform para: xhs dy ks bili wb tieba zhihu
    # type para: search creator
    # keywords para: str
    # id para: list() ps. zhihu-主页url 贴吧-url