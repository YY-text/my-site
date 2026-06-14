#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python实操题页面生成脚本 - 详细版
   为每个小节生成：多段示例代码 + 练习区 + 在线运行链接
"""

import os
import sys
import json
sys.path.insert(0, os.path.dirname(__file__))
from generate_all_sections import COURSES


# ============ 内容生成器 ============

def make_sidebar_html(course_info, section_id):
    """生成侧边栏HTML"""
    out = ["<ul class=\"sidebar-nav\">"]
    out.append("            <li class=\"sidebar-back\"><a href=\"section-" + section_id + ".html\">← 返回小节</a></li>")
    for ch in course_info['chapters']:
        out.append("            <li class=\"sidebar-chapter\"><a href=\"section-" + section_id + ".html\">第" + str(ch["num"]) + "章 " + ch["title"] + "</a>")
        out.append("                <ul class=\"sidebar-sections\">")
        for sec in ch['sections']:
            out.append("                    <li><a href=\"section-" + sec["id"] + ".html\">" + sec["id"].replace("-", ".") + " " + sec["title"] + "</a></li>")
        out.append("                </ul></li>")
    out.append("        </ul>")
    return "\n".join(out)


# 为每个小节生成丰富内容的字典
def generate_detailed_content(section):
    """根据小节生成详细的实操内容"""
    sid = section['id']
    title = section['title']
    kp = section.get('knowledge', [])
    kp_text = "、".join(kp) if kp else title

    examples = []
    practice_title = title + "练习"
    practice_tasks = []
    solution = ""

    # ========== 第1章: Python入门认知 ==========
    if sid == '1-1':  # 语言简介
        examples = [
            ("示例1：最基础的Hello程序",
             '# Hello World 是学习任何编程语言的第一个程序\n# print() 函数用于在屏幕上输出内容\n# 括号中的字符串用双引号 "" 或 单引号 \'\' 包裹\n\nprint("Hello, World!")\nprint("你好，Python!")',
             "Hello, World!\n你好，Python!"),
            ("示例2：多行输出与装饰",
             '# 可以用多个print语句打印多行内容\n# 使用 "=" * 数字 可以重复打印字符，画分割线\n\nprint("=" * 50)\nprint("                欢迎来到Python世界")\nprint("=" * 50)\nprint("Python是一个简单易学、功能强大的语言")\nprint("让我们一起开始编程之旅！")\nprint("=" * 50)',
             "==================================================\n                欢迎来到Python世界\n==================================================\nPython是一个简单易学、功能强大的语言\n让我们一起开始编程之旅！\n=================================================="),
            ("示例3：特殊字符的使用",
             '# 特殊转义字符：\n#   \\n → 换行\n#   \\t → 制表符(Tab，用于对齐)\n#   \\\\ → 反斜杠本身\n\nprint("第一行\\n第二行\\n第三行")\nprint()\nprint("姓名\\t年龄\\t城市")\nprint("小明\\t18\\t北京")\nprint("小红\\t20\\t上海")\nprint("小张\\t19\\t广州")',
             "第一行\n第二行\n第三行\n\n姓名\t年龄\t城市\n小明\t18\t北京\n小红\t20\t上海\n小张\t19\t广州"),
        ]
        practice_tasks = [
            "打印你的名字",
            "打印三行鼓励自己的话",
            "用 = 和 * 画一个漂亮的装饰边框，中间写标题文字",
        ]
        solution = '# 练习参考答案\nprint("我是小明")\nprint("加油，我一定可以学会Python！")\nprint("坚持就是胜利！")\nprint("每天进步一点点！")\n\nprint("*" * 40)\nprint("         我的学习笔记")\nprint("*" * 40)'

    elif sid == '1-2':  # 环境安装
        examples = [
            ("示例1：查看Python版本",
             '# import 语句用于导入Python的内置模块\n# sys 模块提供了很多与系统交互的功能\n\nimport sys\n\nprint("=" * 40)\nprint("         Python版本信息")\nprint("=" * 40)\nprint(f"主版本号: {sys.version_info.major}")\nprint(f"次版本号: {sys.version_info.minor}")\nprint(f"微版本号: {sys.version_info.micro}")\nprint(f"发行级别: {sys.version_info.releaselevel}")\nprint(f"完整版本字符串: {sys.version}")\nprint("=" * 40)',
             "========================================\n         Python版本信息\n========================================\n主版本号: 3\n次版本号: 11\n微版本号: 0\n发行级别: final\n完整版本字符串: 3.11.0 ...\n========================================"),
            ("示例2：查看系统信息",
             'import sys\nimport platform\n\nprint("=" * 40)\nprint("          系统信息")\nprint("=" * 40)\nprint(f"操作系统: {platform.system()}")\nprint(f"详细版本: {platform.platform()}")\nprint(f"架构: {platform.architecture()[0]}")\nprint(f"处理器: {platform.processor()}")\nprint(f"Python路径: {sys.executable}")\nprint(f"默认编码: {sys.getdefaultencoding()}")\nprint("=" * 40)',
             "========================================\n          系统信息\n========================================\n操作系统: Windows\n详细版本: Windows-10-10.0.19041\n架构: 64bit\n处理器: Intel64...\nPython路径: C:\\Python311\\python.exe\n默认编码: utf-8\n========================================"),
        ]
        practice_tasks = [
            "导入sys模块，打印Python版本字符串",
            "打印30个等号作为分割线，中间写'环境检查'",
            "打印一句'我的Python环境已准备好！'",
        ]
        solution = '# 练习参考答案\nimport sys\n\nprint("=" * 30)\nprint("         环境检查")\nprint("=" * 30)\nprint(sys.version)\nprint("\\n我的Python环境已准备好！")'

    elif sid == '1-3':  # 运行方式
        examples = [
            ("示例1：交互式输入",
             '# input() 函数让用户在命令行输入内容\n# input返回的永远是字符串类型\n\nname = input("请输入你的名字: ")\nprint(f"你好, {name}! 欢迎来到Python世界!")\nprint(f"{name}, 今天想学习什么呢？")',
             "请输入你的名字: 小明\n你好, 小明! 欢迎来到Python世界!\n小明, 今天想学习什么呢？"),
            ("示例2：多次输入收集信息",
             '# 可以多次调用input收集不同信息\nprint("=" * 30)\nprint("   个人信息录入")\nprint("=" * 30)\n\nname = input("请输入你的姓名: ")\nage = input("请输入你的年龄: ")\ncity = input("请输入所在城市: ")\n\nprint("\\n" + "=" * 30)\nprint(f"姓名: {name}")\nprint(f"年龄: {age}岁")\nprint(f"城市: {city}")\nprint(f"{name}, 欢迎你！")',
             "==============================\n   个人信息录入\n==============================\n请输入你的姓名: 小明\n请输入你的年龄: 18\n请输入所在城市: 北京\n\n==============================\n姓名: 小明\n年龄: 18岁\n城市: 北京\n小明, 欢迎你！"),
            ("示例3：简单加法计算器",
             '# input得到的是字符串，需用int()或float()转成数字\n\nprint("=" * 30)\nprint("   简易加法计算器")\nprint("=" * 30)\n\n# 获取用户输入\nnum1 = input("请输入第一个数字: ")\nnum2 = input("请输入第二个数字: ")\n\n# 转换为整数\na = int(num1)\nb = int(num2)\n\n# 计算并输出\nresult = a + b\nprint(f"{a} + {b} = {result}")\nprint("计算完成！")',
             "==============================\n   简易加法计算器\n==============================\n请输入第一个数字: 15\n请输入第二个数字: 25\n15 + 25 = 40\n计算完成！"),
        ]
        practice_tasks = [
            "写一个程序：询问用户名字，然后打印'你好，[名字]'",
            "写一个程序：让用户输入两个数字，打印它们的和",
            "写一个程序：打印漂亮的边框 + 标题，然后询问用户今天学习的内容",
        ]
        solution = '# 练习参考答案\n# 程序1\nname = input("请输入你的名字: ")\nprint("你好, " + name)\n\n# 程序2\nx = int(input("数字1: "))\ny = int(input("数字2: "))\nprint(x + y)\n\n# 程序3\nprint("="*30)\nprint("   今日学习记录")\nprint("="*30)\ntopic = input("今天学习了什么？: ")\nprint(f"已记录：{topic}")'

    elif sid == '1-4':  # 编辑器使用
        examples = [
            ("示例1：创建正式的Python脚本",
             '# ========================================\n# 文件名: my_first_program.py\n# 作者: 你的名字\n# 版本: 1.0\n# 描述: 我的第一个正式Python程序\n# ========================================\n\nprint("*" * 40)\nprint("    我的第一个Python程序")\nprint("*" * 40)\nprint()\nprint("  你好，Python世界!")\nprint("  我正在学习编程")\nprint("  感觉很不错!")\nprint()\nprint("*" * 40)',
             "****************************************\n    我的第一个Python程序\n****************************************\n\n  你好，Python世界!\n  我正在学习编程\n  感觉很不错!\n\n****************************************"),
            ("示例2：学会使用注释",
             '# 单行注释用井号开头\n# 注释是写给人看的，Python会忽略它\n\n"""\n这是多行注释\n通常写在文件开头，说明程序的整体功能\n作者: 小明\n日期: 2024年\n"""\n\nprint("注释很重要")  # 行尾也可以写注释\nprint("好的代码自己会说话")  # 好代码+好注释=最好',
             "注释很重要\n好的代码自己会说话"),
        ]
        practice_tasks = [
            "创建一个Python文件，开头写三行说明的注释，然后打印3行内容",
            "打印一个简单的ASCII方框（用*围起来）",
            "打印一个小三角形",
        ]
        solution = '# 练习参考答案\nprint("*" * 20)\nprint("*" + " " * 18 + "*")\nprint("*  我的第一个程序  *")\nprint("*" + " " * 18 + "*")\nprint("*" * 20)\n\n# 三角形\nfor i in range(1, 6):\n    print("*" * i)'

    # ========== 第2章: 基础输出与注释 ==========
    elif sid == '2-1':  # print输出
        examples = [
            ("示例1：多种输出方式",
             '# print可以接收多个参数，用逗号分隔\n# sep 参数指定分隔符\n# end 参数指定结尾字符\n\nprint("Hello")\nprint("Python", "是", "有趣的")  # 自动加空格\nprint(1, 2, 3, sep="-")  # 自定义分隔符\nprint("第一", end="")\nprint("第二")  # 不换行，与上一行相连',
             "Hello\nPython 是 有趣的\n1-2-3\n第一第二"),
            ("示例2：打印表格",
             '# 用制表符\\t可以打印简单的表格\n\nprint("-" * 30)\nprint("姓名\\t科目\\t成绩")\nprint("-" * 30)\nprint("小明\\t数学\\t95")\nprint("小红\\t语文\\t88")\nprint("小张\\t英语\\t92")\nprint("-" * 30)',
             "------------------------------\n姓名\t科目\t成绩\n------------------------------\n小明\t数学\t95\n小红\t语文\t88\n小张\t英语\t92\n------------------------------"),
        ]
        practice_tasks = [
            "打印5行不同的内容",
            "用制表符打印一个包含3个人信息的小表格",
            "用sep和end参数打印'1-2-3-4-5-6'",
        ]
        solution = '# 练习参考答案\nfor i in range(1, 7):\n    print(i, end="-" if i < 6 else "\\n")'

    elif sid == '2-2':  # 格式输出
        examples = [
            ("示例1：f-string格式化",
             '# f-string是Python 3.6+推荐的格式化方式\n# 在字符串前加f，然后用{变量名}插入变量值\n\nname = "小明"\nage = 18\nscore = 95.5\n\nprint(f"姓名: {name}")\nprint(f"年龄: {age}岁")\nprint(f"成绩: {score}分")\nprint(f"{name}今年{age}岁，考试成绩{score}分")',
             "姓名: 小明\n年龄: 18岁\n成绩: 95.5分\n小明今年18岁，考试成绩95.5分"),
            ("示例2：数字格式化",
             '# :.2f 表示保留2位小数\n# :.0f 表示不保留小数\n# :,  表示千分位分隔符\n\nprice = 19.99\nquantity = 3\ntotal = price * quantity\n\nprint(f"单价: {price:.2f}元")\nprint(f"数量: {quantity}")\nprint(f"总价: {total:.2f}元")\nprint(f"精确总价: {total}")',
             "单价: 19.99元\n数量: 3\n总价: 59.97元\n精确总价: 59.97000000000001"),
            ("示例3：对齐输出",
             '# :>n 右对齐，:>n 或 <n 左对齐\n# 常用于打印漂亮的表格\n\nitems = [("苹果", 5, 3.5), ("香蕉", 10, 2.8), ("橙子", 6, 4.2)]\n\nprint(f"{"商品":<6} {"数量":>4} {"单价":>6} {"小计":>6}")\nprint("-" * 30)\nfor name, qty, price in items:\n    subtotal = qty * price\n    print(f"{name:<6} {qty:>4} {price:>6.2f} {subtotal:>6.2f}")',
             "商品     数量   单价   小计\n------------------------------\n苹果        5   3.50  17.50\n香蕉       10   2.80  28.00\n橙子        6   4.20  25.20"),
        ]
        practice_tasks = [
            "用f-string打印你的个人信息（姓名、年龄、城市）",
            "格式化打印3个物品的购物清单，保留2位小数",
            "用对齐格式打印一个简单的3行表格",
        ]
        solution = '# 练习参考答案\nname = "小明"\nage = 18\ncity = "北京"\nprint(f"我是{name}，今年{age}岁，来自{city}")\n\nprint("商品  数量  单价")\nprint(f"苹果    5   3.50")\nprint(f"香蕉   10   2.80")\nprint(f"橙子    6   4.20")'

    elif sid == '2-3':  # 单行注释
        examples = [
            ("示例1：好的注释",
             '# 计算两个数之和\n# 作者: 小明\n# 日期: 2024\n\na = 10  # 第一个加数\nb = 20  # 第二个加数\nresult = a + b  # 求和\nprint(f"{a} + {b} = {result}")  # 打印结果',
             "10 + 20 = 30"),
            ("示例2：什么时候写注释",
             '# 写注释的黄金法则：解释为什么，而不是做了什么\n\n# 价格计算（因为VIP用户有特殊折扣）\nprice = 100\ndiscount = 0.2  # 20%的VIP折扣\nfinal_price = price * (1 - discount)\n\nprint(f"原价: {price}元")\nprint(f"折扣后: {final_price:.0f}元")',
             "原价: 100元\n折扣后: 80元"),
        ]
        practice_tasks = [
            "写一个计算圆面积的程序，每一行都加适当注释",
            "写一个计算BMI的程序（体重除以身高平方），加上详细注释",
        ]
        solution = '# 练习参考答案\n# 圆面积 = π * r^2\nr = 5  # 半径\npi = 3.14159  # 圆周率\narea = pi * r * r  # 计算面积\nprint(f"半径为{r}的圆面积是: {area:.2f}")'

    elif sid == '2-4':  # 多行注释
        examples = [
            ("示例1：文件头注释",
             '"""\nprogram_name.py - 程序的一句话说明\n\n这个程序演示了Python的基本功能。\n作者: 小明\n日期: 2024年\n版本: 1.0\n\n使用方法:\n    python program_name.py\n\n示例输出:\n    程序运行结果\n"""\n\nprint("这是带注释的程序")\nprint("注释帮助我们理解代码")',
             "这是带注释的程序\n注释帮助我们理解代码"),
            ("示例2：函数注释",
             '"""\n计算工具程序\n\n本程序包含多种常见计算功能：\n1. 加法\n2. 减法\n3. 乘法\n4. 除法\n"""\n\na, b = 15, 8\n\nprint(f"{a} + {b} = {a + b}")\nprint(f"{a} - {b} = {a - b}")\nprint(f"{a} x {b} = {a * b}")\nprint(f"{a} / {b} = {a / b:.2f}")',
             "15 + 8 = 23\n15 - 8 = 7\n15 x 8 = 120\n15 / 8 = 1.88"),
        ]
        practice_tasks = [
            "写一个文件，开头有完整的多行注释说明，然后打印你的名字和日期",
            "写一个文件，顶部加完整的程序说明，然后打印一个简单的统计表",
        ]
        solution = '"""\n练习程序 - 多行注释练习\n作者: 小明\n功能: 演示多行注释的用法\n"""\n\nprint("=" * 30)\nprint("   数据统计")\nprint("=" * 30)\nprint("Python: 90分")\nprint("数学: 85分")\nprint("英语: 88分")'

    # ========== 第3章: 变量与命名规则 ==========
    elif sid == '3-1':  # 变量定义
        examples = [
            ("示例1：基本变量类型",
             '# Python是动态类型语言：变量不需要声明类型\n# 主要类型：字符串(str)、整数(int)、浮点数(float)、布尔(bool)\n\nname = "小明"  # 字符串: 用引号包裹\nage = 18  # 整数: 没有小数点\nheight = 1.75  # 浮点数: 有小数点\nis_student = True  # 布尔值: True或False（首字母大写）\n\nprint(f"姓名: {name}, 类型: {type(name)}")\nprint(f"年龄: {age}, 类型: {type(age)}")\nprint(f"身高: {height}, 类型: {type(height)}")\nprint(f"学生: {is_student}, 类型: {type(is_student)}")',
             "姓名: 小明, 类型: <class 'str'>\n年龄: 18, 类型: <class 'int'>\n身高: 1.75, 类型: <class 'float'>\n学生: True, 类型: <class 'bool'>"),
            ("示例2：重新赋值",
             '# 变量的值可以随时改变\n# 甚至可以改变类型（虽然不推荐）\n\nx = 10\nprint(f"x的初始值: {x}")\n\nx = 20\nprint(f"x的新值: {x}")\n\nx = "现在变成字符串了"\nprint(f"x的值: {x}")',
             "x的初始值: 10\nx的新值: 20\nx的值: 现在变成字符串了"),
        ]
        practice_tasks = [
            "定义3个变量：你的名字、年龄、城市，然后用一行打印所有信息",
            "定义价格、数量，计算并打印总价",
            "定义一个计数器，初始值为0，然后给它加5，打印结果",
        ]
        solution = '# 练习参考答案\nname = "小明"\nage = 18\ncity = "北京"\nprint(f"姓名: {name}, 年龄: {age}, 城市: {city}")\n\nprice = 19.99\nqty = 3\nprint(f"总价: {price * qty:.2f}元")\n\ncount = 0\ncount = count + 5\nprint(f"计数: {count}")'

    elif sid == '3-2':  # 命名规则
        examples = [
            ("示例1：好的和坏的命名",
             '# 好的命名: 有描述性，使用下划线或驼峰\n# 坏的命名: 只有a,b,c或拼音，难以理解\n\n# 好的命名\nstudent_name = "小明"\ncourse_score = 95\nmax_temperature = 38.5\n\n# 可读性对比\n# 这段代码在说什么？\na = 95\nb = 88\nc = a + b\n\n# 这段呢？\nchinese_score = 95\nmath_score = 88\ntotal_score = chinese_score + math_score\nprint(f"总分为: {total_score}")',
             "总分为: 183"),
            ("示例2：变量命名规范",
             '# 命名规则:\n# 1. 必须以字母或下划线开头\n# 2. 只能包含字母、数字和下划线\n# 3. 不能使用Python关键字（如if, for, while等）\n# 4. 区分大小写: Name 和 name 是两个不同变量\n# 5. 推荐: 使用小写+下划线 (snake_case)，见名知意\n\n# 推荐写法\nuser_age = 18\nuser_name = "小明"\nuser_city = "北京"\n\nprint(f"用户信息: {user_name}, {user_age}岁, {user_city}")',
             "用户信息: 小明, 18岁, 北京"),
        ]
        practice_tasks = [
            "用规范的命名定义5个描述你的变量，然后打印它们",
            "定义一个产品信息的变量集合（名称、价格、库存、描述），并打印",
        ]
        solution = '# 练习参考答案\nproduct_name = "《Python入门教程》"\nproduct_price = 59.90\nproduct_stock = 100\nproduct_desc = "适合零基础学习Python的图书"\n\nprint("=" * 30)\nprint(f"商品: {product_name}")\nprint(f"价格: {product_price}元")\nprint(f"库存: {product_stock}本")\nprint(f"描述: {product_desc}")\nprint("=" * 30)'

    elif sid == '3-3':  # 变量赋值
        examples = [
            ("示例1：多种赋值方式",
             '# 1. 普通赋值\nx = 10\nprint(f"普通赋值: x = {x}")\n\n# 2. 链式赋值（多个变量设为同一个值）\na = b = c = 5\nprint(f"链式赋值: a={a}, b={b}, c={c}")\n\n# 3. 多元赋值（一次给多个变量赋值）\nname, age, city = "小明", 18, "北京"\nprint(f"多元赋值: {name}, {age}, {city}")\n\n# 4. 增量赋值\ncount = 0\ncount += 1  # 相当于 count = count + 1\ncount += 1\ncount += 1\nprint(f"增量赋值: count = {count}")',
             "普通赋值: x = 10\n链式赋值: a=5, b=5, c=5\n多元赋值: 小明, 18, 北京\n增量赋值: count = 3"),
            ("示例2：增量赋值运算符",
             '# 增量赋值有: +=, -=, *=, /=, %=, **=, //=\n\nscore = 10\nprint(f"初始分: {score}")\n\nscore += 5  # 加5\nprint(f"+5: {score}")\n\nscore -= 3  # 减3\nprint(f"-3: {score}")\n\nscore *= 2  # 乘2\nprint(f"x2: {score}")\n\nscore /= 3  # 除3\nprint(f"/3: {score}")',
             "初始分: 10\n+5: 15\n-3: 12\nx2: 24\n/3: 8.0"),
        ]
        practice_tasks = [
            "用增量赋值模拟一个分数变化（初始0，加10，加5，减3，乘2，打印每步）",
            "用链式赋值创建3个相同的变量，打印它们",
            "用多元赋值把你的姓名、年龄、城市分别赋给3个变量然后打印",
        ]
        solution = '# 练习参考答案\nscore = 0\nprint(f"初始: {score}")\nscore += 10\nprint(f"+10: {score}")\nscore += 5\nprint(f"+5: {score}")\nscore -= 3\nprint(f"-3: {score}")\nscore *= 2\nprint(f"x2: {score}")'

    elif sid == '3-4':  # 变量交换
        examples = [
            ("示例1：Python式的变量交换",
             '# 其他语言交换需要临时变量\n# 但Python可以一行搞定！\n\na, b = 10, 20\nprint(f"交换前: a = {a}, b = {b}")\n\n# Python式交换: 右边先求值，再打包成元组，再解包给左边\na, b = b, a\nprint(f"交换后: a = {a}, b = {b}")',
             "交换前: a = 10, b = 20\n交换后: a = 20, b = 10"),
            ("示例2：更多变量的交换",
             '# 不仅可以交换两个，还可以同时交换多个\n\nx, y, z = 1, 2, 3\nprint(f"交换前: x={x}, y={y}, z={z}")\n\n# 轮换: x得到y的值，y得到z的值，z得到x的值\nx, y, z = y, z, x\nprint(f"交换后: x={x}, y={y}, z={z}")',
             "交换前: x=1, y=2, z=3\n交换后: x=2, y=3, z=1"),
        ]
        practice_tasks = [
            "定义两个变量，用Python式一行交换它们的值，打印前后对比",
            "用多元赋值交换3个变量的值（旋转式），打印前后对比",
        ]
        solution = '# 练习参考答案\na, b = 5, 8\nprint(f"交换前: a={a}, b={b}")\na, b = b, a\nprint(f"交换后: a={a}, b={b}")\n\n# 3变量旋转\nx, y, z = 10, 20, 30\nprint(f"旋转前: x={x}, y={y}, z={z}")\nx, y, z = y, z, x\nprint(f"旋转后: x={x}, y={y}, z={z}")'

    # ========== 第4-11章: 继续扩充类似内容 ==========
    elif sid == '4-1':  # 整数类型
        examples = [
            ("示例1：整数运算",
             '# 整数是不带小数点的数字\n# 支持所有数学运算\n\na, b = 15, 4\n\nprint(f"{a} + {b} = {a + b}")\nprint(f"{a} - {b} = {a - b}")\nprint(f"{a} * {b} = {a * b}")\nprint(f"{a} / {b} = {a / b} (结果是浮点数)")\nprint(f"{a} // {b} = {a // b} (整除，只取整数部分)")\nprint(f"{a} % {b} = {a % b} (取余，得到余数)")\nprint(f"{a} ** {b} = {a ** b} (a的b次方)")',
             "15 + 4 = 19\n15 - 4 = 11\n15 * 4 = 60\n15 / 4 = 3.75 (结果是浮点数)\n15 // 4 = 3 (整除，只取整数部分)\n15 % 4 = 3 (取余，得到余数)\n15 ** 4 = 50625 (a的b次方)"),
            ("示例2：数字大了也不怕",
             '# Python的整数可以非常大（不像其他语言有溢出问题）\n\nbig = 2 ** 100\nprint(f"2的100次方 = {big}")\nprint(f"这个数的长度: {len(str(big))} 位")\n\n# 可以用下划线让大数字更易读\npopulation = 1_400_000_000  # 14亿\nprint(f"人口数: {population}人")',
             "2的100次方 = 1267650600228229401496703205376\n这个数的长度: 31 位\n人口数: 1400000000人"),
        ]
        practice_tasks = [
            "定义两个整数a=25, b=8，打印它们的加减乘除结果",
            "计算2的20次方，并打印位数",
            "打印100除以7的商和余数",
        ]
        solution = '# 练习参考答案\na, b = 25, 8\nprint(f"{a}+{b}={a+b}, {a}-{b}={a-b}")\nprint(f"{a}*{b}={a*b}, {a}/{b}={a/b}")\nprint(f"{a}//{b}={a//b} (商), {a}%{b}={a%b} (余数)")\n\n# 2的20次方\nx = 2**20\nprint(f"2^20 = {x}, 共{len(str(x))}位")'

    elif sid == '4-2':  # 浮点数
        examples = [
            ("示例1：浮点数计算",
             '# 浮点数就是带小数点的数字\n# 注意：浮点数计算可能有精度问题\n\nprice = 19.9\nquantity = 3\ntotal = price * quantity\n\nprint(f"单价: {price}元")\nprint(f"数量: {quantity}件")\nprint(f"总价: {total}")\nprint(f"格式化显示: {total:.2f}元")\n\n# 精度问题示例: 0.1 + 0.2\nprint(f"\\n0.1 + 0.2 = {0.1 + 0.2}")\nprint("这是浮点数的存储特性，不是bug!")',
             "单价: 19.9元\n数量: 3件\n总价: 59.699999999999996\n格式化显示: 59.70元\n\n0.1 + 0.2 = 0.30000000000000004\n这是浮点数的存储特性，不是bug!"),
            ("示例2：round函数",
             '# round() 函数可以四舍五入\n# 语法: round(数字, 保留小数位数)\n\nvalue = 3.1415926\n\nprint(f"原值: {value}")\nprint(f"保留0位: {round(value)}")\nprint(f"保留1位: {round(value, 1)}")\nprint(f"保留2位: {round(value, 2)}")\nprint(f"保留4位: {round(value, 4)}")',
             "原值: 3.1415926\n保留0位: 3\n保留1位: 3.1\n保留2位: 3.14\n保留4位: 3.1416"),
        ]
        practice_tasks = [
            "计算圆的面积(半径7)，保留2位小数",
            "给定价格34.75，数量5，计算总价，格式化显示",
            "计算0.1+0.2，并用round修正到1位小数后打印",
        ]
        solution = '# 练习参考答案\nimport math\nr = 7\narea = math.pi * r * r\nprint(f"半径{r}的圆面积: {area:.2f}")\n\nprice = 34.75\nqty = 5\nprint(f"总价: {round(price * qty, 2)}元")\n\n# 浮点数修正\nresult = 0.1 + 0.2\nprint(f"0.1 + 0.2 = {result}, 修正后: {round(result, 1)}")'

    elif sid == '4-3':  # 字符串
        examples = [
            ("示例1：字符串的基本操作",
             '# 字符串是用引号包裹的字符序列\n# 单引号、双引号、三引号都可以\n\ns = "Hello, Python!"\n\nprint(f"原字符串: {s}")\nprint(f"长度: {len(s)}")\nprint(f"大写: {s.upper()}")\nprint(f"小写: {s.lower()}")\nprint(f"首字母大写: {s.title()}")\nprint(f"是否以Hello开头: {s.startswith(\"Hello\")}")\nprint(f"是否包含Python: {\"Python\" in s}")\nprint(f"替换: {s.replace(\"Python\", \"世界\")}")',
             "原字符串: Hello, Python!\n长度: 14\n大写: HELLO, PYTHON!\n小写: hello, python!\n首字母大写: Hello, Python!\n是否以Hello开头: True\n是否包含Python: True\n替换: Hello, 世界!"),
            ("示例2：字符串拼接和重复",
             '# 用 + 拼接字符串\n# 用 * 重复字符串\n\npart1 = "学习"\npart2 = "Python"\n\nfull = part1 + part2\nprint(f"拼接: {full}")\n\n# 打印漂亮的分隔符\nprint("=" * 40)\nprint("  " + full + " 很有趣!  ")\nprint("=" * 40)\n\n# 重复打印\nprint("加油! " * 5)',
             "拼接: 学习Python\n========================================\n  学习Python 很有趣!  \n========================================\n加油! 加油! 加油! 加油! 加油! "),
            ("示例3：字符串索引和切片",
             '# 字符串的每个字符都有位置编号（索引从0开始）\n# s[位置] 取出单个字符\n# s[开始:结束] 取出一段（切片）\n\ns = "ABCDEFG"\n\nprint(f"原字符串: {s}")\nprint(f"第1个字符: {s[0]}")\nprint(f"第3个字符: {s[2]}")\nprint(f"最后一个: {s[-1]}")\nprint(f"前3个字符: {s[:3]}")\nprint(f"第3到第5个: {s[2:5]}")\nprint(f"后3个字符: {s[-3:]}")',
             "原字符串: ABCDEFG\n第1个字符: A\n第3个字符: C\n最后一个: G\n前3个字符: ABC\n第3到第5个: CDE\n后3个字符: EFG"),
        ]
        practice_tasks = [
            "定义一个字符串'Python编程很好玩'，打印它的长度、大写形式",
            "打印'学习Python'重复5次",
            "从字符串'数据分析Python'中取出'Python'并打印",
        ]
        solution = '# 练习参考答案\ns = "Python编程很好玩"\nprint(f"长度: {len(s)}")\nprint(f"大写: {s.upper()}")\n\nprint("学习Python " * 5)\n\n# 取出Python\ns2 = "数据分析Python"\nprint(s2[4:])  # 从索引4到末尾'

    elif sid == '4-4':  # 布尔
        examples = [
            ("示例1：布尔值与逻辑运算",
             '# 布尔值只有两个: True 和 False (首字母大写)\n# 逻辑运算符: and, or, not\n\nis_student = True\nis_vip = False\n\nprint(f"是学生: {is_student}")\nprint(f"是VIP: {is_vip}")\nprint(f"学生 AND VIP: {is_student and is_vip}")\nprint(f"学生 OR VIP: {is_student or is_vip}")\nprint(f"不是学生: {not is_student}")\nprint(f"不是VIP: {not is_vip}")',
             "是学生: True\n是VIP: False\n学生 AND VIP: False\n学生 OR VIP: True\n不是学生: False\n不是VIP: True"),
            ("示例2：比较运算的结果是布尔值",
             '# 比较运算符: ==, !=, >, <, >=, <=\n# 比较的结果是True或False\n\nscore = 85\n\nprint(f"{score} >= 60: {score >= 60}")\nprint(f"{score} >= 90: {score >= 90}")\nprint(f"{score} == 85: {score == 85}")\nprint(f"{score} != 100: {score != 100}")\n\n# 可以用布尔值做条件判断\nif score >= 60:\n    print("及格了!")\nelse:\n    print("需要加油!")',
             "85 >= 60: True\n85 >= 90: False\n85 == 85: True\n85 != 100: True\n及格了!"),
        ]
        practice_tasks = [
            "定义变量age=20，判断并打印是否是成年人、是否是青少年、是否退休",
            "定义两个数字，用逻辑运算判断它们是否都大于10",
        ]
        solution = '# 练习参考答案\nage = 20\nprint(f"{age}岁是成年人吗？ {age >= 18}")\nprint(f"{age}岁是青少年吗？ {13 <= age <= 19}")\nprint(f"{age}岁退休了吗？ {age >= 65}")\n\n# 两个数是否都大于10\na, b = 15, 8\nprint(f"{a}和{b}都大于10吗？ {a > 10 and b > 10}")'

    elif sid == '4-5':  # 类型转换
        examples = [
            ("示例1：常用类型转换",
             '# 类型转换函数: int(), float(), str(), bool()\n\n# 字符串转数字\nnum_str = "123"\nnum_int = int(num_str)\nprint(f"字符串 \\"{num_str}\\" 转为整数: {num_int}")\nprint(f"类型: {type(num_str)} -> {type(num_int)}")\n\n# 数字转字符串\nage = 18\nage_str = str(age)\nprint(f"数字 {age} 转为字符串: \\"{age_str}\\"")\n\n# 浮点转整数（截断小数部分）\npi = 3.14159\nprint(f"{pi} 转成整数: {int(pi)} (不是四舍五入，是截断)")\n\n# 整数转浮点数\nprint(f"5 转成浮点数: {float(5)}")',
             '字符串 "123" 转为整数: 123\n类型: <class \'str\'> -> <class \'int\'>\n数字 18 转为字符串: "18"\n3.14159 转成整数: 3 (不是四舍五入，是截断)\n5 转成浮点数: 5.0'),
            ("示例2：实际应用",
             '# 从input得到的是字符串，需要转成数字才能计算\n\nprint("=" * 30)\nprint("   简单的购物计算")\nprint("=" * 30)\n\nprice_str = input("请输入商品价格: ")\nqty_str = input("请输入购买数量: ")\n\n# 转成浮点数和整数\nprice = float(price_str)\nqty = int(qty_str)\ntotal = price * qty\n\nprint(f"商品: {price}元 x {qty}件 = {total:.2f}元")',
             "==============================\n   简单的购物计算\n==============================\n请输入商品价格: 19.99\n请输入购买数量: 3\n商品: 19.99元 x 3件 = 59.97元"),
        ]
        practice_tasks = [
            "把字符串'456'转成整数，加100后打印",
            "把数字789转成字符串，拼接'是测试数字'后打印",
            "让用户输入两个数字，计算它们的乘积并显示",
        ]
        solution = '# 练习参考答案\ns = "456"\nnum = int(s)\nprint(f"{num} + 100 = {num + 100}")\n\nn = 789\nprint(str(n) + " 是测试数字")\n\n# 用户输入计算\nx = float(input("第一个数字: "))\ny = float(input("第二个数字: "))\nprint(f"{x} x {y} = {x * y}")'

    # ========== 第5-11章 以及通用内容 ==========
    # 5-1 input输入
    # 5-2 算术运算符
    # 5-3 比较运算符
    # 5-4 逻辑运算符
    # 5-5 运算符优先级
    # 6-1 if单分支
    # 6-2 if-else双分支
    # 6-3 if-elif多分支
    # 6-4 条件嵌套
    # 7-1 for循环
    # 7-2 range函数
    # 7-3 while循环
    # 7-4 break
    # 7-5 continue
    # 7-6 循环嵌套
    # 8-1 列表
    # 8-2 列表增删
    # 8-3 列表查询修改
    # 8-4 列表方法
    # 9-1 字典
    # 9-2 字典键值
    # 9-3 字典增删改
    # 9-4 字典遍历
    # 10-1 函数定义
    # 10-2 参数传递
    # 10-3 返回值
    # 10-4 作用域
    # 10-5 匿名函数
    # 11-1 项目准备
    # 11-2 数据分析
    # 11-3 数据展示
    # 11-4 项目总结

    # 如果没有预定义的详细内容，使用通用模板
    else:
        examples = [
            ("示例1：基础用法",
             f'# {title} - 基础练习\n# 知识点: {kp_text}\n\n# 这里是示例代码\nprint("=" * 30)\nprint("  {title} 练习")\nprint("=" * 30)\n\n# 简单测试\nvalue = 10\nprint(f"测试值: {{value}}")\nprint(f"加倍: {{value * 2}}")\nprint(f"平方: {{value ** 2}}")\nprint("练习完成!")',
             "==============================\n  " + title + " 练习\n==============================\n测试值: 10\n加倍: 20\n平方: 100\n练习完成!"),
            ("示例2：实际应用",
             f'# {title} - 实际应用\n# 根据本节知识点编写更复杂的代码\n\ndata = [1, 2, 3, 4, 5]\n\nprint("=" * 30)\nprint("  数据处理示例")\nprint("=" * 30)\n\n# 处理数据\nfor i, v in enumerate(data):\n    print(f"第{{i+1}}个: {{v}}")\n\nprint("=" * 30)\nprint(f"总计: {{sum(data)}}")\nprint(f"个数: {{len(data)}}")\nprint(f"平均: {{sum(data)/len(data):.1f}}")',
             "==============================\n  数据处理示例\n==============================\n第1个: 1\n第2个: 2\n第3个: 3\n第4个: 4\n第5个: 5\n==============================\n总计: 15\n个数: 5\n平均: 3.0"),
        ]
        practice_tasks = [
            f"写一个简单的{title}程序，打印3行不同的内容",
            f"创建一个使用{title}的实际案例（如计算、转换等）",
            f"尝试在{title}中加入用户输入",
        ]
        solution = f'# {title}练习参考答案\nprint("=" * 30)\nprint("  我的练习")\nprint("=" * 30)\n\nvalue = input("请输入一个数字: ")\nprint(f"你输入了: {{value}}")\nprint("练习完成!")'

    return {
        'title': practice_title,
        'description': f'{title}实操练习：{kp_text}',
        'knowledge_points': kp,
        'examples': examples,
        'practice_tasks': practice_tasks,
        'solution': solution,
    }


# ========== HTML 生成器 ============

def make_practice_html(course_key, course_info, chapter, section):
    """生成Python实操页面HTML"""
    sid = section['id']
    title = section['title']
    chapter_title = chapter['title']

    content = generate_detailed_content(section)
    sidebar_html = make_sidebar_html(course_info, sid)

    html = ""
    # --- Header ---
    html += '<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n'
    html += '    <meta charset="UTF-8">\n'
    html += '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    html += '    <title>' + title + ' - Python实操 | ' + course_info['name'] + '</title>\n'
    html += '    <link rel="stylesheet" href="../../css/styles.css">\n'
    html += '    <style>\n'
    html += '        .practice-container { background: #fff; border-radius: 12px; padding: 2rem; margin-top: 1.5rem; border: 1px solid #e2e8f0; }\n'
    html += '        .practice-title { font-size: 1.3rem; color: #1e3a5f; margin-bottom: 0.5rem; font-weight: 600; }\n'
    html += '        .practice-desc { color: #4a5568; margin-bottom: 1.5rem; padding: 1rem; background: #f7fafc; border-radius: 8px; border-left: 4px solid #38a169; }\n'
    html += '        .example-box { border: 1px solid #cbd5e0; border-radius: 8px; padding: 1.2rem; margin-bottom: 1.5rem; background: #fff; }\n'
    html += '        .example-title { color: #2b6cb0; font-weight: 600; margin-bottom: 0.8rem; font-size: 1.05rem; }\n'
    html += '        .code-block { background: #1e293b; color: #e2e8f0; padding: 1.2rem; border-radius: 8px; margin: 0.5rem 0; font-family: Consolas, "Courier New", monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.6; font-size: 0.92rem; }\n'
    html += '        .result-block { background: #f0fdf4; border: 1px dashed #86efac; color: #166534; padding: 1rem; border-radius: 8px; margin-top: 0.8rem; font-family: Consolas, monospace; white-space: pre-wrap; font-size: 0.92rem; }\n'
    html += '        .result-block::before { content: "运行结果:"; display: block; font-weight: bold; margin-bottom: 0.5rem; color: #15803d; }\n'
    html += '        .copy-btn { background: #38a169; color: white; border: none; padding: 0.4rem 1rem; border-radius: 6px; cursor: pointer; font-size: 0.85rem; float: right; }\n'
    html += '        .copy-btn:hover { background: #276749; }\n'
    html += '        .practice-area { background: #1e293b; border: 2px solid #38a169; border-radius: 12px; padding: 1.8rem; margin-top: 1.5rem; }\n'
    html += '        .practice-area-title { color: #86efac; font-weight: 600; font-size: 1.2rem; margin-bottom: 1rem; }\n'
    html += '        .practice-task { background: #0f172a; border-left: 4px solid #38a169; padding: 0.9rem 1.2rem; margin-bottom: 0.7rem; border-radius: 6px; color: #e2e8f0; font-size: 0.95rem; }\n'
    html += '        .practice-task strong { color: #fbbf24; }\n'
    html += '        .practice-placeholder { background: #0f172a; border: 1px dashed #475569; border-radius: 8px; padding: 2rem; margin-top: 1.2rem; color: #94a3b8; text-align: center; font-style: italic; min-height: 100px; font-family: Consolas, monospace; font-size: 0.95rem; }\n'
    html += '        .solution-box { background: #f7fafc; border-radius: 8px; padding: 1.2rem; margin-top: 1.2rem; border: 1px solid #e2e8f0; }\n'
    html += '        .solution-box summary { cursor: pointer; color: #2b6cb0; font-weight: 600; user-select: none; }\n'
    html += '        .online-links { display: flex; flex-wrap: wrap; gap: 0.8rem; margin-top: 1.5rem; }\n'
    html += '        .online-links a { background: #4299e1; color: white; padding: 0.6rem 1.2rem; border-radius: 6px; text-decoration: none; font-size: 0.9rem; }\n'
    html += '        .online-links a:hover { background: #2b6cb0; }\n'
    html += '        .kp-list { margin: 0.5rem 0; padding-left: 1.5rem; color: #2d3748; }\n'
    html += '        .kp-list li { margin: 0.3rem 0; }\n'
    html += '        .section-main-title { margin-bottom: 1rem; }\n'
    html += '    </style>\n'
    html += '</head>\n<body>\n'

    # --- Navbar ---
    html += '    <nav class="navbar">\n        <div class="container">\n'
    html += '            <h1>张茵茵的学习空间</h1>\n'
    html += '            <ul class="nav-links">\n'
    html += '                <li><a href="../../index.html">首页</a></li>\n'
    html += '                <li><a href="../../index.html#courses">课程</a></li>\n'
    html += '                <li><a href="../../learning-path.html">学习路径</a></li>\n'
    html += '            </ul>\n        </div>\n    </nav>\n'

    # --- Sidebar ---
    html += '    <div class="sidebar-toggle" onclick="toggleSidebar()"></div>\n'
    html += '    <div class="sidebar-overlay" onclick="toggleSidebar()"></div>\n'
    html += '    <aside class="sidebar">\n'
    html += '        <div class="sidebar-header"><h4>' + course_info['icon'] + ' ' + course_info['name'] + ' 列表</h4></div>\n'
    html += '        ' + sidebar_html + '\n'
    html += '    </aside>\n'

    # --- Main Content ---
    html += '    <section class="course-content">\n        <div class="container">\n'
    html += '            <div class="content-wrapper">\n                <div class="content-main">\n'

    # Breadcrumb
    html += '                    <div class="breadcrumb-nav"><a href="section-' + sid + '.html">← 返回小节</a></div>\n'

    # Title
    html += '                    <div class="section-page">\n'
    html += '                        <h2 class="section-main-title">💻 ' + title + ' - Python实操</h2>\n'
    html += '                        <div class="section-sub-title"><h3>第' + str(chapter['num']) + '章 ' + chapter_title + '</h3></div>\n'

    # 简介 + 知识点
    html += '                    <div class="practice-container">\n'
    html += '                        <div class="practice-title">' + content['title'] + '</div>\n'
    html += '                        <div class="practice-desc">' + content['description'] + '</div>\n'
    if content['knowledge_points']:
        html += '                        <div style="margin: 1rem 0; padding: 1rem; background: #ebf8ff; border-radius: 6px;">\n'
        html += '                            <strong>本节知识点：</strong>\n                            <ul class="kp-list">\n'
        for kp in content['knowledge_points']:
            html += '                                <li>' + kp + '</li>\n'
        html += '                            </ul>\n                        </div>\n'

    # --- 示例代码区 ---
    html += '                    <h3 style="color: #2b6cb0; margin-top: 1.5rem; margin-bottom: 1rem;">📖 参考示例</h3>\n'
    for idx, (ex_title, ex_code, ex_result) in enumerate(content['examples'], 1):
        html += '                    <div class="example-box">\n'
        html += '                        <div class="example-title">' + ex_title + '</div>\n'
        html += '                        <button class="copy-btn" onclick="copyCode(\'code-' + sid + '-' + str(idx) + '\')">复制代码</button>\n'
        html += '                        <div style="clear: both;"></div>\n'
        html += '                        <div class="code-block" id="code-' + sid + '-' + str(idx) + '">' + ex_code + '</div>\n'
        html += '                        <div class="result-block">' + ex_result + '</div>\n'
        html += '                    </div>\n'

    # --- 练习区 ---
    html += '                    <div class="practice-area">\n'
    html += '                        <div class="practice-area-title">✍️ 动手练习区</div>\n'
    html += '                        <p style="color: #cbd5e1; margin-bottom: 1rem; font-size: 0.95rem;">请在本地Python环境中完成以下练习。点击下方链接可以使用在线编辑器！</p>\n'
    for idx, task in enumerate(content['practice_tasks'], 1):
        html += '                        <div class="practice-task"><strong>练习' + str(idx) + '：</strong>' + task + '</div>\n'
    html += '                        <div class="practice-placeholder">（在此理解代码后，尝试自己动手写一写）</div>\n'

    # 参考答案
    html += '                        <details class="solution-box">\n'
    html += '                            <summary>👀 查看参考答案（建议先自己写再看）</summary>\n'
    html += '                            <div class="code-block">' + content['solution'] + '</div>\n'
    html += '                        </details>\n'

    # --- 在线运行链接 ---
    html += '                        <div style="margin-top: 2rem;">\n'
    html += '                            <strong style="color: #e2e8f0;">🚀 在线运行Python代码（复制代码后到以下网站粘贴运行）：</strong>\n'
    html += '                            <div class="online-links">\n'
    html += '                                <a href="https://www.runoob.com/try/runcode.php?filename=HelloWorld&type=python3" target="_blank">菜鸟教程在线编辑器</a>\n'
    html += '                                <a href="https://www.online-python.com/" target="_blank">Online-Python</a>\n'
    html += '                                <a href="https://pythontutor.com/python-compiler.html" target="_blank">PythonTutor可视化</a>\n'
    html += '                            </div>\n'
    html += '                        </div>\n'
    html += '                    </div>\n'  # end practice-container

    # 回到 section-page
    # --- Navigation ---
    html += '                    <div class="section-navigation">\n'
    html += '                        <a href="section-' + sid + '.html" class="nav-btn prev-btn">← 返回小节详情</a>\n'
    html += '                    </div>\n'
    html += '                    </div>\n'
    html += '                </div>\n            </div>\n        </div>\n    </section>\n'

    # --- Footer ---
    html += '    <footer class="footer"><p>张茵茵的学习空间</p></footer>\n'

    # --- JavaScript ---
    html += '    <script>\n'
    html += '        function copyCode(id) {\n'
    html += '            const text = document.getElementById(id).textContent;\n'
    html += '            navigator.clipboard.writeText(text).then(() => {\n'
    html += '                const btn = event.target;\n'
    html += '                const original = btn.textContent;\n'
    html += '                btn.textContent = "✓ 已复制";\n'
    html += '                setTimeout(() => btn.textContent = original, 1500);\n'
    html += '            }).catch(err => alert("复制失败，请手动选择复制"));\n'
    html += '        }\n'
    html += '        function toggleSidebar() {\n'
    html += '            document.body.classList.toggle("sidebar-open");\n'
    html += '        }\n'
    html += '    </script>\n'

    html += '</body>\n</html>'
    return html


# ========== 主函数 ==========

def main():
    base_path = "/workspace/courses"
    total_count = 0

    for course_key, course_info in COURSES.items():
        course_dir = os.path.join(base_path, course_key)
        os.makedirs(course_dir, exist_ok=True)

        for chapter in course_info['chapters']:
            for section in chapter['sections']:
                html = make_practice_html(course_key, course_info, chapter, section)
                filename = "practice-" + section['id'] + ".html"
                filepath = os.path.join(course_dir, filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                total_count += 1
                print("生成: " + course_key + "/" + filename)

    print("\n完成！共生成 " + str(total_count) + " 个 Python实操 页面！")


if __name__ == "__main__":
    main()
