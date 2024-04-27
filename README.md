# AutoFeedbacker

> TAs 互評表計算自動化

## 介紹
這是為了節省時間做的自動化流程，因為互評表統整是個非常枯燥的工作，因此將其自動化。

## 檔案結構

```
└─Root
    │  README.md
    │
    ├─docs
    │      feedback.xlsx
    │      feedback_output.xlsx
    │      peer.xlsx
    │      peer_output.xlsx
    │
    └─src
            test.py
            main.py
            config.txt
```

## 使用教學
1. 進入 `config.txt` ，設置好各類變數（input file, output file, mode, path...） 

2. 請務必確保file / path / mode存在

3. 將欲評分的資料集copy and paste到你指定的input file中，務必記得範例input檔案首行請勿刪除，必須要有首行才能正常偵測

3. 進入 `src` 資料夾中，打開command line，輸入 `python main.py`

4. 前往你指定的output file，取得分析結果 