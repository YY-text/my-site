#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将全局CSS颜色改为清新绿色系（有生机）
"""
import re

css_file = '/workspace/css/styles.css'

with open(css_file, 'r', encoding='utf-8') as f:
    content = f.read()

# === 清新绿色系配色方案 ===
# 主背景：#C8E8C8 新鲜薄荷绿
# 二级背景：#8FC98F 青草绿
# 按钮/三级：#5A9A5A 绿叶绿
# 边框：#3A7A3A 森林绿
# 强调色：#1A4A1A 深森林绿
# 最深强调：#0A2A0A 墨绿
# 文字：#1A2A1A 深墨绿黑
# 页脚背景：#2A4A2A 深森林
# 页脚文字：#E8F0E8 浅薄荷白

# 替换映射：从灰白色 → 清新绿色
color_replacements = [
    # === 背景色替换 ===
    # 中灰 #D4D4D4 → 薄荷绿
    ('#D4D4D4', '#C8E8C8'),
    # 深银灰 #C0C0C0 → 青草绿
    ('#C0C0C0', '#8FC98F'),
    # 冷灰 #A0A0A0 → 绿叶绿
    ('#A0A0A0', '#5A9A5A'),

    # === 边框色替换 ===
    # 深灰 #6B6B6B → 森林绿
    ('#6B6B6B', '#3A7A3A'),

    # === 强调色替换 ===
    # 深炭灰 #4A4A4A → 深森林绿
    ('#4A4A4A', '#1A4A1A'),
    # 近黑灰 #2A2A2A → 墨绿
    ('#2A2A2A', '#0A2A0A'),

    # === 灰绿色系（若存在）→ 纯绿色 ===
    # 中灰绿 #7A8A7A → 深草绿
    ('#7A8A7A', '#4A8A4A'),
    # 深灰绿 #5A6A5A → 森林绿
    ('#5A6A5A', '#2A6A2A'),
    # 更深灰绿 #3A4A3A → 深森林绿
    ('#3A4A3A', '#1A3A1A'),

    # === 文字色 ===
    # 近黑 #1A1A1A → 深墨绿
    ('#1A1A1A', '#1A2A1A'),

    # === 页脚 ===
    # 浅灰白 #E8E8E8 → 浅薄荷白
    ('#E8E8E8', '#E8F0E8'),
    # 深灰 #3A3A3A → 深森林
    ('#3A3A3A', '#2A4A2A'),

    # === 额外：确保白色卡片内边框等也协调 ===
    # 让一些特殊的深灰也替换
    ('#303030', '#1A3A1A'),
]

# 应用替换
for old_color, new_color in color_replacements:
    pattern = re.compile(re.escape(old_color), re.IGNORECASE)
    content = pattern.sub(new_color, content)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ CSS全局颜色已改为清新绿色系")
print(f"   主背景: #C8E8C8 (新鲜薄荷绿)")
print(f"   二级背景: #8FC98F (青草绿)")
print(f"   按钮背景: #5A9A5A (绿叶绿)")
print(f"   边框: #3A7A3A (森林绿)")
print(f"   强调按钮: #1A4A1A (深森林绿)")
print(f"   文字: #1A2A1A (深墨绿)")
print(f"   页脚: #2A4A2A (深森林) + #E8F0E8 (浅薄荷白)")
