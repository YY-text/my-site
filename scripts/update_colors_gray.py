#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将全局CSS颜色改为灰白色系
"""
import re

css_file = '/workspace/css/styles.css'

with open(css_file, 'r', encoding='utf-8') as f:
    content = f.read()

# === 灰白色系配色方案 ===
# 主背景：#D4D4D4 中灰
# 二级背景：#C0C0C0 深银灰
# 按钮/三级：#A0A0A0 冷灰
# 边框：#6B6B6B 深灰
# 强调色/按钮主色：#4A4A4A 深炭灰
# 最深强调：#2A2A2A 近黑灰
# 文字：#1A1A1A 近黑
# 页脚背景：#3A3A3A 深灰
# 页脚文字：#E8E8E8 浅灰白

# 替换映射：从现有深粉色 → 灰白色系
color_replacements = [
    # === 背景色替换 ===
    # 深玫瑰粉 #C98FA0 → 中灰
    ('#C98FA0', '#D4D4D4'),
    # 深粉棕 #B88794 → 深银灰
    ('#B88794', '#C0C0C0'),
    # 深紫棕 #A07584 → 冷灰
    ('#A07584', '#A0A0A0'),

    # === 边框色替换 ===
    # 深红棕 #8B5A6B → 深灰
    ('#8B5A6B', '#6B6B6B'),

    # === 强调色替换 ===
    # 深玫瑰红 #8B3A50 → 深炭灰
    ('#8B3A50', '#4A4A4A'),
    # 更深玫瑰 #6B2A40 → 近黑灰
    ('#6B2A40', '#2A2A2A'),

    # === 绿色系 → 灰绿色 ===
    # 深黄绿 #6B8B4A → 中灰绿
    ('#6B8B4A', '#7A8A7A'),
    # 深绿 #5A7A3A → 深灰绿
    ('#5A7A3A', '#5A6A5A'),
    # 更深绿 #3A5A2A → 更深灰绿
    ('#3A5A2A', '#3A4A3A'),

    # === 文字色（保持深色，可能已是#2D1A0F） ===
    # 深棕黑 #2D1A0F → 近黑
    ('#2D1A0F', '#1A1A1A'),

    # === 页脚浅色文字 #F5E0D0 → 浅灰白 ===
    ('#F5E0D0', '#E8E8E8'),

    # === 页脚背景 #6B4A55 → 深灰 ===
    ('#6B4A55', '#3A3A3A'),
]

# 应用替换
for old_color, new_color in color_replacements:
    pattern = re.compile(re.escape(old_color), re.IGNORECASE)
    content = pattern.sub(new_color, content)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ CSS全局颜色已改为灰白色系")
print(f"   主背景: #D4D4D4 (中灰)")
print(f"   二级背景: #C0C0C0 (深银灰)")
print(f"   按钮背景: #A0A0A0 (冷灰)")
print(f"   边框: #6B6B6B (深灰)")
print(f"   强调按钮: #4A4A4A (深炭灰)")
print(f"   文字: #1A1A1A (近黑)")
print(f"   页脚: #3A3A3A (深灰) + #E8E8E8 (浅灰白文字)")
