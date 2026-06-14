#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修改CSS颜色为深色纯色配色
"""
import re

css_file = '/workspace/css/styles.css'

with open(css_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 定义颜色替换映射
# 原则：所有浅粉色→更深，所有棕色边框→深粉棕
color_replacements = [
    # === 背景色替换 ===
    # 浅粉色背景 → 深玫瑰粉
    ('#F5DCE4', '#C98FA0'),
    # 中粉色 → 更深粉棕
    ('#E8C5D0', '#B88794'),
    # 深粉色 → 保持较深
    ('#DDB4C0', '#A07584'),

    # === 边框色替换 ===
    # 深粉色边框 → 更深
    ('#E8A0B0', '#8B5A6B'),

    # === 棕色系边框/装饰 → 深粉棕 ===
    ('#DEB887', '#8B5A6B'),
    ('#CD853F', '#8B5A6B'),
    ('#FFB347', '#8B5A6B'),
    ('#DAA520', '#8B5A6B'),

    # === 文字颜色替换 - 更深更易读 ===
    ('#5D3A1A', '#2D1A0F'),
    ('#5D4E37', '#2D1A0F'),
    ('#4A5568', '#2D1A0F'),
    ('#1a1a1a', '#2D1A0F'),

    # === 强调色 - 更深更清晰 ===
    ('#D4697A', '#8B3A50'),
    ('#FF6B6B', '#8B3A50'),
    ('#FF7E5F', '#8B3A50'),

    # === 按钮/特殊颜色 ===
    ('#3182CE', '#8B3A50'),    # 蓝色按钮 → 深玫瑰
    ('#2C5282', '#6B2A40'),    # 深蓝悬停 → 更深玫瑰
    ('#48BB78', '#6B8B4A'),    # 绿色 → 深黄绿
    ('#38A169', '#5A7A3A'),    # 深绿
    ('#276749', '#3A5A2A'),    # 更深绿
    ('#4CAF50', '#6B8B4A'),    # 绿色正确
    ('#E53935', '#8B3A50'),    # 红色错误
    ('#C62828', '#6B2A40'),    # 深红
    ('#228B22', '#5A7A3A'),    # 绿色文字
    ('#2E7D32', '#3A5A2A'),    # 深绿文字

    # === 白色装饰元素 ===
    ('#FFD6E0', '#E8C5D0'),    # 粉色装饰
    ('#FFD700', '#8B5A6B'),    # 金色 → 深粉棕
]

# 应用替换（不分大小写匹配HEX）
for old_color, new_color in color_replacements:
    # 匹配精确颜色值（不区分大小写）
    pattern = re.compile(re.escape(old_color), re.IGNORECASE)
    content = pattern.sub(new_color, content)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ CSS颜色已更新为深色纯色配色")
print(f"   页面主背景: #C98FA0 (深玫瑰粉)")
print(f"   二级背景: #B88794 (深粉棕)")
print(f"   边框色: #8B5A6B (深红棕)")
print(f"   文字色: #2D1A0F (深棕黑)")
print(f"   强调色: #8B3A50 (深玫瑰)")
