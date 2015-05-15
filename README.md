# junior_crawler
This code is from Zhu Junior.

這是蘊兒的程式碼，URL 的部分已經有將網址部分隱藏 `*url*`。

- test.py

    用來抓取 link 頁資料的程式

- f2.py

    用來存 150 則新聞。在蘊兒的測試中，因爲學校的網路大概會每 150 則就斷線一次，所以設定成一次抓取 150 筆資料。

- ITN-link.py

    用來抓取自由時報的 link 連結資料頁，需要手動輸入關鍵字及布林運算條件

- ITN.py

    抓取內文存成 csv 檔。分成時間、標題、版面和正文幾個欄位，新增了一個 url 的欄位
