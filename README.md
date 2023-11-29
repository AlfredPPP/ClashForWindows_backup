# 简化版网页数据监控框架
这是一个为监控特定网站数据更新而设计的轻量级爬虫框架。本框架包含两大核心组件：数据采集模板和任务调配模板。

> 🕷️ **数据采集模板**：负责记录并返回网站数据的更新信息。在`~/task/`中创建任务路径和爬虫。

> ⏰ **任务调配模板**：任务安排在`schedule.json`文件中，配合**cron**表达式安排和管理爬虫任务。要新增一个爬虫任务，只需在`schedule.json`中增加一个包含任务路径与**cron**表达式的列表项即可。

> 🔍 *为什么不用**Scrapy**框架*：在编写本框架时，我还未接触过著名的**Scrapy**框架。本项目与**Scrapy**有少量相似之处，适用于轻量级解决方案的场景，或者基础的爬虫学习。它在功能和完善度上还无法与**Scrapy**相提并论，建议直接学习**Scrapy...**

欢迎有兴趣的朋友尝试使用~

# Customed Web Data Monitoring Framework
This is a lightweight web scraping framework designed for monitoring data updates on specific websites. This framework is comprised of two core components: a data collection template and a task scheduling template.

> 🕷️ **Data Collection Template:** Responsible for recording and returning updates on website data.Tasks and crawlers are set up in the `~/task/` directory.

> ⏰ **Task Scheduling Template:** Tasks are organized in the `schedule.json` file, utilizing cron expressions for arranging and managing crawler tasks. To add a new crawler task, simply include a new list item in `schedule.json` with the task path and cron expression.

> 🔍 *Why not **Scrapy** ?*: When I was developing this framework, I hadn't yet explored the well-known Scrapy framework. This project shares some similarities with Scrapy and is suitable for lightweight solutions or basic web scraping learning. However, in terms of features and robustness, it cannot compete with Scrapy at all. For those looking to delve deeper into web scraping, I recommend learning Scrapy directly...

Welcome to try and explore!
