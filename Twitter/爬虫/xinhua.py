import asyncio
import time
# 异步请求模块
import aiohttp

start_time = time.time()

# 创建特殊函数
# 在特殊函数内部不可以出现不支持异步模块相关的代码
# 异步请求aiohttp(支持异步)模块
# 细节1：在每一个with前加上async关键字
# 细节2：在get方法前和response.text()前加上await关键字进行手动挂起操作(多任务)
async def request(url):
    # 创建aiohttp链接
    async with aiohttp.ClientSession() as cs:
        # aiohttp发送get请求
        async with await cs.get(url=url) as response:
            # 返回网页文本字符串响应数据
            return await response.text()


# 任务回调函数
def task_callback(task):
    # 执行result函数，返回任务对象执行完成后的结果
    page_text = task.result()
    print(page_text + ',请求到的数据！！！')


# flask服务地址，一个线程多任务时默认最多500协程(推荐)
urls = [
    'http://www.news.cn/politics/'

]

# 任务列表
tasks = []

# 返回协程对象
for url in urls:
    c = request(url=url)

    # 封装任务对象
    task = asyncio.ensure_future(c)
    # 把每一个任务对象存放进任务列表
    tasks.append(task)
    # 添加任务回调函数
    task.add_done_callback(task_callback)

# 创建事件循环对象
loop = asyncio.get_event_loop()
# 如果想要将多个任务对象注册到事件循环中，必须将多个任务对象封装到一个列表中，然后将列表注册并将任务挂起
loop.run_until_complete(asyncio.wait(tasks))

print("共执行时间：", time.time() - start_time)


