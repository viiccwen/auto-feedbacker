# AutoFeedbacker

> TAs 互評表計算自動化

## 介紹
我是作者Vic，這是為了節省我時間做的自動化流程XD，因為互評表統整是個非常枯燥的工作，因此將其自動化。

## 檔案結構

```
└─Root
    │  README.md
    │
    ├─docs
    │      feedback.xlsx
    │      output.xlsx
    │
    └─src
            test.py
            main.py
```

## 使用教學
1. 將欲評分的資料集copy and paste到feedback.xlsx中，務必記得首行請勿刪除，必須要有首行才能正常偵測

2. 點開 `main.py` ，將第7行的 `MOD` 指定 (有兩種 SDGs 和 Inter)，及指定路徑。

3. 進入 `src` 資料夾中，打開command line，輸入 `python main.py`

4. 前往 `output.py`，取得分析結果 