# 7seg-image-generator-for-Axross
「[Raspberry piでリアルタイムに7セグメントディスプレイを読み取るレシピ](https://axross-recipe.com/recipes/196)」用の7セグメント表示の画像を生成するツールです。<br>
0~9、-(マイナス記号)、表示なしのデータを生成します。<br><br>
<img src="https://user-images.githubusercontent.com/37477845/118855777-24ec9880-b911-11eb-9d82-888b53a2010e.png" width="800px">

# Requirement 
* OpenCV 3.4.2 or later
* tqdm 4.48.2 or later
* albumentations 0.5.2 or later

# Usage
実行方法は以下です。
```bash
python create_7segment_dataset.py
```
生成時のオプションとして以下を指定できます。
* --width<br>
生成画像の幅<br>
デフォルト：96
* --height<br>
生成画像の高さ<br>
デフォルト：96
* --number_width_min<br>
セグメント表示の横幅の最小割合<br>
デフォルト：0.1
* --number_width_max<br>
セグメント表示の横幅の最大割合<br>
デフォルト：0.9
* --number_height_min<br>
セグメント表示の高さの最小割合<br>
デフォルト：0.4
* --number_height_max<br>
セグメント表示の高さの最大割合<br>
デフォルト：0.9
* --thickness_min<br>
セグメント表示の横幅を1とした際の線の太さの最小割合<br>
デフォルト：0.01
* --thickness_max<br>
セグメント表示の横幅を1とした際の線の太さの最大割合<br>
デフォルト：0.25
* --blank_ratio_min<br>
セグメント同士の隙間の最小割合<br>
デフォルト：0.0
* --blank_ratio_max<br>
セグメント同士の隙間の最大割合<br>
デフォルト：0.1
* --shear_x_min<br>
セグメント表示のX軸方向の傾きの最小<br>
デフォルト：-10
* --shear_x_min<br>
セグメント表示のX軸方向の傾きの最大<br>
デフォルト：30
* --shift_x_min<br>
セグメント表示のX軸方向シフトの最小ピクセル<br>
デフォルト：-10
* --shift_x_max<br>
セグメント表示のX軸方向シフトの最大ピクセル<br>
デフォルト：10
* --shift_y_min<br>
セグメント表示のY軸方向シフトの最小ピクセル<br>
デフォルト：-10
* --shift_y_max<br>
セグメント表示のY軸方向シフトの最大ピクセル<br>
デフォルト：10
* --steps<br>
各クラスを何枚ずつ生成するか<br>
デフォルト：5000
* --erase_debug_window<br>
デバッグ表示用のウィンドウの非表示<br>
デフォルト：指定なし
* --seed<br>
乱数シード<br>
デフォルト：42

# Original Repository
[Kazuhito00/7seg-image-generator](https://github.com/Kazuhito00/7seg-image-generator)

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
7seg-image-generator-for-Axross is under [Apache-2.0 License](LICENSE).
