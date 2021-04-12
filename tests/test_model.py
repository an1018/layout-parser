from layoutparser import load_json
from layoutparser.models import *
import cv2

ALL_CONFIGS = [
    "lp://PrimaLayout/mask_rcnn_R_50_FPN_3x/config",
    "lp://HJDataset/faster_rcnn_R_50_FPN_3x/config",
    "lp://HJDataset/mask_rcnn_R_50_FPN_3x/config",
    "lp://HJDataset/retinanet_R_50_FPN_3x/config",
    "lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config",
    "lp://PubLayNet/mask_rcnn_R_50_FPN_3x/config",
    "lp://PubLayNet/mask_rcnn_X_101_32x8d_FPN_3x/config",
    "lp://NewspaperNavigator/faster_rcnn_R_50_FPN_3x/config",
    "lp://TableBank/faster_rcnn_R_50_FPN_3x/config",
    "lp://TableBank/faster_rcnn_R_101_FPN_3x/config",
]


def test_Detectron2Model(is_large_scale=False):

    if is_large_scale:

        for config in ALL_CONFIGS:
            model = Detectron2LayoutModel(config)

            image = cv2.imread("tests/fixtures/model/test_model_image.jpg")
            layout = model.detect(image)
    else:
        model = Detectron2LayoutModel("tests/fixtures/model/config.yml")
        image = cv2.imread("tests/fixtures/model/test_model_image.jpg")
        layout = model.detect(image)
        
    # Test in enforce CPU mode
    model = Detectron2LayoutModel("tests/fixtures/model/config.yml", enforce_cpu=True)
    image = cv2.imread("tests/fixtures/model/test_model_image.jpg")
    layout = model.detect(image)
    
def test_Detectron2Model_version_compatibility(enabled=True):
    
    if enabled:
        model = Detectron2LayoutModel(
            config_path="lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config",
            extra_config=[
                "MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.85,
                "MODEL.ROI_HEADS.NMS_THRESH_TEST", 0.75,
            ],
        )
        image = cv2.imread("tests/fixtures/model/layout_detection_reference.jpg")
        layout = model.detect(image)
        assert load_json("tests/fixtures/model/layout_detection_reference.json") == layout