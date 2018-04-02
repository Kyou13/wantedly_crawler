# wantedly_crawler
- 対象サイト
    - wantedly
- 対象情報
    - タイトル    
    - URL
    - エントリー数
    
## 0329
- 一覧のページは3000ページほどあるが、100ページまでしか情報がない。
    - 1000件ほどしか情報がとれない
- 記事id総当りに変更    

## 0331
- 全データ取得完了
    - **107,689**件
    - 2台で約2日かかった
*****
    
- tips    
    - scrapy高速化
      - https://doc.scrapy.org/en/latest/topics/broad-crawls.html
    - アウトプットの指定方法
      - https://doc.scrapy.org/en/latest/topics/feed-exports.html
- Sequel Proでcsvとしてエクスポードしたものがエクセルで開くと文字化けする
    - 文字コーディングを**UTF-8 BOM**に変更
          
- mysql          
   - ダンプ
    ```aidl
    $ mysqldump -u user -p db_name > dump.sql
    ```
   - ダンプファイルからのインポート
   ```
   $ mysql -u user -p db_name < dump_file
   ```
   - DB作成
   ```aidl
    CREATE DATABASE db_name;
    ```
   - DB削除 
   ```aidl
    DROP DATABASE db_name;
    ```
    
    - 定義が同じテーブルで全件インサート
    ```aidl
    INSERT INTO テーブルA
    SELECT * 
    FROM   テーブルB
    ```
