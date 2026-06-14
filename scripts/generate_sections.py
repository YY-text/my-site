#!/usr/bin/env python3
"""
批量生成Python课程小节详情页
每个小节包含：通俗讲解、核心知识点、示例代码、10道练习题
"""

import os

# 课程小节内容数据（完整版）
SECTIONS = {
    "1-1": {
        "chapter": "第1章 Python入门认知",
        "title": "语言简介",
        "explanation": "Python是一种简单易懂又非常强大的编程语言，由Guido van Rossum在1991年创建。它就像一把瑞士军刀，可以用来做网站开发、数据分析、人工智能等各种事情。Python的特点是代码简洁，读起来像英文，非常适合零基础学习。",
        "key_points": [
            "Python是一种解释型语言，无需编译即可运行",
            "Python语法简洁，可读性强，学习成本低",
            "Python拥有丰富的第三方库，生态系统完善",
            "Python广泛应用于数据分析、Web开发、AI等领域",
            "Python跨平台，Windows、Mac、Linux都能运行"
        ],
        "code": '''print("Hello, Python!")
# 输出：Hello, Python!

# 简单计算
result = 1 + 2 * 3
print(result)  # 输出：7''',
        "quiz": [
            {"q": "Python是在哪一年首次发布的？", "options": ["1995", "2000", "1991", "1985"], "answer": "C", "explanation": "Python由Guido van Rossum在1991年首次发布。"},
            {"q": "Python的创始人是谁？", "options": ["Bill Gates", "Guido van Rossum", "Mark Zuckerberg", "Steve Jobs"], "answer": "B", "explanation": "Python的创始人是Guido van Rossum，荷兰程序员。"},
            {"q": "Python属于什么类型的语言？", "options": ["编译型语言", "解释型语言", "汇编语言", "机器语言"], "answer": "B", "explanation": "Python是解释型语言，代码逐行执行，无需预先编译。"},
            {"q": "以下哪个不是Python的特点？", "options": ["语法简洁", "跨平台", "生态丰富", "只能用于网站开发"], "answer": "D", "explanation": "Python应用领域广泛，包括数据分析、AI、Web开发等。"},
            {"q": "Python的设计哲学强调什么？", "options": ["代码的复杂性", "代码的可读性", "代码的长度", "代码的加密"], "answer": "B", "explanation": "Python的设计哲学强调代码的可读性和简洁性。"},
            {"q": "Python的文件扩展名通常是？", "options": ["txt", "py", "java", "html"], "answer": "B", "explanation": "Python源代码文件的扩展名是.py。"},
            {"q": "Python不能运行在哪个操作系统？", "options": ["Windows", "MacOS", "Linux", "以上都能运行"], "answer": "D", "explanation": "Python是跨平台语言，可以在Windows、MacOS、Linux上运行。"},
            {"q": "Python的第三方库是通过什么安装的？", "options": ["pip", "npm", "yarn", "brew"], "answer": "A", "explanation": "Python的第三方库通过pip安装。"},
            {"q": "以下哪个不是Python的应用领域？", "options": ["数据分析", "人工智能", "Web开发", "操作系统开发"], "answer": "D", "explanation": "Python不适合开发操作系统，操作系统通常用C/C++开发。"},
            {"q": "对于零基础学习Python，以下说法正确的是？", "options": ["必须先学其他语言", "Python学习难度很高", "Python非常适合零基础", "Python只能专业人士学习"], "answer": "C", "explanation": "Python语法简洁，非常适合零基础学习。"}
        ]
    },
    "1-2": {
        "chapter": "第1章 Python入门认知",
        "title": "环境安装",
        "explanation": "安装Python就像安装其他软件一样简单。你可以去Python官网下载安装包，然后按照提示一步步安装。安装完成后，在命令行输入python就能验证是否安装成功。建议安装Python 3.x版本，因为它是目前的主流版本。",
        "key_points": [
            "从python.org官网下载Python安装包",
            "安装时勾选Add Python to PATH选项",
            "Windows用户可通过命令行验证安装",
            "Mac和Linux系统通常已预装Python",
            "推荐安装Python 3.8及以上版本"
        ],
        "code": '''# 验证Python安装
# 在命令行输入：
python --version
# 输出：Python 3.x.x

# 进入Python交互模式
python
>>> print("安装成功！")''',
        "quiz": [
            {"q": "Python安装包应该从哪里下载？", "options": ["任意网站", "python.org官网", "GitHub", "App Store"], "answer": "B", "explanation": "应从python.org官网下载，确保安全可靠。"},
            {"q": "安装Python时应该勾选哪个选项？", "options": ["自动更新", "Add Python to PATH", "安装所有库", "创建桌面图标"], "answer": "B", "explanation": "勾选Add Python to PATH可将Python添加到系统环境变量。"},
            {"q": "如何验证Python是否安装成功？", "options": ["重启电脑", "打开浏览器", "命令行输入python --version", "查看文件夹"], "answer": "C", "explanation": "在命令行输入python --version可查看Python版本。"},
            {"q": "推荐安装的Python版本是？", "options": ["Python 2.x", "Python 3.8及以上", "任意版本", "最新测试版"], "answer": "B", "explanation": "推荐安装Python 3.8及以上稳定版本。"},
            {"q": "Mac系统是否需要单独安装Python？", "options": ["必须安装", "通常已预装", "不能安装", "只能装Python 2"], "answer": "B", "explanation": "Mac系统通常已预装Python，但可能需要更新版本。"},
            {"q": "Windows安装Python后，Python存放在哪里？", "options": ["桌面", "系统PATH环境变量指定的路径", "浏览器", "回收站"], "answer": "B", "explanation": "Python安装在指定目录，通过PATH环境变量访问。"},
            {"q": "Python交互模式的标志是？", "options": ["$", "#", ">>>", "@"], "answer": "C", "explanation": "Python交互模式以>>>作为输入提示符。"},
            {"q": "安装Python后，pip工具的作用是？", "options": ["编辑代码", "安装第三方库", "运行程序", "调试代码"], "answer": "B", "explanation": "pip是Python的包管理工具，用于安装第三方库。"},
            {"q": "可以同时安装多个Python版本吗？", "options": ["不可以", "可以，使用虚拟环境管理", "必须卸载旧版本", "只能装一个"], "answer": "B", "explanation": "可以安装多个版本，使用虚拟环境或pyenv管理。"},
            {"q": "安装Python时，IDLE是什么？", "options": ["一个游戏", "Python自带的简单编辑器", "安装程序", "系统工具"], "answer": "B", "explanation": "IDLE是Python自带的简单代码编辑器和交互环境。"}
        ]
    },
    "1-3": {
        "chapter": "第1章 Python入门认知",
        "title": "运行方式",
        "explanation": "Python代码有两种运行方式：交互模式和脚本模式。交互模式就像聊天，输入一行代码立刻看到结果，适合测试和学习。脚本模式是把代码写在文件里，然后一次性运行整个文件，适合完整的程序。",
        "key_points": [
            "交互模式：逐行输入代码，立即执行",
            "脚本模式：代码保存为py文件后运行",
            "交互模式适合快速测试和调试",
            "脚本模式适合完整程序的开发",
            "使用python命令运行脚本文件"
        ],
        "code": '''# 交互模式示例
>>> print("Hello")
Hello
>>> 1 + 2
3

# 脚本模式
# 1. 将代码保存为 hello.py
print("Hello, Python!")

# 2. 命令行运行
python hello.py''',
        "quiz": [
            {"q": "Python交互模式的提示符是？", "options": ["$", "#", ">>>", "@"], "answer": "C", "explanation": "Python交互模式使用>>>作为提示符。"},
            {"q": "脚本模式下，Python代码保存在什么文件中？", "options": ["txt文件", "py文件", "doc文件", "pdf文件"], "answer": "B", "explanation": "Python脚本文件使用.py扩展名。"},
            {"q": "交互模式适合做什么？", "options": ["开发大型程序", "快速测试和调试", "安装软件", "编辑文档"], "answer": "B", "explanation": "交互模式适合快速测试代码和学习。"},
            {"q": "如何运行一个Python脚本文件？", "options": ["双击文件", "python 文件名.py", "打开文件", "拖到浏览器"], "answer": "B", "explanation": "使用python命令加文件名来运行脚本。"},
            {"q": "脚本模式相比交互模式的优势是？", "options": ["更慢", "可以保存和运行完整程序", "不能保存", "只能一行"], "answer": "B", "explanation": "脚本模式可以保存完整程序并反复运行。"},
            {"q": "在交互模式中，输入代码后会发生什么？", "options": ["保存到文件", "立即执行并显示结果", "等待保存", "不执行"], "answer": "B", "explanation": "交互模式中代码立即执行并显示结果。"},
            {"q": "退出Python交互模式的命令是？", "options": ["quit()", "exit()", "两者都可以", "close()"], "answer": "C", "explanation": "quit()和exit()都可以退出交互模式。"},
            {"q": "脚本文件hello.py如何运行？", "options": ["hello.py", "python hello.py", "run hello.py", "start hello.py"], "answer": "B", "explanation": "使用python hello.py命令运行脚本。"},
            {"q": "交互模式中如何查看变量值？", "options": ["必须用print", "直接输入变量名", "用show()", "用display()"], "answer": "B", "explanation": "交互模式中直接输入变量名即可查看值。"},
            {"q": "哪种模式更适合初学者学习？", "options": ["脚本模式", "交互模式", "编译模式", "调试模式"], "answer": "B", "explanation": "交互模式可以即时看到结果，更适合初学者。"}
        ]
    },
    "1-4": {
        "chapter": "第1章 Python入门认知",
        "title": "编辑器使用",
        "explanation": "写Python代码需要一个好用的编辑器。初学者可以用Python自带的IDLE，简单易用。进阶后可以使用VS Code、PyCharm等专业编辑器，它们有代码高亮、自动补全、错误提示等功能，让编程更高效。",
        "key_points": [
            "IDLE是Python自带的简单编辑器",
            "VS Code免费且功能强大，适合初学者",
            "PyCharm专业版功能最全面",
            "编辑器提供代码高亮和自动补全",
            "选择编辑器根据个人习惯和需求"
        ],
        "code": '''# IDLE使用方法
# 1. 打开IDLE
# 2. File -> New File 创建新文件
# 3. 写入代码
# 4. Run -> Run Module 运行

# VS Code使用方法
# 1. 安装Python扩展插件
# 2. 创建py文件
# 3. 按 F5 或点击运行按钮''',
        "quiz": [
            {"q": "Python自带的编辑器叫什么？", "options": ["VS Code", "IDLE", "PyCharm", "Sublime"], "answer": "B", "explanation": "IDLE是Python安装时自带的基础编辑器。"},
            {"q": "VS Code需要安装什么才能写Python？", "options": ["不需要", "Python扩展插件", "付费版", "特殊软件"], "answer": "B", "explanation": "VS Code需要安装Python扩展插件。"},
            {"q": "PyCharm的特点是？", "options": ["免费简单", "功能全面专业", "不能调试", "只能写Python"], "answer": "B", "explanation": "PyCharm是专业的Python开发工具，功能全面。"},
            {"q": "代码高亮的作用是？", "options": ["让代码更漂亮", "区分不同类型的代码元素", "让代码运行更快", "加密代码"], "answer": "B", "explanation": "代码高亮用不同颜色区分关键字、变量、字符串等。"},
            {"q": "自动补全功能的作用是？", "options": ["自动写代码", "提示并补全代码", "自动运行", "自动保存"], "answer": "B", "explanation": "自动补全帮助快速输入代码，减少错误。"},
            {"q": "初学者推荐使用哪个编辑器？", "options": ["IDLE或VS Code", "PyCharm专业版", "记事本", "Word"], "answer": "A", "explanation": "IDLE简单易用，VS Code免费强大，适合初学者。"},
            {"q": "在IDLE中运行代码的快捷键是？", "options": ["F5", "Ctrl+R", "F9", "Ctrl+Enter"], "answer": "A", "explanation": "在IDLE中按F5运行代码。"},
            {"q": "编辑器的调试功能可以做什么？", "options": ["写代码", "查找和修复错误", "运行代码", "保存文件"], "answer": "B", "explanation": "调试功能帮助查找和修复代码错误。"},
            {"q": "可以用Word写Python代码吗？", "options": ["可以，推荐使用", "可以，但不推荐", "不可以", "必须用"], "answer": "B", "explanation": "Word可以写代码但没有编程功能，不推荐。"},
            {"q": "专业Python开发者常用哪个编辑器？", "options": ["记事本", "IDLE", "PyCharm或VS Code", "Word"], "answer": "C", "explanation": "专业开发者常用PyCharm或VS Code。"}
        ]
    },
    "2-1": {
        "chapter": "第2章 基础输出与注释",
        "title": "print输出",
        "explanation": "print是Python最常用的函数，用来在屏幕上显示内容。就像说话一样，你告诉print要说什么，它就会显示出来。可以输出文字、数字、计算结果等各种内容。",
        "key_points": [
            "print函数用于输出内容到屏幕",
            "可以输出字符串、数字、变量等",
            "多个内容用逗号分隔，自动添加空格",
            "sep参数可自定义分隔符",
            "end参数可自定义结尾字符"
        ],
        "code": '''# 基本输出
print("Hello, Python!")

# 输出数字
print(100)
print(3.14)

# 输出多个内容
print("姓名:", "张三", "年龄:", 18)

# 自定义分隔符
print("A", "B", "C", sep="-")  # 输出：A-B-C

# 自定义结尾
print("第一行", end="|")
print("第二行")  # 输出：第一行|第二行''',
        "quiz": [
            {"q": "print函数的作用是？", "options": ["输入数据", "输出内容到屏幕", "计算数据", "保存文件"], "answer": "B", "explanation": "print函数用于在屏幕上显示输出内容。"},
            {"q": "print输出字符串需要用什么包裹？", "options": ["括号", "引号", "方括号", "花括号"], "answer": "B", "explanation": "字符串需要用引号（单引号或双引号）包裹。"},
            {"q": "print(1, 2, 3)输出结果是什么？", "options": ["123", "1 2 3", "1,2,3", "(1,2,3)"], "answer": "B", "explanation": "多个内容默认用空格分隔。"},
            {"q": "sep参数的作用是？", "options": ["设置结尾", "设置分隔符", "设置颜色", "设置字体"], "answer": "B", "explanation": "sep参数用于自定义多个内容之间的分隔符。"},
            {"q": "print默认的结尾字符是？", "options": ["空格", "换行符", "逗号", "无"], "answer": "B", "explanation": "print默认在结尾添加换行符。"},
            {"q": "如何让print不换行？", "options": ["print不加内容", "end为空字符串", "sep为空字符串", "使用input"], "answer": "B", "explanation": "设置end为空字符串可以让print不换行。"},
            {"q": "print可以输出变量吗？", "options": ["不可以", "可以", "只能输出字符串", "只能输出数字"], "answer": "B", "explanation": "print可以输出任何类型的内容，包括变量。"},
            {"q": "print(年龄, 18)输出什么？", "options": ["年龄18", "年龄 18", "(年龄, 18)", "年龄:18"], "answer": "B", "explanation": "输出多个内容时默认用空格分隔。"},
            {"q": "以下哪个是正确的print用法？", "options": ["print Hello", "print(Hello)", "print[Hello]", "print{Hello}"], "answer": "B", "explanation": "print需要用括号，字符串用引号包裹。"},
            {"q": "print(A, B, sep=-)输出什么？", "options": ["A B", "A-B", "AB", "A,B"], "answer": "B", "explanation": "sep=-设置分隔符为横线。"}
        ]
    },
    "2-2": {
        "chapter": "第2章 基础输出与注释",
        "title": "格式输出",
        "explanation": "格式输出让打印的内容更整齐美观。Python有三种方式：百分号格式化（老方法）、format方法（较新）、f-string（最新最简洁）。f-string最推荐，在字符串前加f，用花括号放入变量即可。",
        "key_points": [
            "f-string是最新的格式化方式，简洁易用",
            "format方法使用花括号占位符",
            "百分号格式化使用s、d等占位符",
            "格式化可以控制数字的小数位数",
            "格式化让输出内容更整齐美观"
        ],
        "code": '''# f-string方式（推荐）
name = "张三"
age = 18
print(f"姓名: {name}, 年龄: {age}")

# format方法
print("姓名: {}, 年龄: {}".format("张三", 18))

# 百分号格式化
print("姓名: %s, 年龄: %d" % ("张三", 18))

# 控制小数位数
price = 19.99
print(f"价格: {price:.2f}元")  # 输出：价格: 19.99元''',
        "quiz": [
            {"q": "f-string需要在字符串前加什么？", "options": ["s", "f", "r", "b"], "answer": "B", "explanation": "f-string需要在字符串引号前加f。"},
            {"q": "f-string中变量放在哪里？", "options": ["括号", "花括号", "方括号", "引号"], "answer": "B", "explanation": "f-string中变量放在花括号内。"},
            {"q": "format方法使用什么作为占位符？", "options": ["百分号", "花括号", "方括号", "圆括号"], "answer": "B", "explanation": "format方法使用花括号作为占位符。"},
            {"q": "百分号格式化中s代表什么？", "options": ["数字", "字符串", "浮点数", "布尔值"], "answer": "B", "explanation": "s是字符串的占位符。"},
            {"q": "d代表什么类型？", "options": ["字符串", "整数", "浮点数", "列表"], "answer": "B", "explanation": "d是整数的占位符。"},
            {"q": "如何控制浮点数显示2位小数？", "options": ["{price:2}", "{price:.2f}", "{price:2f}", "{price:.2}"], "answer": "B", "explanation": "使用:.2f控制显示2位小数。"},
            {"q": "三种格式化方式哪个最推荐？", "options": ["百分号", "format", "f-string", "都一样"], "answer": "C", "explanation": "f-string最简洁易用，是最新推荐的方式。"},
            {"q": "f值:{x}中x是什么？", "options": ["字符串", "变量", "函数", "关键字"], "answer": "B", "explanation": "花括号中的x是变量名。"},
            {"q": "print({}+{}={}.format(1,2,3))输出什么？", "options": ["{}+{}={}", "1+2=3", "123", "format(1,2,3)"], "answer": "B", "explanation": "format按顺序替换占位符。"},
            {"q": "格式化的主要目的是？", "options": ["让代码更快", "让输出更整齐美观", "让代码更短", "让程序更大"], "answer": "B", "explanation": "格式化让输出内容整齐美观，便于阅读。"}
        ]
    },
    "2-3": {
        "chapter": "第2章 基础输出与注释",
        "title": "单行注释",
        "explanation": "注释是代码中的说明文字，不会被执行。单行注释用井号开头，井号后面的内容都是注释。注释用来解释代码的作用，帮助自己和他人理解代码。写好注释是良好编程习惯的一部分。",
        "key_points": [
            "单行注释以井号开头",
            "井号后面的整行内容都是注释",
            "注释不会被执行，只是说明文字",
            "注释用于解释代码的作用和逻辑",
            "良好的注释习惯让代码更易理解"
        ],
        "code": '''# 这是一个单行注释
print("Hello")  # 这也是注释，在代码后面

# 计算并输出结果
result = 1 + 2
print(result)  # 输出：3

# 注释可以解释复杂逻辑
# 下面计算圆的面积
radius = 5
area = 3.14 * radius ** 2''',
        "quiz": [
            {"q": "单行注释用什么符号开头？", "options": ["//", "#", "--", "/*"], "answer": "B", "explanation": "Python单行注释用#开头。"},
            {"q": "注释的内容会被执行吗？", "options": ["会执行", "不会执行", "有时执行", "只执行一半"], "answer": "B", "explanation": "注释是说明文字，不会被执行。"},
            {"q": "注释的主要作用是？", "options": ["让代码运行更快", "解释代码的作用", "增加代码长度", "美化代码"], "answer": "B", "explanation": "注释用于解释代码，帮助理解。"},
            {"q": "# print(Hello) 这行代码会输出吗？", "options": ["会输出Hello", "不会输出", "会报错", "会输出#"], "answer": "B", "explanation": "#开头的是注释，不会执行。"},
            {"q": "可以在代码后面加注释吗？", "options": ["不可以", "可以，用#开头", "只能单独一行", "必须用括号"], "answer": "B", "explanation": "可以在代码行末用#添加注释。"},
            {"q": "以下哪个是正确的注释？", "options": ["//注释", "# 注释", "/*注释*/", "--注释"], "answer": "B", "explanation": "Python使用#作为单行注释符号。"},
            {"q": "注释对程序运行有影响吗？", "options": ["会减慢速度", "没有任何影响", "会加快速度", "会改变结果"], "answer": "B", "explanation": "注释不参与执行，对运行无影响。"},
            {"q": "为什么要写注释？", "options": ["必须写", "帮助理解代码", "让代码更长", "为了美观"], "answer": "B", "explanation": "注释帮助自己和他人理解代码。"},
            {"q": "#后面可以写什么？", "options": ["只能写英文", "任意说明文字", "只能写代码", "只能写数字"], "answer": "B", "explanation": "#后面可以写任意说明文字。"},
            {"q": "好的注释应该？", "options": ["越多越好", "简洁明了，解释关键逻辑", "写满每行", "用英文写"], "answer": "B", "explanation": "好的注释应该简洁明了，解释关键逻辑。"}
        ]
    },
    "2-4": {
        "chapter": "第2章 基础输出与注释",
        "title": "多行注释",
        "explanation": "多行注释用于写较长的说明文字。Python中用三引号（单引号或双引号）包裹多行注释。多行注释常用于文件开头的说明、函数或类的详细描述等。三引号注释也可以作为多行字符串使用。",
        "key_points": [
            "多行注释用三引号包裹",
            "三引号内的所有行都是注释内容",
            "常用于文件说明和函数描述",
            "三引号也可以创建多行字符串",
            "多行注释可以跨越任意多行"
        ],
        "code": '''"""
这是一个多行注释
可以写很多行内容
用于详细说明代码
"""

\'\'\'这也是多行注释使用单引号三引号效果和双引号一样\'\'\'

print("Hello")

# 多行字符串
text = """
第一行
第二行
第三行
"""
print(text)''',
        "quiz": [
            {"q": "多行注释用什么符号？", "options": ["#", "三引号", "//", "/* */"], "answer": "B", "explanation": "Python多行注释用三引号。"},
            {"q": "三引号可以是单引号还是双引号？", "options": ["只能单引号", "只能双引号", "都可以", "都不能"], "answer": "C", "explanation": "单引号三引号和双引号三引号都可以用于多行注释。"},
            {"q": "多行注释适合用于？", "options": ["单行说明", "文件开头详细说明", "代码后面", "只能一行"], "answer": "B", "explanation": "多行注释适合详细说明，如文件描述。"},
            {"q": "三引号内的内容会执行吗？", "options": ["会执行", "不会执行", "部分执行", "只执行首行"], "answer": "B", "explanation": "三引号注释内容不会被执行。"},
            {"q": "多行注释可以写几行？", "options": ["最多3行", "任意多行", "只能2行", "只能1行"], "answer": "B", "explanation": "多行注释可以跨越任意多行。"},
            {"q": "三引号除了注释还能做什么？", "options": ["只能注释", "创建多行字符串", "执行代码", "定义函数"], "answer": "B", "explanation": "三引号也可以创建多行字符串。"},
            {"q": "以下哪个是多行注释？", "options": ["# 注释", "三引号注释", "// 注释", "-- 注释"], "answer": "B", "explanation": "三引号是Python的多行注释格式。"},
            {"q": "函数说明通常用什么注释？", "options": ["单行注释", "多行注释", "不需要注释", "特殊符号"], "answer": "B", "explanation": "函数详细说明通常用多行注释。"},
            {"q": "双引号三引号和单引号三引号效果一样吗？", "options": ["不一样", "一样", "前者更好", "后者更好"], "answer": "B", "explanation": "双引号和单引号三引号效果相同。"},
            {"q": "多行注释应该写在哪里？", "options": ["代码末尾", "文件开头或函数定义前", "任意位置", "只能末尾"], "answer": "B", "explanation": "多行注释常用于文件开头或函数定义前。"}
        ]
    }
}

def escape_html(text):
    """转义HTML特殊字符"""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def generate_section_html(section_id, data, prev_id=None, next_id=None):
    """生成小节详情页HTML"""
    
    quiz_html = ""
    for i, q in enumerate(data["quiz"], 1):
        options_html = ""
        for j, opt in enumerate(q["options"]):
            letter = chr(65 + j)  # A, B, C, D
            options_html += f'''                            <li class="option"><input type="radio" name="q{i}" id="q{i}-{letter}" value="{letter}"><label for="q{i}-{letter}">{letter}. {escape_html(opt)}</label></li>\n'''
        
        quiz_html += f'''                        <div class="question">
                            <p class="question-text">{i}. {escape_html(q["q"])}</p>
                            <ul class="options">
{options_html}                            </ul>
                            <div class="explanation" id="q{i}-explanation"></div>
                        </div>\n'''
    
    # 答案JSON
    answers_json = "{"
    for i, q in enumerate(data["quiz"], 1):
        answers_json += f'''q{i}: {{ answer: '{q["answer"]}', explanation: '{escape_html(q["explanation"])}' }}'''
        if i < len(data["quiz"]):
            answers_json += ", "
    answers_json += "}"
    
    prev_html = "上一节：无" if not prev_id else f'<a href="section-{prev_id}.html" class="prev-section-link">← 上一节</a>'
    next_html = "下一节：无" if not next_id else f'<a href="section-{next_id}.html" class="next-section-link">下一节 →</a>'
    
    key_points_html = ""
    for point in data["key_points"]:
        key_points_html += f"                            <li>{escape_html(point)}</li>\n"
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{section_id.replace("-", ".")} {data["title"]} - Python基础</title>
    <link rel="stylesheet" href="../../css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <h1>张茵茵的学习空间</h1>
            <ul class="nav-links">
                <li><a href="../../index.html">首页</a></li>
                <li><a href="../../index.html#courses">课程</a></li>
                <li><a href="../../learning-path.html">学习路径</a></li>
            </ul>
        </div>
    </nav>

    <section class="course-detail">
        <div class="container">
            <div class="course-content-wrapper section-page">
                <a href="../python-catalog.html" class="back-to-catalog">← 返回课程目录</a>
                
                <div class="section-header">
                    <span class="section-badge">{data["chapter"]}</span>
                    <h2>{section_id.replace("-", ".")} {data["title"]}</h2>
                </div>
                
                <div class="section-content">
                    <div class="explanation-box">
                        <h5 class="explanation-title">通俗讲解</h5>
                        <p class="explanation-text">{escape_html(data["explanation"])}</p>
                    </div>
                    
                    <div class="key-points-box">
                        <h5 class="key-points-title">核心知识点</h5>
                        <ul class="key-points-list">
{key_points_html}                        </ul>
                    </div>
                    
                    <div class="example-box">
                        <div class="example-header">
                            <span class="example-title">示例代码</span>
                            <button class="copy-btn" onclick="copyCode('code1')">复制</button>
                        </div>
                        <div class="example-code">
                            <pre id="code1"><code>{escape_html(data["code"])}</code></pre>
                        </div>
                    </div>
                    
                    <div class="section-progress">
                        <button class="mark-learned-btn" onclick="toggleLearned('python-{section_id}')">标记已学习</button>
                    </div>
                    
                    <div class="quiz-section">
                        <h4 class="quiz-title">本节练习</h4>
{quiz_html}                        <button class="submit-quiz-btn" onclick="submitQuiz()">提交答案</button>
                        <div class="quiz-result" id="quiz-result"></div>
                    </div>
                    
                    <div class="section-nav">
                        <span class="prev-section">{prev_html}</span>
                        <span class="next-section">{next_html}</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class="footer">
        <p>张茵茵的学习空间</p>
    </footer>

    <script>
        const SECTION_ID = 'python-{section_id}';
        const answers = {answers_json};
        
        function copyCode(id) {{
            navigator.clipboard.writeText(document.getElementById(id).textContent).then(() => alert('代码已复制！'));
        }}
        
        function toggleLearned(id) {{
            const btn = document.querySelector('.mark-learned-btn');
            const learned = JSON.parse(localStorage.getItem('python-learned') || '[]');
            if (learned.includes(id)) {{
                learned.splice(learned.indexOf(id), 1);
                btn.textContent = '标记已学习';
                btn.classList.remove('learned');
            }} else {{
                learned.push(id);
                btn.textContent = '已学习';
                btn.classList.add('learned');
            }}
            localStorage.setItem('python-learned', JSON.stringify(learned));
        }}
        
        function submitQuiz() {{
            let score = 0;
            for (let i = 1; i <= 10; i++) {{
                const selected = document.querySelector('input[name="q' + i + '"]:checked');
                const expDiv = document.getElementById('q' + i + '-explanation');
                if (selected) {{
                    const opt = selected.closest('.option');
                    if (selected.value === answers['q' + i].answer) {{
                        score++;
                        opt.classList.add('correct');
                        expDiv.innerHTML = '<p class="correct-text">正确！' + answers['q' + i].explanation + '</p>';
                        expDiv.classList.add('show', 'correct');
                    }} else {{
                        opt.classList.add('incorrect');
                        expDiv.innerHTML = '<p class="incorrect-text">错误。正确答案是 ' + answers['q' + i].answer + '。' + answers['q' + i].explanation + '</p>';
                        expDiv.classList.add('show', 'incorrect');
                    }}
                }}
            }}
            const result = document.getElementById('quiz-result');
            result.innerHTML = '<h4>答题结果</h4><p class="quiz-score">' + score + ' / 10</p><p>' + (score >= 8 ? '优秀！' : score >= 6 ? '良好！' : '继续努力！') + '</p>';
            result.classList.add('show');
        }}
        
        document.addEventListener('DOMContentLoaded', function() {{
            const learned = JSON.parse(localStorage.getItem('python-learned') || '[]');
            if (learned.includes(SECTION_ID)) {{
                const btn = document.querySelector('.mark-learned-btn');
                btn.textContent = '已学习';
                btn.classList.add('learned');
            }}
        }});
    </script>
</body>
</html>'''
    
    return html

def main():
    # 创建目录
    os.makedirs("/workspace/courses/python", exist_ok=True)
    
    # 获取所有小节ID并排序
    section_ids = sorted(SECTIONS.keys(), key=lambda x: (int(x.split("-")[0]), int(x.split("-")[1])))
    
    # 生成所有小节页面
    for i, sid in enumerate(section_ids):
        prev_id = section_ids[i-1] if i > 0 else None
        next_id = section_ids[i+1] if i < len(section_ids)-1 else None
        
        html = generate_section_html(sid, SECTIONS[sid], prev_id, next_id)
        filepath = f"/workspace/courses/python/section-{sid}.html"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"生成: {filepath}")
    
    print(f"\n完成！共生成 {len(section_ids)} 个小节页面")

if __name__ == "__main__":
    main()