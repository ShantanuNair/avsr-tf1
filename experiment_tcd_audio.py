import avsr
import os
os.environ['CUDA_VISIBLE_DEVICES'] = "0"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"  # ERROR
import sys


def main(argv):

    num_epochs = int(argv[1])
    learning_rate = float(argv[2])

    experiment = avsr.AVSR(
        unit='character',
        unit_file='/run/media/john_tukey/download/datasets/MV-LRS/misc/character_list',
        video_processing=None,
        #cnn_filters=(12, 32, 64, 96),
        cnn_filters=(8, 16, 32, 64),
        cnn_dense_units=64,
        batch_normalisation=True,
        video_train_record='/run/media/john_tukey/download/datasets/tcdtimit/tfrecords3/rgb36lips_train_sd.tfrecord',
        video_test_record='/run/media/john_tukey/download/datasets/tcdtimit/tfrecords3/rgb36lips_test_sd.tfrecord',
        # video_test_record='/run/media/john_tukey/download/datasets/tcdtimit/tfrecords3/rgb36lips_newtrain_50spk.tfrecord',
        audio_processing='features',
        audio_train_record='/run/media/john_tukey/download/datasets/tcdtimit/tfrecords_del/logmel_train_sd_stack_w6s3_clean.tfrecord',
        audio_test_record='/run/media/john_tukey/download/datasets/tcdtimit/tfrecords_del/logmel_train_sd_stack_w6s3_clean.tfrecord',
        labels_train_record ='/run/media/john_tukey/download/datasets/tcdtimit/tfrecords3/characters_train_sd.tfrecord',
        labels_test_record ='/run/media/john_tukey/download/datasets/tcdtimit/tfrecords3/characters_train_sd.tfrecord',
        # labels_test_record='/run/media/john_tukey/download/datasets/tcdtimit/tfrecords3/characters_newtrain_50spk.tfrecord',
        encoder_type='unidirectional',
        architecture='unimodal',
        clip_gradients=True,
        max_gradient_norm=1.0,
        recurrent_regularisation=0.0001,
        cell_type='gru',
        embedding_size=128,
        highway_encoder=False,
        sampling_probability_outputs=0.1,
        use_dropout=True,
        #dropout_probability=(0.7, 0.7, 0.7),
        decoding_algorithm='beam_search',
        enable_attention=True,
        encoder_units_per_layer=(128, 128, 128),
        decoder_units_per_layer=(128, ),
        attention_type=(('scaled_luong', )*1, ('scaled_luong', )*1),
        mwer_training=False,
        beam_width=10,
        batch_size=(64, 64),
        optimiser='AMSGrad',
        learning_rate=learning_rate,
        label_skipping=False,
        num_gpus=1,
    )

    uer = experiment.evaluate(
      checkpoint_path='./checkpoints/tcd_audio_to_chars_3x128_1xattn_nohw_128emb_s6w3/checkpoint.ckp-415',
    )
    print(uer)
    return

    experiment.train(
        num_epochs=num_epochs,
        logfile='./logs/tcd_audio_to_chars_3x256_3xattn_nohw_256emb_s6w3',
        try_restore_latest_checkpoint=True
    )



if __name__ == '__main__':
    main(sys.argv)
