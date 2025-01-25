import json
import os
import re

def clean_filename(name):
    # 替换特殊字符
    replacements = {
        '&': 'And',
        '+': 'Plus',
        '@': 'At',
        '!': '',
        '?': '',
        "'": '',
        '"': '',
        '#': '',
        '$': '',
        '%': '',
        '^': '',
        '*': '',
        '=': '',
        '|': '',
        '\\': '',
        '/': '',
        ':': '',
        ';': '',
        ',': '',
        '<': '',
        '>': '',
        '(': '',
        ')': '',
        '[': '',
        ']': '',
        '{': '',
        '}': '',
        ' ': '_',
        'å':'a'
    }
    
    result = name
    for char, replacement in replacements.items():
        result = result.replace(char, replacement)
    
    # 移除任何其他非字母数字字符
    result = re.sub(r'[^\w\-.]', '', result)
    
    return result

def extract_mod_name_and_translation(title):
    # 提取[]中的内容和中文翻译
    match = re.search(r'\[(.*?)\](.*?)$', title)
    if match:
        mod_name = match.group(1)
        translation = match.group(2).strip()
        return mod_name, translation if translation else mod_name
    return title, title

def create_json_content(name, url, category):
    return {
        "name": name,
        "icon": "minecraft:writable_book",
        "category": f"patchouli:{category}",
        "pages": [
            {
                "type": "patchouli:link",
                "text": "暂未完善内容，请点击下面的按钮查看详情！",
                "url": url,
                "link_text": "在浏览器中查看"
            }
        ]
    }

def process_mod_category(items, current_category, expected_files):
    # 处理模组类别
    if not current_category:
        return
        
    for item in items:
        if item['type'] == 'link':
            mod_name, display_name = extract_mod_name_and_translation(item['title'])
            if mod_name:
                # 创建文件名
                filename = f"{clean_filename(mod_name)}.json"
                filepath = os.path.join(current_category, filename)
                
                # 将此文件路径添加到预期文件列表中
                expected_files.add(filepath)
                
                # 检查文件是否已存在
                if os.path.exists(filepath):
                    print(f"Skipped existing: {filepath}")
                    continue
                
                # 创建 JSON 文件
                json_content = create_json_content(display_name, item['url'], current_category)
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(json_content, f, ensure_ascii=False, indent=4)
                print(f"Created: {filepath}")
        
        elif item['type'] == 'folder' and 'children' in item:
            process_mod_category(item['children'], current_category, expected_files)

def process_special_category(items, category, expected_files):
    # 处理资源包、数据包和光影包类别
    for item in items:
        if item['type'] == 'link':
            name = item['title']
            if '[' in name and ']' in name:
                name = re.search(r'\[(.*?)\]', name).group(1)
            
            # 创建文件名
            filename = f"{clean_filename(name)}.json"
            filepath = os.path.join(category, filename)
            
            # 将此文件路径添加到预期文件列表中
            expected_files.add(filepath)
            
            # 检查文件是否已存在
            if os.path.exists(filepath):
                print(f"Skipped existing: {filepath}")
                continue
            
            # 创建 JSON 文件
            json_content = create_json_content(name, item['url'], category)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(json_content, f, ensure_ascii=False, indent=4)
            print(f"Created: {filepath}")

def process_bookmarks(data):
    # 创建所有必要的目录
    categories = [
        'adventure', 'agriculture', 'assist', 'custom', 'datapacks',
        'decoration', 'lib', 'magic', 'resourcepacks', 'shaderpacks',
        'technology', 'utility'
    ]
    for folder in categories:
        os.makedirs(folder, exist_ok=True)
    
    # 用于存储所有预期生成的文件路径
    expected_files = set()
    
    # 递归查找并处理内容
    def process_folder(items):
        for item in items:
            if item['type'] == 'folder':
                title = item.get('title', '')
                
                # 处理模组类别
                match = re.match(r'([a-zA-Z]+)\s*[\|｜]', title)
                if match and 'children' in item:
                    category = match.group(1).lower()
                    process_mod_category(item['children'], category, expected_files)
                
                # 处理特殊类别
                if title == '资源包' and 'children' in item:
                    process_special_category(item['children'], 'resourcepacks', expected_files)
                elif title == '数据包' and 'children' in item:
                    process_special_category(item['children'], 'datapacks', expected_files)
                elif title == '光影包' and 'children' in item:
                    process_special_category(item['children'], 'shaderpacks', expected_files)
                
                # 继续递归处理
                if 'children' in item:
                    process_folder(item['children'])
    
    # 开始处理数据
    process_folder(data)
    
    # 检查并删除多余的文件
    for category in categories:
        if os.path.exists(category):
            for file in os.listdir(category):
                filepath = os.path.join(category, file)
                if filepath not in expected_files and file.endswith('.json'):
                    os.remove(filepath)
                    print(f"Removed unused: {filepath}")

# 读取输入的JSON数据
with open('bookmark.json', 'r', encoding='utf-8') as f:
    input_data = json.load(f)

# 处理书签数据
process_bookmarks(input_data)