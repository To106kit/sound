# %%
from pydub import AudioSegment
import os
import pathlib
import numpy as np

def synthsiswab():

    # 初期化
    # 合成用の入力ファイル格納先を取得
    ######### 入力ファイル格納先により以下パスを変更すること。########
    t_base_path = "D:\\11_github\\sound\\result\\demcsgui"
    ######### 出力(合成)ファイル格納先により以下パスを変更すること。########
    t_outputBaseDir = "D:\\11_github\\sound\\result\\synthesis"
    t_bass_name = "bass.wav"
    t_drums_name = "drums.wav"
    t_other_name = "other.wav"
    t_synthsys_sound_list = []

    # 入力対象フォルダ一覧を取得
    t_input_list= os.listdir(t_base_path)
    t_input_dir_list = [f for f in t_input_list if os.path.isdir(os.path.join(t_base_path, f))]

    # 合成ループ処理
    for t_idx_path in t_input_dir_list:
        # 出力先ファイル名を作成
        # フォルダ名から不要な文字列".mp3_separated"を削除
        t_replace_name = t_idx_path.replace(".mp3_separated","")
        t_output_path = os.path.join(t_outputBaseDir, t_replace_name)
        # 出力先ディレクトリが存在しない場合は作成
        os.makedirs(t_output_path, exist_ok=True)
        t_output_file = os.path.join(t_output_path, "mixed_sounds.wav") # 出力ファイル名
        # すでに合成済みであれば、なにもせず次対象に移る。
        if os.path.isfile(t_output_file):
            # print("this wav is used synthesis. So Skip.")
            continue
        else:
            # 合成していないため、合成処理に移る。
            t_abs_path = os.path.join(t_base_path, t_idx_path)
            t_sound_name = os.path.splitext(os.path.basename(t_abs_path))[0]
            t_synthsys_sound_list = t_synthsys_sound_list + [t_sound_name]
            # 入力ファイルパスを作成
            t_bass_sound = os.path.join(t_abs_path, t_bass_name)
            t_drums_sound = os.path.join(t_abs_path, t_drums_name)
            t_other_sound = os.path.join(t_abs_path, t_other_name)

            # AudioSegmentオブジェクト作成
            t_bass_obj = AudioSegment.from_file(t_bass_sound)
            t_drums_obj = AudioSegment.from_file(t_drums_sound)
            t_other_obj = AudioSegment.from_file(t_other_sound)

            # 合成
            t_output1 = t_bass_obj.overlay(t_drums_obj)
            t_output2 = t_output1.overlay(t_other_obj)

            # 保存
            t_output2.export(t_output_file, format="wav")

    t_synth_sound_for_print = "\n".join(t_synthsys_sound_list)
    # エスケープシーケンス無効化
    print(repr(t_synth_sound_for_print))
    return t_synthsys_sound_list

if __name__ == "__main__":
    synthsiswab()
