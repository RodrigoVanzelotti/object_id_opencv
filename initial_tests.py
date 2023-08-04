import cv2
import mediapipe as mp
import numpy as np
import os

# running_mode          -> IMAGE, VIDEO, LIVE_STREAM                                            [DEFAULT SET]
# display_names         -> Default is en for english. Sets the language of the model            [DEFAULT SET]
# max_results           -> Define o maximo de retornos dado os tops scores (-1 retorna tudo)    [DEFAULT SET]
# score_threshold       -> Score Threshold, resultados abaixo do T são rejeitados
# category_allow_list   -> 
# category_deny_list    ->

# ** Não é possível usar category_allow_list e category_deny_list simultaneamente.

model_path = os.path.join('media_pipe_model', 'efficientdet_lite0.tflite')
