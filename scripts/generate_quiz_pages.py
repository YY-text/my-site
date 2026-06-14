#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""独立的 quiz 页面生成脚本 - 避免 f-string 与 JavaScript 花括号冲突"""

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from generate_all_sections import COURSES


def make_questions(section_title, chapter_title, knowledge_points):
    """基于知识点生成10道题"""
    if knowledge_points:
        qs = [
            {"q": "关于" + section_title + "，以下说法正确的是？",
             "options": [knowledge_points[0] if len(knowledge_points) > 0 else "第一个知识点",
                         "只了解理论即可", "不需要实践", "可以随便学习"],
             "answer": "A",
             "explanation": knowledge_points[0] if len(knowledge_points) > 0 else "这是关于" + section_title + "的基本概念。"},
            {"q": section_title + "在实际工作中的应用场景包括？",
             "options": ["理论学习", "考试做题",
                         knowledge_points[-1] if len(knowledge_points) > 1 else "实践应用",
                         "以上都不对"],
             "answer": "C",
             "explanation": knowledge_points[-1] if len(knowledge_points) > 1 else section_title + "在实际工作中有重要应用。"},
            {"q": "学习" + section_title + "的最佳方法是？",
             "options": ["只看不练", "边学边练", "只练不看", "临时抱佛脚"],
             "answer": "B", "explanation": "边学边练是最好的学习方法，可以加深理解和记忆。"},
            {"q": section_title + "需要注意的事项是？",
             "options": ["不需要注意",
                         knowledge_points[1] if len(knowledge_points) > 1 else "理论与实践结合",
                         "随便学习就行", "只看不做"],
             "answer": "B",
             "explanation": knowledge_points[1] if len(knowledge_points) > 1 else "学习" + section_title + "需要注意理论与实践结合。"},
            {"q": "掌握" + section_title + "后可以？",
             "options": ["解决基础问题", "独立完成相关任务", "进行深入研究", "以上全部"],
             "answer": "D", "explanation": "掌握" + section_title + "后可以进行多种应用和发展。"},
            {"q": section_title + "与其他知识的关系是？",
             "options": ["相互独立",
                         knowledge_points[2] if len(knowledge_points) > 2 else "相互关联",
                         "毫不相关", "完全相同"],
             "answer": "B",
             "explanation": knowledge_points[2] if len(knowledge_points) > 2 else section_title + "与其他知识相互关联。"},
            {"q": "评估" + section_title + "掌握程度的方法是？",
             "options": ["做练习题", "完成实际任务", "A和B都正确", "无法评估"],
             "answer": "C", "explanation": "可以通过做题和实践来评估" + section_title + "的掌握程度。"},
            {"q": "学习" + section_title + "的难点在于？",
             "options": ["概念理解", "方法运用",
                         knowledge_points[3] if len(knowledge_points) > 3 else "综合应用",
                         "以上都不是"],
             "answer": "C",
             "explanation": knowledge_points[3] if len(knowledge_points) > 3 else section_title + "的难点主要在于综合应用。"},
            {"q": "关于" + section_title + "的学习建议是？",
             "options": ["坚持练习", "多思考多总结", "A和B都采纳", "随便学学就行"],
             "answer": "C", "explanation": "学习" + section_title + "建议坚持练习并多思考多总结。"},
            {"q": section_title + "的核心价值在于？",
             "options": ["考试拿高分", "解决实际问题", "应付作业", "没有实际作用"],
             "answer": "B", "explanation": section_title + "的核心价值在于解决实际问题，这也是学习的真正目的。"}
        ]
        return qs
    else:
        qs = []
        template_qs = [
            ("关于" + section_title + "的基本概念，以下哪个说法正确？",
             [section_title + "是" + chapter_title + "中的重要内容", "不需要理解概念", "可以随便学习", "以上都不对"],
             "A", section_title + "是" + chapter_title + "中的重要内容，需要认真学习掌握。"),
            (section_title + "的主要特点是？",
             ["简单易懂", "实用性强", "应用广泛", "以上都是"],
             "D", section_title + "具有简单易懂、实用性强、应用广泛的特点。"),
            ("学习" + section_title + "的正确方法是？",
             ["理论学习", "实践操作", "理论与实践结合", "随便看看"],
             "C", "学习" + section_title + "应该理论与实践结合，才能真正掌握。"),
            (section_title + "在实际应用中的作用是？",
             ["辅助理解", "解决问题", "提高效率", "以上都是"],
             "D", section_title + "在实际应用中可以帮助理解、解决问题、提高效率。"),
            ("掌握" + section_title + "的关键在于？",
             ["死记硬背", "理解与应用", "猜题", "不需要掌握"],
             "B", "掌握" + section_title + "的关键在于理解与应用。"),
            (section_title + "与" + chapter_title + "的关系是？",
             ["没有关系", "重要组成部分", "独立存在", "可以替代"],
             "B", section_title + "是" + chapter_title + "的重要组成部分。"),
            ("下列关于" + section_title + "的说法，错误的是？",
             ["需要认真学习", "可以跳过不学", "注重理解", "需要实践"],
             "B", section_title + "是重要的知识点，不能跳过不学。"),
            ("学习" + section_title + "时应该重点关注？",
             ["核心概念", "实际应用", "常见问题", "以上都是"],
             "D", "学习" + section_title + "时应该重点关注核心概念、实际应用和常见问题。"),
            (section_title + "的学习目标是？",
             ["应付考试", "理解并应用", "随便学学", "凑够学时"],
             "B", section_title + "的学习目标是理解并应用。"),
            ("关于" + section_title + "，以下说法正确的是？",
             ["只需要了解", "需要深入理解", "不需要实践", "可以跳过"],
             "B", section_title + "需要深入理解才能真正掌握。")
        ]
        for t in template_qs:
            qs.append({"q": t[0], "options": t[1], "answer": t[2], "explanation": t[3]})
        return qs


def make_questions_html(questions):
    """生成题目 HTML - 不使用 f-string，避免花括号冲突"""
    out = []
    for i, q in enumerate(questions, 1):
        out.append("                        <div class=\"question\">")
        out.append("                            <p class=\"question-text\">" + str(i) + ". " + q["q"] + "</p>")
        out.append("                            <ul class=\"options\">")
        letters = ["A", "B", "C", "D"]
        for li, opt in zip(letters, q["options"]):
            out.append("                                <li class=\"option\"><input type=\"radio\" name=\"q" + str(i) + "\" id=\"q" + str(i) + "-" + li.lower() + "\" value=\"" + li + "\"><label for=\"q" + str(i) + "-" + li.lower() + "\">" + li + ". " + opt + "</label></li>")
        out.append("                            </ul>")
        out.append("                            <div class=\"explanation\" id=\"q" + str(i) + "-explanation\"></div>")
        out.append("                        </div>")
    return "\n".join(out)


def make_sidebar_html(course_info, section_id):
    """生成侧边栏 - 用普通字符串拼接"""
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


def make_quiz_html(course_key, course_info, chapter, section):
    """用普通字符串拼接构造 quiz 页面 HTML"""
    section_id = course_key + "-section-" + section['id']
    section_title = section['title']
    chapter_title = chapter['title']
    course_name = course_info['name']
    course_icon = course_info['icon']
    knowledge_points = section.get('knowledge', [])

    questions = make_questions(section_title, chapter_title, knowledge_points)
    questions_html = make_questions_html(questions)
    sidebar_html = make_sidebar_html(course_info, section['id'])

    # 构造答案 JSON
    correct_answers = {}
    explanations = {}
    for i, q in enumerate(questions, 1):
        correct_answers["q" + str(i)] = q["answer"]
        explanations["q" + str(i)] = q["explanation"]

    # 构造 HTML 主体（逐行拼接，完全不用 f-string）
    html = ""
    html += "<!DOCTYPE html>\n"
    html += "<html lang=\"zh-CN\">\n"
    html += "<head>\n"
    html += "    <meta charset=\"UTF-8\">\n"
    html += "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
    html += "    <title>" + section_title + " - 练习题 | " + course_name + "</title>\n"
    html += "    <link rel=\"stylesheet\" href=\"../../css/styles.css\">\n"
    html += "    <style>\n"
    html += "        .quiz-result { margin-top: 2rem; padding: 1.5rem; border-radius: 12px; background: linear-gradient(135deg, #FFFACD 0%, #FFEFD5 100%); border: 2px solid #DAA520; display: none; }\n"
    html += "        .quiz-result.show { display: block; }\n"
    html += "        .quiz-result h4 { font-size: 1.3rem; color: #8B4513; margin-bottom: 0.5rem; }\n"
    html += "        .quiz-score { font-size: 2.5rem; font-weight: bold; color: #CD853F; }\n"
    html += "    </style>\n"
    html += "</head>\n"
    html += "<body>\n"
    html += "    <nav class=\"navbar\">\n"
    html += "        <div class=\"container\">\n"
    html += "            <h1>张茵茵的学习空间</h1>\n"
    html += "            <ul class=\"nav-links\">\n"
    html += "                <li><a href=\"../../index.html\">首页</a></li>\n"
    html += "                <li><a href=\"../../index.html#courses\">课程</a></li>\n"
    html += "                <li><a href=\"../../learning-path.html\">学习路径</a></li>\n"
    html += "            </ul>\n"
    html += "        </div>\n"
    html += "    </nav>\n"
    html += "    <div class=\"sidebar-toggle\" onclick=\"toggleSidebar()\"></div>\n"
    html += "    <div class=\"sidebar-overlay\" onclick=\"toggleSidebar()\"></div>\n"
    html += "    <aside class=\"sidebar\">\n"
    html += "        <div class=\"sidebar-header\">\n"
    html += "            <h4>" + course_icon + " " + course_name + " 列表</h4>\n"
    html += "        </div>\n"
    html += "        " + sidebar_html + "\n"
    html += "    </aside>\n"
    html += "    <section class=\"course-content\">\n"
    html += "        <div class=\"container\">\n"
    html += "            <div class=\"content-wrapper\">\n"
    html += "                <div class=\"content-main\">\n"
    html += "                    <div class=\"breadcrumb-nav\">\n"
    html += "                        <a href=\"section-" + section['id'] + ".html\">← 返回小节</a>\n"
    html += "                    </div>\n"
    html += "                    <div class=\"section-page\">\n"
    html += "                        <h2 class=\"section-main-title\">📝 " + section_title + " - 练习题</h2>\n"
    html += "                        <div class=\"section-sub-title\">\n"
    html += "                            <h3>第" + str(chapter['num']) + "章 " + chapter_title + "</h3>\n"
    html += "                        </div>\n"
    html += "                        <div class=\"knowledge-section\">\n"
    html += questions_html + "\n"
    html += "                            <div class=\"quiz-actions\">\n"
    html += "                                <button class=\"submit-quiz-btn\" onclick=\"submitQuiz()\">提交答案</button>\n"
    html += "                                <button class=\"reset-quiz-btn\" onclick=\"resetQuiz()\">重置答案</button>\n"
    html += "                            </div>\n"
    html += "                            <div class=\"quiz-result\" id=\"quizResult\">\n"
    html += "                                <h4>答题结果</h4>\n"
    html += "                                <div class=\"quiz-score\" id=\"scoreDisplay\">0/10</div>\n"
    html += "                                <p id=\"scoreComment\">提交答案后查看详细解析</p>\n"
    html += "                            </div>\n"
    html += "                        </div>\n"
    html += "                        <div class=\"section-navigation\">\n"
    html += "                            <a href=\"section-" + section['id'] + ".html\" class=\"nav-btn prev-btn\">← 返回小节详情</a>\n"
    html += "                        </div>\n"
    html += "                    </div>\n"
    html += "                </div>\n"
    html += "            </div>\n"
    html += "        </div>\n"
    html += "    </section>\n"
    html += "    <footer class=\"footer\"><p>张茵茵的学习空间</p></footer>\n"

    # JavaScript 部分 - 逐字符写出来，确保与 Python 花括号无冲突
    import json
    html += "    <script>\n"
    html += "        const sectionId = \"" + section_id + "\";\n"
    html += "        const correctAnswers = " + json.dumps(correct_answers, ensure_ascii=False) + ";\n"
    html += "        const explanations = " + json.dumps(explanations, ensure_ascii=False) + ";\n"
    # JS 代码用普通字符串（单引号内的大括号不会被 Python 解析）
    js_code = r'''
        function submitQuiz() {
            let score = 0;
            for (let i = 1; i <= 10; i++) {
                const selected = document.querySelector('input[name="q' + i + '"]:checked');
                const explanationEl = document.getElementById('q' + i + '-explanation');
                if (selected) {
                    const selectedValue = selected.value;
                    const correctValue = correctAnswers['q' + i];
                    if (selectedValue === correctValue) {
                        score++;
                        explanationEl.innerHTML = '<span class="correct">回答正确！</span> ' + explanations['q' + i];
                        selected.parentElement.classList.add('correct');
                    } else {
                        explanationEl.innerHTML = '<span class="wrong">回答错误！</span> ' + explanations['q' + i];
                        selected.parentElement.classList.add('incorrect');
                        const correctOption = document.querySelector('input[name="q' + i + '"][value="' + correctValue + '"]');
                        if (correctOption) correctOption.parentElement.classList.add('correct');
                    }
                } else {
                    explanationEl.innerHTML = '<span style="color:#999;">未作答</span> - ' + explanations['q' + i];
                }
                explanationEl.classList.add('show');
            }
            document.getElementById('scoreDisplay').textContent = score + '/10';
            document.getElementById('quizResult').classList.add('show');
            var quizResult = { sectionId: sectionId, score: score, total: 10, answers: {} };
            for (let i = 1; i <= 10; i++) {
                const selected = document.querySelector('input[name="q' + i + '"]:checked');
                quizResult.answers['q' + i] = selected ? selected.value : null;
            }
            localStorage.setItem('quiz-' + sectionId, JSON.stringify(quizResult));
            document.getElementById('quizResult').scrollIntoView({ behavior: 'smooth', block: 'center' });
        }

        function resetQuiz() {
            for (let i = 1; i <= 10; i++) {
                const options = document.querySelectorAll('input[name="q' + i + '"]');
                options.forEach(opt => {
                    opt.checked = false;
                    opt.parentElement.classList.remove('correct', 'incorrect');
                });
                const explanationEl = document.getElementById('q' + i + '-explanation');
                explanationEl.classList.remove('show');
                explanationEl.innerHTML = '';
            }
            document.getElementById('quizResult').classList.remove('show');
            document.getElementById('scoreDisplay').textContent = '0/10';
        }

        function toggleSidebar() {
            document.body.classList.toggle('sidebar-open');
        }

        document.addEventListener('DOMContentLoaded', function() {
            const saved = localStorage.getItem('quiz-' + sectionId);
            if (saved) {
                const quizResult = JSON.parse(saved);
                for (let i = 1; i <= 10; i++) {
                    const answer = quizResult.answers['q' + i];
                    if (answer) {
                        const radio = document.querySelector('input[name="q' + i + '"][value="' + answer + '"]');
                        if (radio) radio.checked = true;
                    }
                }
                document.getElementById('scoreDisplay').textContent = quizResult.score + '/10';
                document.getElementById('quizResult').classList.add('show');
            }
            if (window.innerWidth < 768) {
                const sidebarLinks = document.querySelectorAll('.sidebar a');
                sidebarLinks.forEach(link => {
                    link.addEventListener('click', () => {
                        document.body.classList.remove('sidebar-open');
                    });
                });
            }
        });
'''
    html += js_code
    html += "    </script>\n"
    html += "</body>\n"
    html += "</html>"

    return html


def main():
    base_path = "/workspace/courses"
    total_count = 0

    for course_key, course_info in COURSES.items():
        course_dir = os.path.join(base_path, course_key)
        os.makedirs(course_dir, exist_ok=True)

        # 获取所有章节
        for chapter in course_info['chapters']:
            for section in chapter['sections']:
                html = make_quiz_html(course_key, course_info, chapter, section)
                filename = "quiz-" + section['id'] + ".html"
                filepath = os.path.join(course_dir, filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                total_count += 1
                print("生成: " + course_key + "/" + filename)

    print("\n完成！共生成 " + str(total_count) + " 个 quiz 页面！")


if __name__ == "__main__":
    main()
