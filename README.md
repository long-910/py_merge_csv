# CSVマージツール

2つのCSVファイルを指定されたキーでマージするPythonツールです。

## 目次
- [必要条件](#必要条件)
- [インストール手順](#インストール手順)
- [使用方法](#使用方法)
- [使用例](#使用例)
- [注意事項](#注意事項)

## 必要条件

- Python 3.6以上
- pandas

## インストール手順

### 1. Pythonのインストール

#### Windows
1. [Python公式サイト](https://www.python.org/downloads/)から最新版をダウンロード
2. インストーラーを実行
3. 「Add Python to PATH」にチェックを入れてインストール
4. コマンドプロンプトで以下を実行して確認：
```bash
python --version
```

#### macOS
1. [Homebrew](https://brew.sh/)をインストール（未インストールの場合）
2. ターミナルで以下を実行：
```bash
brew install python
```
3. インストール確認：
```bash
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2. プロジェクトのセットアップ

1. このリポジトリをクローンまたはダウンロード
```bash
git clone https://github.com/long-910/py_merge_csv.git
cd py_merge_csv
```

2. 仮想環境の作成と有効化

#### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. 必要なパッケージのインストール
```bash
pip install -r requirements.txt
```

### 3. VS Codeの設定（推奨）

1. [VS Code](https://code.visualstudio.com/)をインストール
2. 以下の拡張機能をインストール：
   - Python (ms-python.python)
   - Rainbow CSV (mechatroner.rainbow-csv)

## 使用方法

### 基本的な使い方
```bash
python merge_csv.py ファイル1.csv ファイル2.csv キー名 [-o 出力ファイル名]
```

### 引数の説明

- `ファイル1.csv`: 1つ目のCSVファイルのパス
- `ファイル2.csv`: 2つ目のCSVファイルのパス
- `キー名`: マージに使用する列名
- `-o, --output`: 出力ファイル名（オプション、デフォルト: output.csv）

## 使用例

### テスト用CSVファイルの準備

1. `customers.csv`（顧客情報）:
```csv
customer_id,name,email,phone
1,山田太郎,yamada@example.com,090-1234-5678
2,鈴木花子,suzuki@example.com,090-2345-6789
```

2. `orders.csv`（注文情報）:
```csv
customer_id,order_id,product,amount,order_date
1,ORD001,ノートパソコン,150000,2024-03-01
2,ORD003,キーボード,8000,2024-03-01
```

### マージの実行

```bash
python merge_csv.py test_data/customers.csv test_data/orders.csv customer_id -o merged_result.csv
```

### 実行結果

マージされた`merged_result.csv`には以下のような結果が出力されます：
```csv
customer_id,name,email,phone,order_id,product,amount,order_date
1,山田太郎,yamada@example.com,090-1234-5678,ORD001,ノートパソコン,150000,2024-03-01
2,鈴木花子,suzuki@example.com,090-2345-6789,ORD003,キーボード,8000,2024-03-01
```

## 注意事項

- 両方のCSVファイルに指定されたキーが存在する必要があります
- 重複する列は自動的に1つにまとめられます
- エラーが発生した場合は、適切なエラーメッセージが表示されます
- CSVファイルはUTF-8エンコーディングで保存してください
- 大きなファイルを処理する場合は、十分なメモリが必要です

## トラブルシューティング

### よくある問題と解決方法

1. **Pythonが見つからない場合**
   - PATHの設定を確認
   - 仮想環境が有効化されているか確認

2. **パッケージのインストールエラー**
   - pipをアップグレード: `python -m pip install --upgrade pip`
   - 仮想環境が有効化されているか確認

3. **CSVファイルの文字化け**
   - ファイルがUTF-8で保存されているか確認
   - エンコーディングを指定して開く: `pd.read_csv(file, encoding='utf-8')`

4. **メモリエラー**
   - 大きなファイルの場合は、チャンク単位で処理することを検討
   - 不要な列を削除してからマージ