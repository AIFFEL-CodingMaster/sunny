
import os
import argparse
from glob import glob
import tensorflow as tf

from make_tfrecord import MakeTFRecord
from preprocessing import delete_4_channel, label_encording

def preprocessing_1(data_path):
    data_path = data_pathh + "*"
    data_list = glob(data_path)
    
    #전처리
    data_list = delete_mat(data_list)
    data_list = delete_4_ckannel(data_list)
    
    data_class = label_encording(data_list)
    return data_list, data_class

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=['tfr', 'train','test'], help="TFRecord만들기 or 모델 학습 or 모델 테스트")
    parser.add_argument("--data_path", type=str, default=".\", help="데이터가 들어있는 디렉토리 경로")
    parser.add_argument("--tfr_path", type=str, default=".\", help="tfrecord 가 저장될 디렉토리")
    parser.add_argument("--img_size", type=int, default=224, help="이미지 사이즈 입력")
    args = parser.parse_args()
                        
    if args.mode == "tfr":
        data_list, data_class = proprocessing_1(args.data_path)
                        
        IMG_SIZE = args.img_size
        tfrecord = MakeTFRecord(
            data_list = data_list,
            tfr_path = args.tfr_path,
            data_class = data_class
        )
                        
        if args.img_size !=224:
            tfrecord.change_img_size(args.img_size)
        #tfrecord 만들기
        tfrecord()
                        
