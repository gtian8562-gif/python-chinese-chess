# python-chinese-chess
一個使用 Python 純文字 terminal 運行的中國象棋遊戲
# ♟️ Python 純文字 CLI 中國象棋 (Chinese Chess)

一個基於 Python 二維陣列開發的終端機中國象棋遊戲。無須安裝第三方庫，純原生 Python 即可執行！

## ✨ 專案亮點與功能
- 📊 **座標化視覺棋盤**：採用 10x9 二維陣列設計，附帶數字座標，方便精準定位。
- ⚡ **流暢輸入**：支援 `6050` 連續 4 位數字指令（免加空格），操作極速。
- 🛡️ **完整棋步與違規判定**：
  - 支援所有棋子（車、馬、炮、將/帥、士、象、兵/卒）的合法移動邏輯。
  - **飛將（照面）自動檢查**：防止將帥同路且中間無子。
  - **九宮格限制**與**楚河漢界**範圍判定。
  - **塞象眼**與**拐馬腳**障礙物檢查。
  - **炮隔山打子**判定。
- ⚔️ **雙人輪流對弈**：自動切換紅黑回合，防止走錯棋子。

## 🚀 快速開始

### 執行需求
- Python 3.x

### 執行方式
1. 下載或複製本專案：
   ```bash
   git clone [https://github.com/gtian8562-gif/python-chinese-chess/tree/main](https://github.com/gtian8562-gif/python-chinese-chess/tree/main)
執行python3 chess.py/python chess.py
