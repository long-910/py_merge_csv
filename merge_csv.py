#!/usr/bin/env python3
import argparse
import pandas as pd
import sys

def merge_csv_files(file1, file2, key, output_file='output.csv'):
    try:
        # CSVファイルを読み込む
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)

        # キーが両方のデータフレームに存在するか確認
        if key not in df1.columns or key not in df2.columns:
            print(f"エラー: 指定されたキー '{key}' が両方のCSVファイルに存在しません。")
            sys.exit(1)

        # データフレームをマージ
        merged_df = pd.merge(df1, df2, on=key, how='outer')

        # 結果をCSVファイルに出力
        merged_df.to_csv(output_file, index=False)
        print(f"マージが完了しました。出力ファイル: {output_file}")

    except FileNotFoundError as e:
        print(f"エラー: ファイルが見つかりません - {e}")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print("エラー: 空のCSVファイルが指定されています。")
        sys.exit(1)
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='2つのCSVファイルをマージします。')
    parser.add_argument('file1', help='1つ目のCSVファイルのパス')
    parser.add_argument('file2', help='2つ目のCSVファイルのパス')
    parser.add_argument('key', help='マージに使用するキー（列名）')
    parser.add_argument('-o', '--output', default='output.csv',
                      help='出力ファイル名（デフォルト: output.csv）')

    args = parser.parse_args()
    merge_csv_files(args.file1, args.file2, args.key, args.output)

if __name__ == '__main__':
    main() 