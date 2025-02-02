import argparse
import os
from pan123 import pan123openAPI

def main():
    parser = argparse.ArgumentParser(description="上传文件到123云盘")
    parser.add_argument("--client_id", required=True, help="开发者客户端ID")
    parser.add_argument("--client_secret", required=True, help="开发者客户端密钥")
    parser.add_argument("--file", required=True, help="本地文件路径")
    parser.add_argument("--upload_name", help="上传后的文件名（默认使用本地文件名）")
    parser.add_argument("--parent_id", type=int, default=0, help="目标文件夹ID（默认根目录）")
    
    args = parser.parse_args()

    # 自动获取上传文件名
    if not args.upload_name:
        args.upload_name = os.path.basename(args.file)

    # 初始化API并获取access_token
    pan = pan123openAPI(args.client_id, args.client_secret)
    token_res = pan.refresh_access_token()
    if not token_res.success:
        print(f"认证失败: {token_res.message}")
        return

    # 定义上传进度回调
    def upload_callback(step, res, progress):
        if step == 2:  # 仅显示分片上传进度
            print(f"\r上传进度: {progress['uploaded_size']/1024/1024:.2f}MB / {progress['total_size']/1024/1024:.2f}MB", end="")
        return True

    # 执行上传
    try:
        file_id = pan.file.upload(
            filename_or_io=args.file,
            upload_name=args.upload_name,
            parentFileID=args.parent_id,
            callback=upload_callback
        )
        print(f"\n上传成功！文件ID: {file_id}")
    except Exception as e:
        print(f"\n上传失败: {str(e)}")

if __name__ == "__main__":
    main()