#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import sys

def get_version_from_toml(toml_path):
    """从 pack.toml 文件中提取版本号"""
    try:
        with open(toml_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('version ='):
                    match = re.search(r'version\s*=\s*"([^"]+)"', line)
                    if match:
                        return match.group(1)
        print(f"错误：在 {toml_path} 中找不到版本号")
        return None
    except Exception as e:
        print(f"读取 {toml_path} 时出错：{e}")
        return None

def extract_changelog(changelog_path, version):
    """提取指定版本的变更日志部分及其页脚链接"""
    try:
        with open(changelog_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取当前版本的主要内容部分
        # 当遇到 <details> 标签或下一个版本标题时停止
        pattern = rf'## \[{re.escape(version)}\][^\n]*\n(.*?)(?=\n<details>|\n## \[|\Z)'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            print(f"错误：找不到版本 {version} 的变更日志")
            return None
            
        changelog_content = match.group(0).strip()
        
        # 查找此版本的页脚链接
        footer_pattern = rf'\[{re.escape(version)}\]: [^\n]+'
        footer_match = re.search(footer_pattern, content)
        
        if footer_match:
            # 返回内容和页脚链接
            return changelog_content + "\n\n" + footer_match.group(0)
        else:
            print(f"警告：找不到版本 {version} 的页脚链接")
            return changelog_content
            
    except Exception as e:
        print(f"读取 {changelog_path} 时出错：{e}")
        return None

def main():
    # 确定仓库根目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(script_dir) == 'scripts' and os.path.basename(os.path.dirname(script_dir)) == '.github':
        # 脚本从其原始位置运行
        repo_root = os.path.dirname(os.path.dirname(script_dir))
    else:
        # 假设我们已经在仓库根目录
        repo_root = os.getcwd()
    
    # 定义文件路径
    toml_path = os.path.join(repo_root, 'pack', 'pack.toml')
    changelog_path = os.path.join(repo_root, 'CHANGELOG.md')
    output_path = os.path.join(repo_root, 'CHANGELOG_NOW.md')
    
    # 确保输入文件存在
    if not os.path.exists(toml_path):
        print(f"错误：{toml_path} 不存在")
        return 1
    if not os.path.exists(changelog_path):
        print(f"错误：{changelog_path} 不存在")
        return 1
    
    # 获取当前版本
    version = get_version_from_toml(toml_path)
    if not version:
        return 1
    
    # 提取当前版本的变更日志
    changelog = extract_changelog(changelog_path, version)
    if not changelog:
        return 1
    
    # 写入输出文件
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(changelog)
        print(f"成功将版本 {version} 的变更日志提取到 CHANGELOG_NOW.md")
        return 0
    except Exception as e:
        print(f"写入 {output_path} 时出错：{e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())