import json
import time
import logging
import importlib
from logging.handlers import RotatingFileHandler
from apscheduler.schedulers.background import BackgroundScheduler
from dingtalkchatbot.chatbot import DingtalkChatbot


def set_log_config():
    # 创建一个滚动文件处理器，并设置格式化器
    handler = RotatingFileHandler("./data_monitor_log/log", maxBytes=1024 * 1024, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)

    # 获取根日志器并添加处理器，设置级别
    root_logger = logging.getLogger('')
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(handler)


def execute_task(category, task):
    # 配置钉钉机器人
    # 测试url
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=c16a87777ac1df00fef2bcdfab61c2b6591ddedd32b6ad51cf7353adaae0b6b9'
    #正式url
    # webhook = 'https://oapi.dingtalk.com/robot/send?access_token=00d29582f86b51c11aa1e946762ab3815a3104ea659fa80ebbb5f5be85bb93f5'
    ding_bot = DingtalkChatbot(webhook)

    # 执行爬虫任务
    try:
        module_path = f"tasks.{category}.{task}.{task}"

        logging.info(f"开始执行：tasks.{category}.{task}.{task}")

        task_module = importlib.import_module(module_path)
        result = task_module.run()
        if result:
            message = result
            ding_bot.send_text(msg='自动发送——\n' + message, at_mobiles=['18888642253'])
            logging.info("已钉钉通知对应人员")
    except Exception as e:
        print(f"Error running task {category}.{task}: {e}")
        logging.error(f"Error running task {category}.{task}: {e}")
        ding_bot.send_text(msg=f'自动发送——任务失败\n路径模块：{category} \n路径明细：{task} \n报错内容：{str(e)}', at_mobiles=['18888642253'])


if __name__ == "__main__":
    set_log_config()
    logging.info('process start!')
    print('process start!')

    # 加载调度配置
    with open("schedule.json", "r", encoding='utf-8') as file:
        schedule_config = json.load(file)

    # 定义定时任务
    scheduler = BackgroundScheduler()
    for category, tasks in schedule_config.items():
        for task, config in tasks.items():
            time_config = config["time"]
            # execute_task('FINANCE', 'NEW-Q2-金融-银保监会-银行业总资产总负债')
            scheduler.add_job(execute_task, trigger='cron', year=time_config['year'], month=time_config['month'],
                              day=time_config['day'], hour=time_config['hour'], minute=time_config['minute'],
                              second=time_config['second'], args=[category, task])

    # 开始调度
    logging.info("Scheduler has started!")
    try:
        scheduler.start()
        while True:
            time.sleep(100)  # 主线程将每100秒休眠一次，以减少CPU使用率, 不影响子线程已排期任务的运行
    except (KeyboardInterrupt, SystemExit):
        logging.info("process shutdown!")
        scheduler.shutdown()
