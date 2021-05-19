# 7seg-image-generator-for-Axross
7セグメント表示の画像を生成するツールです。<br>
主に機械学習の学習データセットに使用することを想定しています。<br>
0~9、-(マイナス記号)、表示なしのデータを生成します。<br>
<img src="https://user-images.githubusercontent.com/37477845/118017307-6c16de80-b391-11eb-9fc2-547f66f59e9f.png" width="400px">

# Requirement 
* OpenCV 3.4.2 or later
* tqdm 4.48.2 or later
* albumentations 0.5.2 or later　※create_7segment_dataset_da.py を使用する場合のみ

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
デフォルト：3000
* --erase_debug_window<br>
デバッグ表示用のウィンドウの非表示<br>
デフォルト：指定なし
* --seed<br>
乱数シード<br>
デフォルト：42

また、「create_7segment_dataset.py」を用いるとデータ拡張を実施した状態で画像を生成します。<br>
<img src="https://user-images.githubusercontent.com/37477845/118017348-7638dd00-b391-11eb-86e1-5fa2f32fcda4.png" width="400px">

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
7seg-image-generator-for-Axross is under [Apache-2.0 License](LICENSE).
