from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    spiders_names = process.spider_loader.list()
    for s in spiders_names:
        process.crawl(s)
    process.start()


if __name__ == '__main__':
    main()
